import pandas as pd
import numpy as np
import os

os.chdir(r'C:\Users\bamla\OneDrive\Desktop\insurance-risk-analytics')

df = pd.read_csv('data/MachineLearningRating_v3.txt', sep='|', low_memory=False)

# Clean version — handle missing values and outliers
df_clean = df.copy()

# Drop columns with >50% missing
threshold = len(df) * 0.5
df_clean = df_clean.dropna(thresh=threshold, axis=1)

# Remove negative premiums and claims
df_clean = df_clean[df_clean['TotalPremium'] >= 0]
df_clean = df_clean[df_clean['TotalClaims'] >= 0]

# Add derived columns
df_clean['LossRatio'] = df_clean['TotalClaims'] / df_clean['TotalPremium'].replace(0, np.nan)
df_clean['Margin'] = df_clean['TotalPremium'] - df_clean['TotalClaims']

# Save cleaned version
df_clean.to_csv('data/insurance_data_clean.csv', index=False)
print(f"Clean data saved: {df_clean.shape}")