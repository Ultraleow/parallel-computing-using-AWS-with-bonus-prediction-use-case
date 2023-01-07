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
## 5.Methodology
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

The best model puts on an NFS filesystem and will use Python's os library to read and write files.

First, NFS mount on your machine. Then, use the os.listdir() function to get a list of files in the NFS directory, and use the os.path.join() function to concatenate the filenames with the NFS path.

+ Use the Amazon EC2 service to create a virtual machine instance to run the API management platform.
+ Create a database using the Amazon RDS service to store data related to payroll processing.
+ Install the required systems and software on the virtual machine instance, including the operating system, database management system, API management platform, etc.
+ Install the required systems and software on the virtual machine instance, including the operating system, database management system, API management platform, etc.
+ Deploy the API management platform on the virtual machine instance and connect to the database.
+ Use the Amazon API Gateway service to build an API gateway, and connect the API gateway to the API management platform on the virtual machine instance.
+ Build user pools using the Amazon Cognito service to manage user authentication and authorization.
+ Build a messaging service using the Amazon SNS service to send notifications about payroll processing.
+ Build object storage using the Amazon S3 service to store files related to payroll processing.

The result of the API request is displayed in the UI：

## 6.Description of all components involved in the project
+ API (Application Programming Interface): API is the interface of application programs and a specification for communication between software systems. An API usually + consists of a set of functions, methods, or interfaces that allow a program to access the functionality and data of another program.
+ Flask: Flask is a lightweight Python web framework that can quickly build web applications. Flask provides a simple templating system and routing mechanism that can + help developers quickly build web applications.
+ Nginx: Nginx is a high-performance HTTP server, often used as a reverse proxy server, load balancer and HTTP cache. Nginx can handle high concurrent requests and + works with various web application frameworks like Flask.
+ Python: for data cleaning and model processing.
+ Testing: Used to select the best model.
+ NFS file system: used to store models.
+ RDS MSSQL database: used to store and manage data.
+ AWS cloud service: used to deploy API management platform and provide email service.
+ UI interface: used to display the processing results.

## 7.Results, discussion 
+ Advantages of the project
Payroll information can be processed quickly and efficiently by using AWS's cloud computing technology and API management platform. Using the AWS email service, the processing results can be easily sent to users. These advantages enable our project to meet the needs of users and ensure the stability and reliability of the project.
+ project deficiencies
Although our project has many advantages, there are still some shortcomings. For example, our system currently only handles Stem salary information, if we want to expand to other industries, it may require more development work. Additionally, our system currently only handles payroll information and may need to be extended if we want to provide more functionality.
+ Project direction
To further develop our project, we can consider the following directions:

Expand the functions of the system: We can consider providing more functions in addition to the original salary information processing functions, such as social security, provident fund, etc., so that our system can better meet the needs of users.

Expand the coverage of the system: We can consider expanding our system to other industries, such as education, medical care, etc., so that our system can more widely meet the needs of users.

Look for more cooperation opportunities: We can consider cooperating with more companies to provide them with salary information processing services. In this way, our system can gain more users, and at the same time bring us more benefits.

## 8.Conclusion
"By deploying an API management platform on AWS, we can process salary information of Stem companies more conveniently. We can use API to request salary information and use AWS Simple Email Service (SES) to send processing results to users. In this way, we It can provide salary information to users faster, process salary information quickly and efficiently, and meet user needs.

We have deployed an API management platform on AWS, and used AWS's cloud computing technology and email service to process Stem salary information. Our system has been able to accept user requests and return salary information using our API interface. At the same time, we are constantly improving our system to make the processing faster, more stable, and provide a better user experience.

## 9.future outlook
In the future, we hope to expand our system further to handle more payroll information and provide richer functionality. We also hope to cooperate with more companies to provide better salary information services.

## 10.	References
1.	AWS Case Studies：https://aws.amazon.com/cn/solutions/case-studies/
2.	API Management Case Studies：https://www.akamai.com/us/en/solutions/api-management/case-studies.jsp
3.	Mulesoft Case Studies：https://www.mulesoft.com/customers/case-studies
4.	WSO2 Case Studies：https://wso2.com/customers/case-studies/

