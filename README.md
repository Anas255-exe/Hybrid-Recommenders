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

**Thanks for taking my application into consideration**
Feel free to reach out with any questions or feedback!  
