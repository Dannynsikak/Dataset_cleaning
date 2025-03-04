import pandas as pd
import numpy as np
import re

# load the dataset
file_path = "/datasets/fifa21_raw_data.csv"
df = pd.read_csv(file_path)

# display basic info and first few rows to understand the structure
df.info(), df.head()

