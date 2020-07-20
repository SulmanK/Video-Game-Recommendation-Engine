# Video-Game-Recommendation-Engine


## Objective
* Gather the data using Giant Bomb API.
* Complete exploratory data analysis.
* Analyze recommendation methods.
* Deploy Application

## Background Information
* With the number of products increasing exponentially, it burdens the consumer in which products to purchase. A novel solution is the use of recommender systems (engines) to "recommend" relevant products to the consumers based on their preferences. Applications of recommender systems include areas such as playlist generators for video and music services like Netflix, YouTube, and Spotify. Additionally, product recommendations for services such as Amazon. In this project, we'll explore novel techniques in recommending video games using the Giant Bomb video game database. 

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
	* [Jupyter Notebook](https://github.com/SulmanK/Customer-Churn-in-World-of-Warcraft/blob/master/Customer%20Churn%20in%20World%20of%20Warcraft.ipynb)
	* [Project Report](https://github.com/SulmanK/Customer-Churn-in-World-of-Warcraft/blob/master/Customer%20Churn%20in%20World%20of%20Warcraft_Report.pdf)
	* [Dashboard](https://customer-churn-in-wow-app.herokuapp.com/)
		* Disclaimer: Due to memory constraints from Heroku API (free server), less data was used in fitting the models (17500 instead of 35000), and therefore the results will be different than the values listed in the report.  
	
* References
  * S. Qaiser and R. Ali, "Text Mining: Use of TF-IDF to Examine the Relevance of Words to Documents", International Journal of Computer Applications, vol. 181, no. 1, pp. 25-29, 2018. Available: 10.5120/ijca2018917395.

  * "Recommendation system Based On Cosine Similarity Algorithm", International Journal of Recent Trends in Engineering and Research, vol. 3, no. 9, pp. 6-10, 2017. Available: 10.23883/ijrter.2017.3423.iss9x.

  * B. Trstenjak, S. Mikac and D. Donko, "KNN with TF-IDF based Framework for Text Categorization", Procedia Engineering, vol. 69, pp. 1356-1364, 2014. Available: 10.1016/j.proeng.2014.03.129.

  * "Singular Value Decomposition", Iridl.ldeo.columbia.edu, 2020. [Online]. Available: http://iridl.ldeo.columbia.edu/dochelp/StatTutorial/SVD/index.html. [Accessed: 20- Jul- 2020].


	* P. Probst, M. Wright and A. Boulesteix, "Hyperparameters and tuning strategies for random forest", Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery, vol. 9, no. 3, 2019. Available: 10.1002/widm.1301. 

	* A. Tharwat, "Principal component analysis - a tutorial", International Journal of Applied Pattern Recognition, vol. 3, no. 3, p. 197, 2016. Available: 10.1504/ijapr.2016.079733. 

	* "Survey Report on K-Means Clustering Algorithm", International Journal of Modern Trends in Engineering & Research, vol. 4, no. 4, pp. 218-221, 2017. Available: 10.21884/ijmter.2017.4143.lgjzd. 

