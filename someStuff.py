# Import pandas library
import pandas as pd

# Create a data frame with your data
df = pd.DataFrame({"Time": ["23:15.0"], "others": ["others"], "BE": ["BE"], "Test": ["Test"], "Low": ["Low"], "6": [6], "5": [5]})

# Define a function to convert time values to numerical values
def time_to_num(time):
  # Split the time string by colon
  hour, minute = time.split(":")
  # Convert the hour and minute to integers
  hour = int(hour)
  minute = int(minute)
  # Return the total number of minutes
  return hour * 60 + minute

# Apply the time_to_num function to the Time column
df["Time"] = df["Time"].apply(time_to_num)

# Define a function to convert ordinal values to numerical values
def ordinal_to_num(ordinal):
  # Define a dictionary that maps ordinal values to numerical values
  ordinal_dict = {"Low": 0, "Medium": 0.5, "High": 1}
  # Return the corresponding numerical value
  return ordinal_dict[ordinal]

# Apply the ordinal_to_num function to the Low column
df["Low"] = df["Low"].apply(ordinal_to_num)

# Define a function to perform min-max scaling on numerical columns
def min_max_scale(col):
  # Get the minimum and maximum values of the column
  min_val = col.min()
  max_val = col.max()
  # Return the scaled column
  return (col - min_val) / (max_val - min_val)

# Apply the min_max_scale function to the Time, 6, and 5 columns
df[["Time", "6", "5"]] = df[["Time", "6", "5"]].apply(min_max_scale)

# Define a function to perform one-hot encoding on categorical and nominal columns
def one_hot_encode(col):
  # Get the unique values of the column
  unique_vals = col.unique()
  # Create a dictionary that maps each unique value to a binary vector
  one_hot_dict = {}
  for i, val in enumerate(unique_vals):
    # Create a binary vector with all zeros except one at index i
    vector = [0] * len(unique_vals)
    vector[i] = 1
    # Add the vector to the dictionary with the value as the key
    one_hot_dict[val] = vector
  # Return the encoded column
  return col.map(one_hot_dict)

# Apply the one_hot_encode function to the others, BE, and Test columns
df[["others", "BE", "Test"]] = df[["others", "BE", "Test"]].apply(one_hot_encode)

# Print the normalized data frame
print(df)
