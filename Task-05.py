import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import folium
from folium.plugins import HeatMap

# Load the dataset
# df = pd.read_csv('US_Accidents_Dec21_updated.csv')
df = pd.read_csv('C:/Users/uu/Documents/GitHub/PRODIGY-INFOTECH-Task-05/sample_accident_data.csv')

# Data Preprocessing
# Convert 'Start_Time' to datetime
df['Start_Time'] = pd.to_datetime(df['Start_Time'])
df['Hour'] = df['Start_Time'].dt.hour
df['Day_of_Week'] = df['Start_Time'].dt.day_name()

# Drop rows with missing critical information
df = df.dropna(subset=['Weather_Condition', 'Road_Condition', 'Start_Time', 'End_Time'])

# Exploratory Data Analysis (EDA)

# Accident counts by road conditions
road_conditions_counts = df['Road_Condition'].value_counts()
print("Accidents by Road Condition:")
print(road_conditions_counts)

# Accident counts by weather conditions
weather_conditions_counts = df['Weather_Condition'].value_counts()
print("\nAccidents by Weather Condition:")
print(weather_conditions_counts)

# Accident counts by hour of day
hour_counts = df['Hour'].value_counts().sort_index()
print("\nAccidents by Hour of Day:")
print(hour_counts)

# Accident counts by day of the week
day_of_week_counts = df['Day_of_Week'].value_counts()
print("\nAccidents by Day of the Week:")
print(day_of_week_counts)

# Visualization

# Accidents by hour of day
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='Hour', palette='viridis')
plt.title('Accidents by Hour of Day')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Accidents')
plt.grid(True)
plt.show()

# Accidents by road condition
plt.figure(figsize=(12, 6))
sns.countplot(data=df, y='Road_Condition', palette='viridis')
plt.title('Accidents by Road Condition')
plt.xlabel('Number of Accidents')
plt.ylabel('Road Condition')
plt.grid(True)
plt.show()

# Accidents by weather condition
plt.figure(figsize=(12, 6))
sns.countplot(data=df, y='Weather_Condition', palette='viridis')
plt.title('Accidents by Weather Condition')
plt.xlabel('Number of Accidents')
plt.ylabel('Weather Condition')
plt.grid(True)
plt.show()

# Accident heatmap by location
# Ensure that the dataset includes latitude and longitude columns
if 'Latitude' in df.columns and 'Longitude' in df.columns:
    m = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=10)
    heat_data = [[row['Latitude'], row['Longitude']] for index, row in df.iterrows()]
    HeatMap(heat_data).add_to(m)
    # Save map to HTML file
    m.save('accident_heatmap.html')
    print("\nHeatmap saved to 'accident_heatmap.html'")
else:
    print("\nLatitude and Longitude columns are not available in the dataset.")

