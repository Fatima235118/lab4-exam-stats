import pandas as pd
import numpy as np
from scipy import stats

# --------------------------------
# Task 1: Exam Statistics
# --------------------------------

# Exam scores of 10 students
scores = pd.Series([
    72, 65, 88, np.nan, 54,
    91, 76, np.nan, 83, 69
])

print("Original Scores:")
print(scores)

# --------------------------------
# 1. Descriptive Statistics
# --------------------------------

print("\nDescriptive Statistics:")
print(scores.describe())

# --------------------------------
# 2. Skewness and Kurtosis
# --------------------------------

clean_scores = scores.dropna()

print("\nSkewness:", stats.skew(clean_scores))
print("Kurtosis:", stats.kurtosis(clean_scores))

# --------------------------------
# 3. Detect Missing Values
# --------------------------------

print("\nMissing values:", scores.isnull().sum())

# --------------------------------
# 4. Fill Missing Values with Mean
# --------------------------------

scores_filled = scores.fillna(scores.mean())

print("\nFilled Scores:")
print(scores_filled)