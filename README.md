# FIFA 21 Dataset Cleaning and Analysis

# Overview

This script processes and cleans the FIFA 21 dataset, converting various columns into a numerical format, removing unnecessary characters, and analyzing player data. The script also generates a scatter plot visualizing the relationship between player wages and market value.

# Features

Converts height (feet/inches) and weight (lbs) into numerical values (cm and kg, respectively).

Removes newline characters from all object columns.

Converts the 'Joined' column into datetime format and calculates the number of years a player has been at a club.

Transforms monetary values (Value, Wage, Release Clause) into numerical data.

Strips 'star' characters from rating columns and converts them to numeric format.

Identifies players who have been at their club for more than 10 years.

Saves the cleaned dataset as cleaned_fifa21_data.csv.

Generates a scatter plot of Wage vs. Value and saves it as wage_vs_value_plot.png.

# Requirements

Python 3.x

Pandas

NumPy

Matplotlib

Seaborn

# Usage

Ensure the dataset (fifa21 raw data v2.csv) is placed in the datasets/ directory.

Run the script to process and clean the data.

The cleaned dataset will be saved as datasets/cleaned_fifa21_data.csv.

The scatter plot will be saved as datasets/wage_vs_value_plot.png.

Output

cleaned_fifa21_data.csv: Contains the cleaned and processed player data.

wage_vs_value_plot.png: A visualization of the relationship between player wages and market value.

# Author

This script was created to explore and clean FIFA 21 player data efficiently for better analysis.
