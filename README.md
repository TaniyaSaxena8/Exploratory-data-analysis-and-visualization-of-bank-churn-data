# Bank-Customers-Churn-Data-Analysis
**OBJECTIVE:**
---

The project aims to help the bank understand customer churn behavior better and make data-driven decisions to improve customer retention, leading to increased customer satisfaction and long-term profitability.

The main goals of the project are as follows:

**1.	Exploratory Data Analysis (EDA):**

Understand the overall structure of the dataset and its key features.

Explore the distribution of churned and non-churned customers.

Identify patterns, trends, and correlations between various customer attributes and churn.

**2.	Identify Factors Influencing Churn:**
   
Determine the most critical factors that contribute to customer churn.

Analyze the relationship between customer churn and attributes like account balance, credit score, age, gender, etc.

**3.	Data Visualization in Power BI:**

Present the findings of the EDA in an interactive and visually appealing manner.

Design informative and insightful dashboards and visualizations to communicate complex patterns effectively.



**DATASET:**
---
The dataset was taken from Kaggle. There are a total of 10,000 customer data from Germany, Spain, and France. 

Dataset Link: 

DatasetThe dataset was cleaned and transformed using power query in PowerBI.



**EXPLORATORY DATA ANALYSIS:**
---
1.	Use Python and popular libraries like Pandas, NumPy, and Matplotlib/Seaborn to perform exploratory data analysis.
   
2.	Explore the data distribution, missing values, and outliers.
   
3.	Generate descriptive statistics, such as mean, median, and standard deviation, for key features related to churn.
   
4.	Create visualizations like histograms, box plots, and scatter plots to gain insights into different aspects of the data.
   
5.	Values count of customers based on different features of the dataset:

   ![image](https://github.com/TaniyaSaxena8/Data-Analysis-of-Bank-Churn-Data/assets/135128191/98e83efa-544d-4325-bd93-e8152000df47)

6. Analyzed trends and patterns of customer based on their Age, Account Balance, Credit Score, and Expected salary using histogram:

   ![image](https://github.com/TaniyaSaxena8/Data-Analysis-of-Bank-Churn-Data/assets/135128191/1567a47b-3174-477a-b73e-48e9360664de)

7. Analyzing what factors influencing churn rate:

   (i.) Categorical variables:

   ![image](https://github.com/TaniyaSaxena8/Data-Analysis-of-Bank-Churn-Data/assets/135128191/87670af3-6df8-4e0d-a57a-818fb101c077)
   ![image](https://github.com/TaniyaSaxena8/Data-Analysis-of-Bank-Churn-Data/assets/135128191/60821001-95ff-4e9c-a51a-d9102ac35f2c)
   ![image](https://github.com/TaniyaSaxena8/Data-Analysis-of-Bank-Churn-Data/assets/135128191/23c6468d-d2dd-4eba-a8e0-543b4432a1d4)

   (ii.) Continuous variable:

   ![image](https://github.com/TaniyaSaxena8/Data-Analysis-of-Bank-Churn-Data/assets/135128191/02b44071-a481-4e45-a261-97e6a0a534b9)
   ![image](https://github.com/TaniyaSaxena8/Data-Analysis-of-Bank-Churn-Data/assets/135128191/b58e858c-dc95-4f91-8684-6fe44d665ca5)


**DATA VISUALIZATION USING PowerBI:**
---
1.	Data Model:
   
   ![image](https://github.com/TaniyaSaxena8/Data-Analysis-of-Bank-Churn-Data/assets/135128191/e6778bca-8110-4c58-8b04-a9bccf95f4f9)


2. Dashboard:
   
 ![image](https://github.com/TaniyaSaxena8/Data-Analysis-of-Bank-Churn-Data/assets/135128191/11c07e05-be4a-4b43-aff7-ade6ea7237fd)


**KEY INSIGHTS:** 
  ---
1.	Out of 3 countries, Germany has the highest churn rate (32.4%).
   
2.	The overall churn rate is 20.4%. The churn rate for males is 16.5% and for females is 25.1% which indicates that females are more likely to churn than males.
   
3.	Customers with <=400 credit score having a 100% churning rate, whereas customers with >400 credit score have an average churning rate is about 20%, this shows that above 400, a change in credit score does not cause any significant effect on churn rate.
   
4.	People in the <20-40 age group is having an average churn rate of 8.44% and the 41-80 age group is having average churn rate of 40.54%.
   
5.	Churn rate of 0 account balance customers is 13.8%, 100% for 1K-10K account balance customers and >25% for 10K-200K account balance customers.






