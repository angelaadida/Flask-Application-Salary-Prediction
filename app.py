import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# Initialize Flask application
application = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

# Home route
@application.route('/')
def home():
    return render_template('index.html')

# Predict route
@application.route('/predict', methods=['POST'])
def predict():
    # Extract input features from form
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    # Format the prediction output
    output = round(prediction[0], 2)
    return render_template('index.html', prediction_text=f"Employee salary should be $ {output}")

# Main entry point
if __name__ == "__main__":
    application.run(debug=True)

