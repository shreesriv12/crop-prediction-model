# Crop Recommendation System

## Overview
The Crop Recommendation System is a machine learning-based web application that predicts the most suitable crop for cultivation based on historical data and environmental parameters. It also provides insights into required fertilizers, seeds, market prices, and estimated yield.

## Features
- Predicts the most suitable crop based on soil characteristics, weather conditions, and historical data.
- Provides information on necessary fertilizers, seed requirements, and market prices for the recommended crop.
- Estimates the potential yield in quintals per acre.
- User-friendly web application for easy input of local parameters and accessing recommendations.
- Integration with real-time weather data for accurate predictions.

## Technology Used
- **Python**: Core programming language.
- **Machine Learning (scikit-learn)**: Model training and predictions.
- **Flask**: Backend framework for web application.
- **HTML/CSS/JavaScript**: Frontend development for user interface.![Screenshot 2025-03-29 175721](https://github.com/user-attachments/assets/d6c0cdef-a36a-4b76-9dd6-c1186f7a546c)


## Usage
1. Enter the required parameters such as soil characteristics, weather conditions, and other relevant details.
2. Click on the "Predict" button.
3. Receive the recommended crop.

## Installation
### Prerequisites
- Python 3.12.9
- pip (Python package manager)

### Steps
1. Clone the repository:
   ```bash
   git clone (https://github.com/shreesriv12/crop-prediction-model.git)
   cd crop-recommendation
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python app.py
   ```
4. Open your browser and go to `http://127.0.0.1:5000/` to use the web application.

## Model Training
If you want to retrain the machine learning model:
1. Prepare your dataset in CSV format.
2. Run the training script:
   ```bash
   python3 model.py
   ```
3. The updated model will be saved and used for future predictions.



