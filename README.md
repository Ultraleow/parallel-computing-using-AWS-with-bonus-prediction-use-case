# WQD7008 Parallel and Distributed Computing Project 
## Project Title  
Deploy an API management platform on AWS for Stem salary processing
## Team Members
## 1.Introduction
Our project is to meet users' needs for salary information, and we use the API management platform on AWS to process Stem salary information. Using AWS's cloud computing technology, we are able to process payroll information quickly and efficiently.
## 2.The objective of the project
+	Meet users' needs by using the API management platform on AWS to process payroll information quickly and efficiently.
+	Use the delivery ability of email to send the result of salary processing to the user, so that the user can obtain information conveniently.
+ Use stable and reliable cloud computing technology to ensure the stability of project operation.
## 3.Scenario
Projects deploying an API management platform on AWS to support STEM payroll processing can be used in many different scenarios:
+ Provide salary information service on the website or mobile application: You can provide salary information through the API interface for users to view on the website or mobile application.
+	Provide salary information service within the enterprise: You can provide the API interface to the personnel within the enterprise to facilitate them to view their salary information.
+	Integrate salary information into other systems: You can use the API interface to import salary information into other systems, such as financial management systems or human resource management systems.
## 2. Previous case study
### 5.Methodology
![1673025932367](https://user-images.githubusercontent.com/102680739/211156266-cbecc503-5268-4194-9303-2bbf4021eee5.png)
![image](https://user-images.githubusercontent.com/102680739/211156273-aa60eeff-eb61-4d95-be0f-669f892bd618.png)
### 5.1 Dataset Collected
This dataset was obtained from Kaggle：https://www.kaggle.com/datasets/jackogozaly/data-science-and-stem-salaries

which was originally scraped from levels.fyi with some additional cleaning. This dataset contains 29 attributes with over 60,000 of records, focusing on the salaries of employees in a variety of technological companies. Below are the descriptions of the attributes contained within the dataset.

Figure 2: Description of the attributes contained in the dataset.
![image](https://user-images.githubusercontent.com/102680739/211156539-639d6dcb-6b58-44b0-b5a3-2b028faa866f.png)
### 5.2 Data Preprocessing
The dataset contained a lot of noisy data and further pre-processing was needed. We used the following Python modules for our data cleaning:

+	Pandas
+	NumPy
+	Scikit-Learn

Step 1: Remove Null Values

Delete records with null values in important attributes in the dataset. This reduces the number of records from 60,000 to approximately 21,000.

Step 2: Remove unnecessary attributes

We removed columns that were not helpful for salary prediction. Below are the columns we removed based on our initial understanding of the dataset and the rationale behind the removal.

Step 3: Standardize the company name

There is a material inconsistency in the company name. For example, Google can have many variations such as "google", "Google Inc", "GOOGLE", etc. We normalize their names to avoid duplicate categories in attributes.

Step 4: Preprocess the "location" attribute

The values in the attribute contain city, state, and country, but they are separated by commas, which makes them a string data type. We separated them and created additional attributes for our dataset.

Step 5: Labels Encoding Categorical Attributes for Modeling

We convert these categorical attributes that will be used for modeling into numerical attributes in order to fit them to our machine learning model. Especially for the categorical attribute "company", we label the top 89 companies according to market capitalization, and those companies that are not among these 89 companies are labeled as "89", similar to the "other" category, because the dataset contains hundreds of company.

![image](https://user-images.githubusercontent.com/102680739/211156739-cbc98886-19f4-4d95-9ec1-0752eeccd772.png)

### 5.3 Training + Validation

At this stage, we trained three different machine learning algorithms for our dataset using Python 3. Since our goal is to predict salary (continuous data), only regression algorithms like Multiple Linear Regression (MLR), Random Forest, and K Nearest Neighbors (KNN) were chosen.

When selecting the best model, we will use cross-validation. Divide the training data into several disjoint subsets, each time use one subset as the validation set, and the remaining subsets as the training set, train multiple models, and evaluate the model performance on the validation set. Finally, choose the model that performs best on the validation set among all models.

Why use cross-validation?

+ It can effectively solve the problem of poor model generalization ability caused by unbalanced data division.
+ It can effectively evaluate the generalization ability of the model, that is, the performance of the model on unknown data.
+ The stability and reliability of the model can be improved.

