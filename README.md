# Video-Game-Recommendation-Engine


## Objective
* Gather the data using Giant Bomb API.
* Complete exploratory data analysis.
* Analyze recommendation methods.
* Deploy Application

## Background Information
* With the number of products increasing exponentially, it burdens the consumer in which products to purchase. A novel solution is the use of recommender systems (engines) to "recommend" relevant products to the consumers based on their preferences. Applications of recommender systems include areas such as playlist generators for video and music services like Netflix, YouTube, and Spotify. Additionally, product recommendations for services such as Amazon. In this project, we'll explore novel techniques in recommending video games using the Giant Bomb video game database. 

---
## Repository Structure
```plaintext
eBay-web-crawler-phone-auctions/
├── Dashboard/                              # Contains files related to the live dashboard
│   ├── assets/                             # CSS/IMG files used in the dashboard
│   ├── layout_assets/                      # All functions used to create the figures in the dashboard layout
│   ├── model/                              # Model related functions
│   ├── Procfile                            # Configuration of the web application
│   ├── app.py                              # Defines the server application
│   ├── index.py                            # Defines the layout of the application
│   └── requirements.txt                    # Python dependencies for the dashboard
├── Scraping_Application_Docker/            # Dockerized web scraping application
│   ├── Dockerfile                          # Dockerfile for setting up the scraping environment
│   ├── active_auctions.py                  # Checks for active auctions and updates the SQL databases
│   ├── clear_db.py                         # Checks if the number of rows in the SQL database exceeds 10,000 rows
│   ├── remove_duplicates.py                # Removes all duplicate item ids from the SQL database
│   ├── requirements.txt                    # Python dependencies for the scraper
|   └── scraper.py                          # Main web scraping script
├── Animation.gif                           # GIF demonstrating the application's functionality
├── LICENSE                                 # Licensing information for the repository
└── README.md                               # Overview of the repository
```
---
## Process:
* Preprocessing (NLP packages)
* Exploratory Data Analysis conducted utilizing various python packages (Numpy, Matplotlib, Pandas, and Plotly).'
* Recommendation Methods.
    * TF-IDF
        * Cosine Similarity
        * Cosine Similarity + Singular Value Decomposition
        * K-Nearest Neighbors
        * K-Nearest Neighbors + Singular Value Decomposition
* PostgreSQL database.



## Table of Contents:
* Part I: Data Exploration
    * Gathering
    * Preprocessing
    * Exploration
* Part II: Recommendation Methods
    * TF-IDF
    * Cosine Similarity
    * KNN
    * SVD
        * Cosine Similarity
        * KNN
    * Results
* Part III: PostgreSQL database for application deployment.
   
* Pertinent Deliverables
	* [Jupyter Notebook](https://github.com/SulmanK/Video-Game-Recommendation-Engine/blob/master/Video%20Game%20Recommendation%20Engine.ipynb)
	* [Dashboard](http://video-game-rec-env.eba-bmsnxzwj.us-east-1.elasticbeanstalk.com/)

* Demo

![Demo](Animation.gif)

* References
  * S. Qaiser and R. Ali, "Text Mining: Use of TF-IDF to Examine the Relevance of Words to Documents", International Journal of Computer Applications, vol. 181, no. 1, pp. 25-29, 2018. Available: 10.5120/ijca2018917395.

  * "Recommendation system Based On Cosine Similarity Algorithm", International Journal of Recent Trends in Engineering and Research, vol. 3, no. 9, pp. 6-10, 2017. Available: 10.23883/ijrter.2017.3423.iss9x.

  * B. Trstenjak, S. Mikac and D. Donko, "KNN with TF-IDF based Framework for Text Categorization", Procedia Engineering, vol. 69, pp. 1356-1364, 2014. Available: 10.1016/j.proeng.2014.03.129.

  * "Singular Value Decomposition", Iridl.ldeo.columbia.edu, 2020. [Online]. Available: http://iridl.ldeo.columbia.edu/dochelp/StatTutorial/SVD/index.html. [Accessed: 20- Jul- 2020].


