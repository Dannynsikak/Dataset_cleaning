import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import seaborn as sns

# load the dataset
file_path = "datasets/fifa21 raw data v2.csv"
df = pd.read_csv(file_path)

# display basic info and first few rows to understand the structure
df.info(), df.head()

# convert Height to numerical values (convert feet/inches to cm)
# Function to convert height to cm
def convert_height(height):
    match = re.match(r"(\d+)'(\d+)", height)
    if match:
        feet = int(match.group(1))
        inches = int(match.group(2))
        return feet * 30.48 + inches * 2.54
    return None

# Function to convert weight to kg
def convert_weight(weight):
    match = re.match(r"(\d+)lbs", weight)
    if match:
        return int(match.group(1)) * 0.453592  # Convert lbs to kg
    return None

# Convert height and weight columns
df["Height"] = df["Height"].apply(convert_height)
df["Weight"] = df["Weight"].apply(convert_weight)

# Remove newline characters from all object columns
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Convert 'Joined' column to datetime format
df["Joined"] = pd.to_datetime(df["Joined"], errors="coerce")

# Identify players who have been at the club for more than 10 years
df["Years_at_Club"] = (pd.Timestamp("today") - df["Joined"]).dt.days / 365
long_term_players = df[df["Years_at_Club"] > 10][["Name", "Club", "Years_at_Club"]]

# Function to convert currency strings to numeric values
def convert_currency(value):
    if isinstance(value, str):
        value = value.replace("€", "").replace("K", "e3").replace("M", "e6").replace("B", "e9")
        try:
            return float(eval(value))  # Safely evaluate the string as a numeric expression
        except:
            return None
    return None

# Convert 'Value', 'Wage', and 'Release Clause' columns
for col in ["Value", "Wage", "Release Clause"]:
    df[col] = df[col].apply(convert_currency)

# Remove 'star' characters from rating columns and convert to numeric
for col in ["W/F", "SM", "IR"]:
    df[col] = df[col].str.replace("★", "").astype(float)

# Display cleaned dataset info and check long-term players
df.info(), long_term_players.head()

# Filter out rows with missing values in 'Value' and 'Wage'
df_filtered = df.dropna(subset=["Value", "Wage"])

# Save the cleaned dataset
cleaned_file_path = "datasets/cleaned_fifa21_data.csv"
df.to_csv(cleaned_file_path, index=False)

# Scatter plot of Wage vs. Value
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df_filtered["Wage"], y=df_filtered["Value"], alpha=0.5)

plt.xlabel("Wage (€)")
plt.ylabel("Value (€)")
plt.title("Scatter Plot of Wage vs. Value")
plt.xscale("log")  # Log scale for better visibility
plt.yscale("log")

# Save the plotted graph as a PNG file
plot_file_path = "datasets/wage_vs_value_plot.png"
plt.savefig(plot_file_path)

plt.show()