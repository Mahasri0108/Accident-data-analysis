# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 10:43:06 2025

@author: Lenovo
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# File path to dataset
file_path = r"C:\Users\Lenovo\Downloads\archive (1)\US_Accidents_March23.csv"

# Read first few rows to check actual column names
df_sample = pd.read_csv(file_path, nrows=5)
actual_columns = df_sample.columns.str.strip().str.lower()
print("Checking dataset columns...")
print("Actual columns:", list(actual_columns))

# Define correct column names based on the dataset
columns_needed = {'start_time': 'Start_Time', 'start_lat': 'Start_Lat', 'start_lng': 'Start_Lng'}

# ---- Step 1: Read CSV File in Chunks (Memory Efficient) ----
chunk_size = 100000  # Load 100,000 rows at a time
df_list = []

# Read dataset in chunks
for chunk in pd.read_csv(file_path, usecols=columns_needed.values(), chunksize=chunk_size):
    chunk = chunk.rename(columns={v: k for k, v in columns_needed.items()})
    chunk['start_time'] = pd.to_datetime(chunk['start_time'], errors='coerce')
    chunk['hour'] = chunk['start_time'].dt.hour
    chunk['start_lat'] = chunk['start_lat'].astype('float32')
    chunk['start_lng'] = chunk['start_lng'].astype('float32')
    df_list.append(chunk)

# Combine first 5 chunks for analysis
df = pd.concat(df_list[:5])

# ---- Step 2: Exploratory Data Analysis ----

## **Accidents by Time of Day**
plt.figure(figsize=(10, 5))
sns.countplot(x=df['hour'], palette="coolwarm")
plt.xlabel("Hour of the Day")
plt.ylabel("Number of Accidents")
plt.title("Accidents by Time of Day")
plt.show()

## **Accident Hotspots (Latitude & Longitude)**
df_geo = df[['start_lat', 'start_lng']].dropna()

plt.figure(figsize=(10, 7))
plt.scatter(df_geo['start_lng'], df_geo['start_lat'], alpha=0.5, c='red', s=10)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Accident Hotspots")
plt.grid(True)
plt.show()