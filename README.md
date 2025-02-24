# Breast Cancer Dataset - Exploratory Data Analysis (EDA)

## Project Portfolio - Breast Cancer Prediction

This project focuses on **Exploratory Data Analysis (EDA)** and **Machine Learning Modeling** using the **Breast Cancer Dataset**. The dataset is sourced from **UCI Machine Learning Repository** and contains diagnostic information about breast cancer tumors.

Breast cancer is one of the most common types of cancer affecting women worldwide. Early detection through accurate diagnosis plays a crucial role in increasing survival rates. This dataset consists of various **biopsy features** used to classify tumors as either **malignant** or **benign**.

**Dataset Source:**\
[Breast Cancer Wisconsin]([https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html])

---

## Goals:

1. Perform EDA to understand the distribution of features in the dataset.
2. Identify key patterns and correlations between tumor characteristics.
3. Develop Machine Learning models to classify tumors as **malignant** or **benign**.
4. Optimize model performance using **Hyperparameter Tuning**.
5. Evaluate the model using key performance metrics such as **accuracy, precision, recall, and F1-score**.
6. Analyze the importance of features in predicting breast cancer.

---

## Dataset Overview:

- The dataset contains **569 instances** and **30 numeric features** extracted from digitized images of breast mass biopsies.
- The target variable is **diagnosis**:
  - **M (Malignant)** - Cancerous tumors
  - **B (Benign)** - Non-cancerous tumors
- Key features include:
  - **Radius, Texture, Perimeter, Area, Smoothness, Compactness, Concavity, Symmetry**, etc.
  - Each feature is calculated for the mean, standard error, and worst case.

---

## Insights:

1. **Malignant tumors tend to have larger values for radius, perimeter, and area compared to benign tumors.**
2. **There is a strong correlation between some features, such as radius, perimeter, and area.**
3. **Feature Importance analysis shows that texture, concavity, and symmetry play significant roles in classification.**
4. **Hyperparameter tuning improves model accuracy and balances performance across different classes.**

---

## Machine Learning Implementation:

- Applied classification models:
  - **Random Forest Classifier**
  - **Support Vector Machine (SVM)**
  - **Gradient Boosting Classifier**
- **Hyperparameter tuning** was performed using **GridSearchCV**.
- **Evaluation metrics**: Precision, Recall, F1-score, and Confusion Matrix.
- Feature Importance visualization helps understand the most influential predictors.

---

## Key Findings & Recommendations:

1. **Early detection models can be improved with better feature selection and hyperparameter tuning.**
2. **Using feature scaling and balancing techniques (SMOTE) enhances model performance.**
3. **Visualizing feature importance aids in understanding which tumor characteristics are most relevant for classification.**
4. **Integrating deep learning methods could further enhance predictive accuracy.**

---

### Contact & Feedback:

If you have any suggestions or feedback, feel free to connect with me on LinkedIn or via email:

- **Email**: [wiryawansujana@gmail.com](mailto\:wiryawansujana@gmail.com)
- **LinkedIn**: https\://www\.linkedin.com/in/rajendra-artanto-4698a8306/

\#MachineLearning #BreastCancer #EDA #DataScience

