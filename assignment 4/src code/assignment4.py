# -*- coding: utf-8 -*-
"""assignment4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iF9RQVwBdAythspbxdoecZzpSbD7bzh3
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
diabetes = pd.read_csv("/content/diabetes.csv")

# Set seed for reproducibility
np.random.seed(123)

# Sample 25 observations
sample_data = diabetes.sample(n=25)

# Calculate mean and highest glucose values of the sample
sample_mean = sample_data['Glucose'].mean()
sample_highest = sample_data['Glucose'].max()

# Calculate mean and highest glucose values of the population
population_mean = diabetes['Glucose'].mean()
population_highest = diabetes['Glucose'].max()

# Create a DataFrame for comparison
comparison = pd.DataFrame({
    'Type': ['Sample Mean', 'Sample Highest', 'Population Mean', 'Population Highest'],
    'Glucose': [sample_mean, sample_highest, population_mean, population_highest]
})

# Save DataFrame to CSV
comparison.to_csv('glucose_comparison.csv', index=False)

# Create a bar plot for comparison
plt.figure(figsize=(8, 6))
plt.bar(comparison['Type'], comparison['Glucose'], color=['blue', 'red', 'green', 'orange'])
plt.title('Comparison of Glucose Statistics')
plt.xlabel('Type')
plt.ylabel('Glucose Value')

plt.savefig('/content/drive/MyDrive/glucose_comparison_plot.png')

plt.show()

# Calculate 98th percentile of BMI for sample and population
sample_bmi_98th = np.percentile(sample_data['BMI'], 98)
population_bmi_98th = np.percentile(diabetes['BMI'], 98)

# Create a DataFrame for comparison
comparison_bmi = pd.DataFrame({
    'Dataset': ['Sample', 'Population'],
    '98th Percentile BMI': [sample_bmi_98th, population_bmi_98th]
})

# Save DataFrame to CSV
comparison.to_csv('BMI.csv', index=False)

# Plot comparison
plt.figure(figsize=(8, 6))
plt.bar(comparison_bmi['Dataset'], comparison_bmi['98th Percentile BMI'], color=['blue', 'green'])
plt.title('Comparison of 98th Percentile BMI')
plt.ylabel('BMI Value')
plt.xlabel('Dataset')

# Save the plot as an image file
plt.savefig('/content/drive/MyDrive/98th percentile BMI.png')

plt.show()

# Set seed for reproducibility
np.random.seed(123)

# Define the number of bootstrap samples and their size
n_bootstrap_samples = 500
sample_size = 150

# Initialize lists to store bootstrap statistics
bootstrap_means = []
bootstrap_stds = []
bootstrap_percentiles = []

# Generate bootstrap samples and calculate statistics
for _ in range(n_bootstrap_samples):
    # Sample with replacement from the population
    bootstrap_sample = diabetes['BloodPressure'].sample(n=sample_size, replace=True)
    # Calculate mean, standard deviation, and percentile for the bootstrap sample
    bootstrap_means.append(bootstrap_sample.mean())
    bootstrap_stds.append(bootstrap_sample.std())
    bootstrap_percentiles.append(np.percentile(bootstrap_sample, 50))  # Median

# Calculate statistics for the population
population_mean = diabetes['BloodPressure'].mean()
population_std = diabetes['BloodPressure'].std()
population_percentile = np.percentile(diabetes['BloodPressure'], 50)  # Median

# Create DataFrame for comparison
comparison = pd.DataFrame({
    'Statistic': ['Mean', 'Standard Deviation', 'Percentile'],
    'Bootstrap': [np.mean(bootstrap_means), np.mean(bootstrap_stds), np.mean(bootstrap_percentiles)],
    'Population': [population_mean, population_std, population_percentile]
})

# Save DataFrame to CSV
comparison.to_csv('bloodpressure.csv', index=False)

# Plot comparison
plt.figure(figsize=(10, 6))

# Plot bootstrap statistics
plt.bar(np.arange(len(comparison)) - 0.2, comparison['Bootstrap'], width=0.4, color='blue', label='Bootstrap')

# Plot population statistics
plt.bar(np.arange(len(comparison)) + 0.2, comparison['Population'], width=0.4, color='green', alpha=0.5, label='Population')

plt.title('Comparison of BloodPressure Statistics (Bootstrap vs Population)')
plt.ylabel('Value')
plt.legend()
plt.xticks(np.arange(len(comparison)), comparison['Statistic'] + ' (BloodPressure)', rotation=45)
plt.tight_layout()

# Save the plot as an image file
plt.savefig('/content/drive/MyDrive/bloodpressure_statistics.png')

plt.show()