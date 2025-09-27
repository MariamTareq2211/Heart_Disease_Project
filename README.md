# 🫀 Heart Disease Prediction Project

This project uses **Machine Learning** techniques to analyze the UCI Heart Disease dataset and predict the presence of heart disease.  
It includes **data preprocessing, feature selection, supervised learning, clustering, hyperparameter tuning, and model export**.

---


# 🚀 Workflow
1. Data Preprocessing & Cleaning

Handles missing values

One-hot encodes categorical variables

Scales numeric features

Performs exploratory data analysis (EDA)

📓 Notebook: 01_data_preprocessing.ipynb

2. Dimensionality Reduction (PCA)

Reduces dataset dimensionality

Visualizes variance explained by components

📓 Notebook: 02_pca.ipynb

3. Feature Selection

Random Forest feature importance

Recursive Feature Elimination (RFE)

Chi-Square test

Saves reduced dataset

📓 Notebook: 03_feature_selection.ipynb

4. Supervised Learning

Models: Logistic Regression, Decision Tree, Random Forest, SVM

Evaluation: Accuracy, Precision, Recall, F1, ROC AUC

Visualizes performance

📓 Notebook: 04_supervised_learning.ipynb

5. Unsupervised Learning (Clustering)

K-Means clustering with Elbow method

Hierarchical clustering (dendrogram)

Compares clusters with actual labels

📓 Notebook: 05_clustering.ipynb

6. Hyperparameter Tuning

Uses GridSearchCV and RandomizedSearchCV

Tunes all supervised models

Auto-selects the best model (based on ROC AUC)

Saves model name → models/best_model_name.txt

📓 Notebook: 06_hyperparam_tuning.ipynb

7. Model Export & Deployment

Builds final pipeline (scaler + best model)

Trains on data

Saves final model → models/final_model.pkl

Saves evaluation metrics → results/evaluation_metrics.txt

📓 Notebook: 07_model_export.ipynb

# 📊 Results

The pipeline identifies the best-performing model for predicting heart disease.

Metrics (Precision, Recall, F1, ROC AUC) are saved in:

results/evaluation_metrics.txt

💡 How to Use the Model

Load the exported model (final_model.pkl) in Python:

import joblib

# Load model
model = joblib.load("models/final_model.pkl")

# Example prediction
sample = [[63, 145, 233, 1, 0, 150, 0, 2.3, 0, 0, 1]]  # Replace with real feature values
prediction = model.predict(sample)
print("Prediction:", "Heart Disease" if prediction[0] == 1 else "No Heart Disease")

#📌 Requirements

See requirements.txt
:

pandas
numpy
matplotlib
seaborn
scikit-learn
scipy
joblib
