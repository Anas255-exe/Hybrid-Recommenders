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

 ### Key Decisions Made During Development

During the development of this project, several key decisions and challenges were encountered that shaped the implementation process. Below are the major decisions and problems faced:

1. **Model Selection**: 
   Initially, I explored several models to implement the video recommendation system. After researching, I decided to experiment with K-Nearest Neighbors (KNN) for the recommendation algorithm. However, after a series of trials, I faced difficulties in implementing it effectively due to issues in data handling and model integration.

2. **Data Inconsistencies**: 
   One of the significant challenges encountered during the implementation was inconsistencies in the dataset. Specifically, there were discrepancies in how the `user_id` variable was represented across different parts of the data. In some places, the variable was referred to as `id`, while in others, it was labeled as `user_id`. This caused confusion when trying to merge or process the data, leading to errors and delays in the implementation. To resolve this, I had to manually standardize the variable names across the dataset to ensure consistency and smooth data processing.

3. **Modeling Approach**: 
   Due to the difficulties with KNN, I eventually pivoted to exploring alternative approaches for building the recommendation system. This required significant rethinking of the data flow and model selection to ensure better accuracy and scalability. This decision was pivotal to moving the project forward and achieving a more robust recommendation system.

4. **Data Preprocessing**:
   During the preprocessing stage, I had to ensure that all features and data points were aligned correctly. This involved cleaning up missing values, handling inconsistent variable names, and formatting data for compatibility with the chosen recommendation algorithm. The inconsistencies, especially in variable names, were a roadblock at this stage and took considerable time to resolve.


**Thanks for taking my application into consideration**
Feel free to reach out with any questions or feedback!  
