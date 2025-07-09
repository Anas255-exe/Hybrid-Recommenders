# Hybrid Recommendation System  

## Overview  
This project implements a hybrid recommendation system for personalized content recommendations based on user interactions, preferences, and collaborative filtering techniques. The API provides endpoints to fetch recommended posts based on username, category, and mood.

---

## Setup and Installation  
![image](https://github.com/user-attachments/assets/ed6b24e9-2966-4e44-b7b8-0575c3db5912)


### Prerequisites  
Ensure you have the following installed:  
- Python 3.7 or above  
- Flask  
- `requests` library  

### Installation Steps  
1. Clone the repository:


```bash
git clone https://github.com/Anas255-exe/Video_recommendation-.git
cd Video_recommendation-
```


3. Install dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  



4. Run the Flask app:  
   ```bash  
   python app.py  
   ```  

5. Access the API at `http://127.0.0.1:5000`.  

---

## Testing the API  

### Test Cases  

1. **Fetch Recommended Posts by Username, Category, and Mood**  
   - **Endpoint:** `/feed`  
   - **Method:** `GET`  
   - **Parameters:**  
     - `username` (string): Username of the user.  
     - `category_id` (optional, string): Category filter.  
     - `mood` (optional, string): Mood filter.  
   - **Example Request:**  
     ```bash  
     curl "http://127.0.0.1:5000/feed?username=kinha&category_id=1&mood=happy"  
     ```  

2. **Fetch Recommended Posts by Category**  
   - **Endpoint:** `/feed/category`  
   - **Method:** `GET`  
   - **Parameters:**  
     - `username` (string): Username of the user.  
     - `category_id` (string): Category filter.  
   - **Example Request:**  
     ```bash  
     curl "http://127.0.0.1:5000/feed/category?username=kinha&category_id=1"  
     ```  

3. **Fetch Recommended Posts by Mood**  
   - **Endpoint:** `/feed/mood`  
   - **Method:** `GET`  
   - **Parameters:**  
     - `username` (string): Username of the user.  
     - `mood` (string): Mood filter.  
   - **Example Request:**  
     ```bash  
     curl "http://127.0.0.1:5000/feed/mood?username=kinha&mood=excited"  
     ```  

---

## How the Algorithm Works  

### Hybrid Recommendation Approach  
1. **Input Stage:**  
   - Collects user interactions including:  

     - Viewed Posts  
     - Liked Posts  
     - Inspired Posts  
     - Rated Posts
  <img src="https://github.com/user-attachments/assets/68c87835-a00b-436f-b157-15ac73d45d0b" alt="Description of Image" width="500" height="300">
      

2. **Content-Based Filtering:**  
   - Filters posts based on:  
     - Categories of interest.  
     - Mood preferences.
     
       
   <img src="https://github.com/user-attachments/assets/2affebfc-fa00-4bb8-81f1-57019d7f7e55" alt="Description of Image" width="500" height="300">


3. **Collaborative Filtering:**  
   - Analyzes posts interacted with by similar users.  
   - Recommends posts liked or rated by these users.
  
     
      <img src="https://github.com/user-attachments/assets/f56620bf-b1de-476c-beb0-476e8777c00e" alt="Description of Image" width="500" height="300">


4. **Hybrid Recommendation Engine:**  
   - Combines the results from content-based and collaborative filtering.  
   - Prioritizes posts that meet both criteria.


     <img src="https://github.com/user-attachments/assets/6f6c2696-c9c1-4e06-808c-10f31ebf2927" alt="Description of Image" width="500" height="300">

5. **Output:**  
   - Returns the top 10 recommended posts.  


 <img src="https://github.com/user-attachments/assets/4541bcd0-9acb-4b49-85df-679b75a7f742" alt="Description of Image" width="500" height="300">


---

### Key Decisions Made During Development

During the development of this recommendation system, the initial approach was to implement the K-Nearest Neighbors (KNN) algorithm to provide video recommendations. This approach was chosen because of the simplicity and effectiveness of KNN in identifying patterns from user preferences based on ratings or features.

**KNN Approach**

KNN operates by calculating the similarity (or distance) between users (or items), identifying the nearest neighbors, and using their preferences or ratings to predict ratings for unseen items. However, during the implementation, a few challenges arose:

1. **Model Selection**: Initially, I tried using KNN as a recommendation model. However, I encountered difficulties in adjusting the model and processing the data effectively. This led to exploring alternative approaches like content-based or collaborative filtering methods.
  
2. **Data Inconsistencies**: One major issue encountered was the inconsistency in variable names used across different datasets. Specifically, the variable `user_id` was sometimes referred to as `id`, which caused problems during data merging and distance computation for KNN. Resolving this inconsistency was critical to the successful implementation of the model.

3. **Similarity Calculations**: KNN requires the computation of similarities between users or items. Initially, I used Euclidean Distance to measure the similarity between users. Later, I considered switching to Cosine Similarity for better performance, especially in sparse datasets, as it accounts for the direction of ratings rather than the magnitude.

**Equations Attempted in KNN**

The following key equations were part of the KNN implementation and were used to calculate distances and predict ratings:

1. **Euclidean Distance**

Euclidean Distance is a standard method used to calculate the similarity between two data points (users or items). The formula is:

d(x, y) = √(∑(xi - yi)²)

Where:
- x and y are data points (user/item feature vectors).
- n is the number of features/items.
- xi and yi are the values of the i-th feature.

2. **KNN Prediction Formula**

The prediction for a user u on an item i is calculated as:

r̂(u,i) = (∑(v ∈ N_k(u)) sim(u,v) * r(v,i)) / (∑(v ∈ N_k(u)) sim(u,v))

Where:
- r̂(u,i) is the predicted rating for user u on item i.
- N_k(u) is the set of k nearest neighbors of user u.
- sim(u,v) is the similarity between user u and user v.
- r(v,i) is the actual rating given by user v for item i.

3. **Cosine Similarity**

An alternative to Euclidean distance is Cosine Similarity, which calculates the cosine of the angle between two vectors. The formula is:

sim(u,v) = (∑(r(u,i) * r(v,i))) / (√(∑(r(u,i)²)) * √(∑(r(v,i)²)))

Where:
- r(u,i) and r(v,i) are the ratings given by users u and v for item i.
- n is the number of items.

4. **Weighted Average Prediction**

For better accuracy, a weighted average of neighbors' ratings can be used instead of a simple average:

r̂(u,i) = (∑(v ∈ N_k(u)) sim(u,v) * r(v,i)) / (∑(v ∈ N_k(u)) |sim(u,v)|)

Where:
- The numerator is the weighted sum of ratings from the nearest neighbors.
- The denominator normalizes the weights.
  


**Problems Faced:**
Inconsistencies in Variable Naming
One of the main issues I encountered was the inconsistency in variable names, particularly with user_id. In some places, it was referred to as id, and in other places, it was referred to as user_id. This inconsistency caused errors during data processing and model training, as the variables were not properly mapped. I had to carefully refactor the code and standardize the naming convention across the entire project.


Feel free to reach out with any questions or feedback!  
