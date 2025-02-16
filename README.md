Project Overview

    This project builds a Linear Regression Model using Scikit-Learn to predict salaries based on experience, test scores, and interview performance. The trained model is saved and loaded using Pickle for future predictions.
    

  1. Libraries Used
     
    numpy: Supports numerical operations.
    
    matplotlib.pyplot: Used for visualization (not used in this code but useful for plotting results).
    
    pandas: Loads and manipulates the dataset.
    
    pickle: Saves and loads the trained machine learning model.
    
    sklearn.linear_model.LinearRegression: Implements Linear Regression for salary prediction.



2. Dataset – Hiring Data (hiring.csv)
   
    The dataset contains three features:
   
    Years of Experience
   
    Test Score
   
    Interview Score
   
    The target variable (output) is Salary.



3. Loading the Dataset

   Reads the dataset from hiring.csv into a Pandas DataFrame.

   

4. Defining Features and Target Variables
   
    Features (X): Independent variables used to predict the salary.
   
    Target (Y): Dependent variable (salary).
   

5. Training the Linear Regression Model
   
    LinearRegression() creates a Linear Regression model.


      
6. Saving the Trained Model Using Pickle
   
    Serializes the trained model and saves it as model.pkl.



7. Loading the Model for Future Predictions
   
    Loads the saved model from the disk.



8. Making Predictions (Example Usage)
   
    Converts input data into a NumPy array.
   
    Uses model.predict() to predict the salary.


Summary:

    Load the dataset from hiring.csv.
    
    Define features (experience, test score, interview score) and target (salary).
    
    Train a Linear Regression Model using Scikit-Learn.
    
    Save the trained model using Pickle (model.pkl).
    
    Load the saved model and make predictions.

