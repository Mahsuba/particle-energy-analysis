# Project Structure
particle-energy-analysis/
├── data/
│   ├── particle.csv
│   └── cleaned_particle_data.csv
├── src/
│   └── particleAnalysis.py
├── README.md
└── requirements.txt

# Installation

Install the required Python packages:

pip install -r requirements.txt


# Dependencies:

pandas

numpy

matplotlib

# How to Run

Run the analysis script from your terminal:

# Navigate to the project
cd particle-energy-analysis

# Go into the source folder
cd src

# Run the script
python particleAnalysis.py


The script will:

Load the particle energy dataset

Clean missing values

Compute mean and standard deviation

Detect high-energy particle events

Group energies into low/medium/high

Generate scientific plots

Save cleaned dataset

Output appears in:

data/cleaned_particle_data.csv

# Features & Methods
1. Data Loading & Overview

read_csv()

head()

info()

describe()

2. Data Cleaning

Remove missing rows

Fill missing values

3. Statistical Analysis

Mean

Standard deviation

High-energy threshold

Grouping using pd.cut()

4. Visualization

Histogram

Line plot

5. Saved Output

Cleaned dataset in /data

# What This Project Demonstrates

Reading scientific datasets

Cleaning noisy data

Using Pandas & NumPy

Producing visual analysis

Writing organized Python code

Creating a reproducible project

Structuring folders professionally

# Future Improvements

Gaussian curve fitting

More particle features

Interactive plots

Jupyter Notebook version

Monte Carlo simulation

# Author

Mahsuba(Mahim Islam)
Beginner data analyst with interest in physics & scientific computing.

📜 License

MIT License.



