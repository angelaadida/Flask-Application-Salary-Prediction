import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression

# Load dataset
dataset = pd.read_csv('hiring.csv')

# Define features and target
x = dataset.iloc[:, :3]
y = dataset.iloc[:, -1]

# Train model
regressor = LinearRegression()
regressor.fit(x, y)

# Save the model to disk
pickle.dump(regressor, open('model.pkl', 'wb'))

# Load the model from disk
model = pickle.load(open('model.pkl', 'rb'))

