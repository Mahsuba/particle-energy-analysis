# Particle Energy Analysis (Python, Pandas, NumPy, Matplotlib)

This project analyzes particle collision data similar to what is seen in CERN experiments.  
It uses Python, NumPy, Pandas, and Matplotlib to clean, analyze, group, and visualize particle energies.

---

#  Dataset Description
The dataset `particle.csv` contains:
- `event` – event number
- `particle_id` – PDG particle code
- `particle_name` – human-readable name
- `energy` – particle energy (GeV)
- `px`, `py`, `pz` – momentum components
- `charge` – particle charge

Particles include electrons, muons, photons, pions, and protons.

---

##  What the Project Does..

#  1. Load and inspect data
- `head()`, `info()`, `describe()`
- Checks missing values
- Calculates mean and standard deviation

# 2. Clean the data
- Drops missing rows
- Shows before/after cleaning

# 3. Analyze energies
- Computes mean and std
- Detects high-energy particles
- Groups particles into:
  - low energy
  - medium energy
  - high energy

# 4. Visualize energies
- Histogram of energies
- Line plot of energy trends

# 5. Save cleaned dataset
- Creates `cleaned_particle_data.csv`

---

## Visual Outputs....

# Histogram  
Shows how particle energies are distributed.

# Line Plot  
Shows energy changes across events.

---

# Tools Used
- Python
- Pandas
- NumPy
- Matplotlib

---

# Skills Demonstrated
- Data cleaning
- Scientific data analysis
- Statistical grouping
- Data visualization
- CSV processing
- Pandas advanced operations

---

# Files Included

- `particle.csv` — dataset  
- `particleAnalysis.py` — project code  
- `cleaned_particle_data.csv` — cleaned data output  
- `README.md` — this project report  

---

# --- Summary ---

This project simulates a beginner-level particle physics analysis similar to real experiments at CERN.  
It shows how to read, clean, analyze, visualize, and save scientific data using Python.

