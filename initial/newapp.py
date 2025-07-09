from flask import Flask, request, jsonify
import requests
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Base URL for the API and token for authentication
API_BASE_URL = "https://api.socialverseapp.com"
FLIC_TOKEN = "flic_6e2d8d25dc29a4ddd382c2383a903cf4a688d1a117f6eb43b35a1e7fadbb84b8"

# Fetch posts or user data from the API
def fetch_user_posts(endpoint):
    headers = {"Flic-Token": FLIC_TOKEN}
    response = requests.get(endpoint, headers=headers)
    if response.status_code != 200:
        return {"error": "Could not fetch data from the API", "status_code": response.status_code}
    return response.json()

# Recommend posts for a user using k-Nearest Neighbors (k-NN)
def recommend_posts_knn(user_id, category_id=None, mood=None, k=10):
    # Get all posts and user interaction data
    all_posts_response = fetch_user_posts(f"{API_BASE_URL}/posts/summary/get?page=1&page_size=1000")
    viewed_posts = fetch_user_posts(f"{API_BASE_URL}/posts/view?page=1&page_size=1000")

    if "error" in all_posts_response or "error" in viewed_posts:
        return {"error": "Error while fetching posts", "details": [all_posts_response, viewed_posts]}

    all_posts = all_posts_response.get('posts', [])
    viewed_post_ids = {post['id'] for post in viewed_posts.get('posts', []) if 'id' in post}

    # Prepare feature matrix and post IDs list
    post_features = []
    post_ids = []
    for post in all_posts:
        # Filter by category and mood if specified
        if category_id is not None and post.get('category_id') != category_id:
            continue
        if mood is not None and post.get('mood') != mood:
            continue

        # Represent each post as a vector of its attributes
        feature_vector = [
            post.get('likes', 0),
            post.get('views', 0),
            post.get('inspirations', 0),
            post.get('ratings', 0)
        ]
        post_features.append(feature_vector)
        post_ids.append(post['id'])

    if not post_features:
        return []

    post_features = np.array(post_features)

    # Create a vector summarizing the user's interactions
    user_vector = np.zeros(len(post_features[0]))
    for post in all_posts:
        if post['id'] in viewed_post_ids:
            user_vector += np.array([
                post.get('likes', 0),
                post.get('views', 0),
                post.get('inspirations', 0),
                post.get('ratings', 0)
            ])

    # Calculate similarity between the user and each post
    similarities = cosine_similarity([user_vector], post_features)[0]

    # Select the top-k most similar posts
    recommended_indices = np.argsort(similarities)[::-1][:k]
    recommended_posts = [
        {
            "id": post_ids[i],
            "similarity": similarities[i],
            **all_posts[i]
        }
        for i in recommended_indices if post_ids[i] not in viewed_post_ids
    ]

    return recommended_posts

# Endpoint to get recommended posts based on username, category, and mood
@app.route('/feed', methods=['GET'])
def get_feed():
    username = request.args.get('username')
    category_id = request.args.get('category_id', type=int)
    mood = request.args.get('mood')

    # Find the user ID by username
    users_response = fetch_user_posts(f"{API_BASE_URL}/users/get_all?page=1&page_size=1000")
    user_id = next((user['id'] for user in users_response.get('users', []) if user['username'] == username), None)

    if user_id is None:
        return jsonify({"status": "error", "message": "User not found"}), 404

    # Get recommendations for the user
    recommended_posts = recommend_posts_knn(user_id, category_id, mood)

    if "error" in recommended_posts:
        return jsonify({"status": "error", "message": recommended_posts["error"], "details": recommended_posts["details"]}), 500

    return jsonify({"status": "success", "recommended_posts": recommended_posts})

if __name__ == '__main__':
    app.run(debug=True)
