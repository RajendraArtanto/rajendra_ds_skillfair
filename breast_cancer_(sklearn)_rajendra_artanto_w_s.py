# -*- coding: utf-8 -*-
"""Breast Cancer (SKLearn) - Rajendra Artanto W.S.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lLWe0v1bkYZxR9RLc1sO5o0_WIl5l4hU

# Breast Cancer (Scikit-learn Dataset)

Oleh : Rajendra Artanto Wiryawan Sujana

"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, auc
from imblearn.over_sampling import SMOTE

breast_cancer = datasets.load_breast_cancer()
X = breast_cancer.data
y = breast_cancer.target

df_X = pd.DataFrame(X, columns=breast_cancer.feature_names)
df_y = pd.Series(y, name='target')

df = pd.concat([df_X, df_y], axis=1)

import warnings
warnings.filterwarnings("ignore")

plt.figure(figsize=(6, 4))
sns.countplot(x="target", data=df, palette="pastel")
plt.title("Distribusi Kelas Target Sebelum SMOTE")
plt.xticks(ticks=[0, 1], labels=breast_cancer.target_names)
plt.show()

class_distribution = df_y.value_counts(normalize=True) * 100
print(class_distribution)

plt.figure(figsize=(12, 6))
sns.heatmap(df.corr(), cmap="coolwarm", linewidths=0.5)
plt.title("Korelasi Antar Fitur")
plt.show()

smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(df_X, df_y)

plt.figure(figsize=(6, 4))
sns.countplot(x=y_resampled, palette="pastel")
plt.title("Distribusi Kelas Target Setelah SMOTE")
plt.xticks(ticks=[0, 1], labels=breast_cancer.target_names)
plt.show()

class_distribution = y_resampled.value_counts(normalize=True) * 100
print(class_distribution)

X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.2, random_state=42)

param_grid = {
    'n_estimators': [50, 100, 150],
    'learning_rate': [0.01, 0.1, 0.2],
    'max_depth': [3, 4, 5]
}

gbc = GradientBoostingClassifier()
grid_search = GridSearchCV(gbc, param_grid, cv=5, scoring='accuracy', n_jobs=-1)
grid_search.fit(X_train, y_train)

best_gbc = grid_search.best_estimator_
y_pred = best_gbc.predict(X_test)

print("\n=== Classification Report ===")
print(classification_report(y_test, y_pred, target_names=breast_cancer.target_names))

from sklearn.metrics import classification_report

report = classification_report(y_test, y_pred, output_dict=True)

formatted_report = {}

for key, value in report.items():
    if isinstance(value, dict): 
        formatted_report[key] = {
            metric: f"{value[metric] * 100:.2f}%" if metric != "support" else f"{value[metric]:.0f}"
            for metric in value
        }
    else: 
        formatted_report[key] = f"{value * 100:.2f}%"

for key, value in formatted_report.items():
    if isinstance(value, dict):
        print(f"\nClass {key}:")
        for metric, score in value.items():
            print(f"  {metric.capitalize()}: {score}")
    else:
        print(f"\nClass accuracy:\n  Accuracy: {value}")

cf_matrix = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 4))
sns.heatmap(cf_matrix, annot=True, fmt='d', cmap="Blues",
            xticklabels=breast_cancer.target_names,
            yticklabels=breast_cancer.target_names)
plt.xlabel("Prediksi")
plt.ylabel("Aktual")
plt.title("Matriks Konfusi Gradient Boosting")
plt.show()

feature_importance = pd.Series(best_gbc.feature_importances_, index=df_X.columns).sort_values(ascending=False)
plt.figure(figsize=(10, 6))
sns.barplot(x=feature_importance.values, y=feature_importance.index, palette="viridis")
plt.xlabel("Importance Score")
plt.ylabel("Feature")
plt.title("Feature Importance - Gradient Boosting")
plt.show()
