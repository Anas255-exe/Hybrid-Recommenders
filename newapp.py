from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Constants for API URLs
API_BASE_URL = "https://api.socialverseapp.com"
FLIC_TOKEN = "flic_6e2d8d25dc29a4ddd382c2383a903cf4a688d1a117f6eb43b35a1e7fadbb84b8"

# Function to fetch posts based on user interactions
def fetch_user_posts(endpoint):
    headers = {"Flic-Token": FLIC_TOKEN}
    response = requests.get(endpoint, headers=headers)
    if response.status_code != 200:
        return {"error": "Failed to fetch data from API", "status_code": response.status_code}
    return response.json()

# Function to recommend posts based on user interactions
def recommend_posts(user_id, category_id=None, mood=None):
    # Fetch user interactions
    viewed_posts = fetch_user_posts(f"{API_BASE_URL}/posts/view?page=1&page_size=1000")
    liked_posts = fetch_user_posts(f"{API_BASE_URL}/posts/like?page=1&page_size=1000")
    inspired_posts = fetch_user_posts(f"{API_BASE_URL}/posts/inspire?page=1&page_size=1000")
    rated_posts = fetch_user_posts(f"{API_BASE_URL}/posts/rating?page=1&page_size=1000")
    all_posts = fetch_user_posts(f"{API_BASE_URL}/posts/summary/get?page=1&page_size=1000")

    # Check for errors in fetching data
    if "error" in viewed_posts or "error" in liked_posts or "error" in inspired_posts or "error" in rated_posts or "error" in all_posts:
        return {"error": "Error fetching user posts", "details": [viewed_posts, liked_posts, inspired_posts, rated_posts, all_posts]}

    # Collect post IDs from user interactions
    viewed_post_ids = {post['id'] for post in viewed_posts.get('posts', []) if 'id' in post}
    liked_post_ids = {post['id'] for post in liked_posts.get('posts', []) if 'id' in post}
    inspired_post_ids = {post['id'] for post in inspired_posts.get('posts', []) if 'id' in post}
    rated_post_ids = {post['id'] for post in rated_posts.get('posts', []) if 'id' in post}

    # Combine all user interactions
    user_interacted_post_ids = viewed_post_ids.union(liked_post_ids, inspired_post_ids, rated_post_ids)

    # Filter all posts based on user interactions, category, and mood
    recommended_posts = []
    for post in all_posts.get('posts', []):
       

        if post['id'] in user_interacted_post_ids:
            continue  # Skip posts the user has already interacted with

        # Check category and mood filters
        if (category_id is None or post.get('category_id') == category_id) and \
           (mood is None or post.get('mood') == mood):
             recommended_posts.append(post)

    return recommended_posts[:10]  # Return top 10 recommended posts

# Route to get recommended posts based on username, category_id, and mood
@app.route('/feed', methods=['GET'])
def get_feed():
    username = request.args.get('username')
    category_id = request.args.get('category_id')
    mood = request.args.get('mood')

    # Fetch user ID based on username
    users_response = fetch_user_posts(f"{API_BASE_URL}/users/get_all?page=1&page_size=1000")
    user_id = next((user['id'] for user in users_response.get('users', []) if user['username'] == username), None)

    if user_id is None:
        return jsonify({"status": "error", "message": "User  not found"}), 404

    # Get recommended posts
    recommended_posts = recommend_posts(user_id, category_id, mood)

    if "error" in recommended_posts:
        return jsonify({"status": "error", "message": recommended_posts["error"], "details": recommended_posts["details"]}), 500


    return jsonify({"status": "success", "recommended_posts": recommended_posts})

# Route to get recommended posts based on username and category_id
@app.route('/feed/category', methods=['GET'])
def get_feed_by_category():
    username = request.args.get('username')
    category_id = request.args.get('category_id')

    # Fetch user ID based on username
    users_response = fetch_user_posts(f"{API_BASE_URL}/users/get_all?page=1&page_size=1000")
    user_id = next((user['id'] for user in users_response.get('users', []) if user['username'] == username), None)

    if user_id is None:
        return jsonify({"status": "error", "message": "User  not found"}), 404

    # Get recommended posts
    recommended_posts = recommend_posts(user_id, category_id=category_id)

    if "error" in recommended_posts:
        return jsonify({"status": "error", "message": recommended_posts["error"], "details": recommended_posts["details"]}), 500

    return jsonify({"status": "success", "recommended_posts": recommended_posts})

# Route to get recommended posts based on username and mood
@app.route('/feed/mood', methods=['GET'])
def get_feed_by_mood():
    username = request.args.get('username')
    mood = request.args.get('mood')

    # Fetch user ID based on username
    users_response = fetch_user_posts(f"{API_BASE_URL}/users/get_all?page=1&page_size=1000")
    user_id = next((user['id'] for user in users_response.get('users', []) if user['username'] == username), None)

    if user_id is None:
        return jsonify({"status": "error", "message": "User  not found"}), 404

    # Get recommended posts
    recommended_posts = recommend_posts(user_id, mood=mood)

    if "error" in recommended_posts:
        return jsonify({"status": "error", "message": recommended_posts["error"], "details": recommended_posts["details"]}), 500

    return jsonify({"status": "success", "recommended_posts": recommended_posts})

if __name__ == '__main__':
    app.run(debug=True)