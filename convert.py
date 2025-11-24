import pandas as pd

# Load the .dat file using '::' as the separator
df = pd.read_csv("data/ratings.dat", delimiter="::", engine="python", names=["user_id", "movie_id", "rating", "Timestamp"])

# Save to CSV
df.to_csv("ratings.csv", index=False)

print("Conversion complete! Saved as ratings.csv")