import pandas as pd

df=pd.read_csv("particle.csv")

print("--first 5 rows: --")
print(df.head())

print("\n--Structure of the data--")
print(df.info())

print("\n--Describe (STATISTICS: )--")
print(df.describe())

print("\n--CHEAKING MISSING VALUES--\n")
print(df.isna().sum)


print("\n--Mean Energy--")
print(df["energy"].mean())

print("\n--STANDARD DEVIATION OF ENERGY--")
print(df["energy"].std())


print("\n CLEANING DATA......")
print("\n--MISSING VALUES IN EACH COLUMN: ")
print(df.isna().sum())
df_clean=df.dropna()

#showing how many rows were removed
print("\n Roes before cleaning: ",len(df))
print("Rows after cleaning: ",len(df_clean))

print("\n--Cleaned Data(first rows)--")
print(df_clean.head())

print("\n===  ANALYZE ENERGIES ===")
mean_energy=df_clean["energy"].mean()
std_energy=df_clean["energy"].std()

print("\nMean energy:", mean_energy)
print("\n Standard deviation of energy:", std_energy)


# we will define "high energy" as energy > mean + 1 * std

high_threshold = mean_energy + std_energy
print("\nHigh energy threshold (mean + 1*std):", high_threshold)

high_energy_events =df_clean[df_clean["energy"]>high_threshold]
print("\n--- High-energy events (energy > threshold) ---")
print(high_energy_events)


# Group energies into low , medium , high
# low: below (mean - std)
# medium: between (mean - std) and (mean + std)
# high: above (mean + std)

low_limit = mean_energy - std_energy
high_limit = mean_energy + std_energy


my_bins = [0, low_limit, high_limit, df_clean["energy"].max() + 1]
my_labels = ["low", "medium", "high"]


df_clean["energy_group"] = pd.cut(df_clean["energy"],
                                  bins=my_bins,
                                  labels=my_labels,
                                  include_lowest=True)

print("\n--- Energy groups for each particle ---")
print(df_clean[["event", "particle_name", "energy", "energy_group"]])

print("\n--- Count of particles in each energy group ---")
print(df_clean["energy_group"].value_counts())

print("\n--- Average energy in each group ---")
print(df_clean.groupby("energy_group")["energy"].mean())


import matplotlib.pyplot as plt

print("\n=== VISUALIZE ENERGIES ===")

# Histogram of energies
plt.figure(figsize=(8,5))
plt.hist(df_clean["energy"], bins=10)
plt.xlabel("Energy (GeV)")
plt.ylabel("Count")
plt.title("Particle Energy Distribution")
plt.show()

# Line plot: energy vs event index
plt.figure(figsize=(8,5))
plt.plot(df_clean["energy"])
plt.xlabel("Index")
plt.ylabel("Energy (GeV)")
plt.title("Energy Trend Across Particles")
plt.show()


print("\n=== SAVE CLEANED DATA ===")
df_clean.to_csv("cleaned_particle_data.csv", index=False)

print("Cleaned data saved as cleaned_particle_data.csv")



