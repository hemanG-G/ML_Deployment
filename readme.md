# Student Performance Predication

### Information About the Dataset:

**The dataset** The goal of this project is to understand the influence of the parents background, test preparation, and various other variables on the students math score.

## Life cycle of Machine learning Project
### Understanding the Problem Statement
1. Data Collection
2. Data Checks to perform
3. Exploratory data analysis
4. Data Pre-Processing
5. Model Training
6. Choose best model



There are 8 independent variables:

- `gender` : Sex of a student (Male/Female)
- `race/ethnicity` : Ethnicity of a student (Group A,B,C,D,E)
- `parental level of education` : parents' final education (bachelor's degree,some college,master's degree,associate's degree,high school)
- `lunch` : What type of lunch the student had before test (standard or free/reduced)
- `test preparation course` : Whether the student completed any preparation course before the test.
- `reading score` : Reading score obtained by the student.
- `writing score` : Writing score obtained by the student.

Target variable:

- `math score`: Math score of a student.

Dataset Source Link :
[https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?resource=download](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?resource=download)

#UI
![image](https://github.com/user-attachments/assets/4f9a38b9-af55-4193-9106-e21bfb8fdefb)


# Project Development Approach

1. Data Ingestion :

   - In Data Ingestion phase the data is first read as csv.
   - Then the data is split into training and testing and saved as csv file.

2. Data Transformation :

   - In this phase a ColumnTransformer Pipeline is created.
   - for Numeric Variables first SimpleImputer is applied with strategy median (because there were some outliers in the data), then standard scaling is performed on numeric data.
   - for Categorical Variables SimpleImputer is applied with most frequent strategy, then one-hot-encoding is performed, after this data is scaled with standard scaler.
   - This preprocessor is saved as pkl file inside the artifacts folder.

3. Model Training :

   - In this phase, all the models are trained and evaluated. The best model found was Linear Regression.
   - After this hyperparameter tuning is also performed prior to selecting the best model.
   - This model is saved as pickle file to be used for the predict pipeline.

4. Prediction Pipeline :
   - This pipeline converts given data into dataframe and has various functions to load pickle files and predict the final results in python.

5. Flask App creation :
   - Flask app is created with User Interface to predict the math score of a student given the required features inside a Web Application.

# Exploratory Data Analysis Notebook

Link : [EDA Notebook](./notebook/1.EDASTUDENTPERFORMANCE.ipynb)

# Model Training Approach Notebook

Link : [Model Training Notebook](./notebook/2.MODELTRAINING.ipynb)

# Usage:

1. conda create -p std python=3.8 -y
2. conda activate std/
3. pip install -r requirements.txt
4. Execute app.py
5. Access http://127.0.0.1:5000/


## For Deployment: (AWS Elastic Beanstalk) (step by step)
make: make a folder: .ebextension>python.config>
~~~
option_settings:
  "aws:elasticbeanstalk:container:python":
    WSGIPath: application:application
 ~~~
 make a folder then application.py> copy full code of app.py
 Then push it on Github
    
1. open aws then sign in
2. Search for Elastic Beanstalk open application icon
3. create application
4. application name: , platform = python
5. click on sample application then create application
6. search on aws, "codepipeline", click on CodePipeline, create pipeline, pipeline name: , click next
7. source provider: Github (version 1), click connect to the Github, confirm it
8. select repository name, branch: main, Github webhooks, click next
9. Build Provider: Skip
10. Deploy provider: AWS Elastic Beanstalk, region, application name, environment name, next
11. Review: create pipeline
12. if error occurs: delete app.py file
13. Deployment Success.


## For Deployment: (Azure)
1. open azure, sign-in, create the resource
2. create Web App, subscription name:, resource group:, name:, publish: code, runtiome: python 3.8, next
3. continuous deployment: enable, configure with your github account, organisation: github username, repository: repo name, branch: main, review+create, create
4. wait then reload github project page.
5. .github/workflows will be created on your repository, click on it
6. .yaml fill would be created
7. go to github actions, add or update azure....
8. Deployment Completed.
