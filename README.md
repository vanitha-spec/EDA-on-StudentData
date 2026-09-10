# Student Data Cleaning with Python & Pandas

## Project Level

Beginner

## Objective

This project teaches the basics of cleaning messy student data using:

- Python
- Pandas
- CSV files

## Project Structure

student_data_cleaning/

├── data/
│   └── students.csv

├── main.py
├── cleaning.py
├── requirements.txt
└── README.md

## What This Project Does

The project:

1. Reads student data
2. Inspects the dataset
3. Finds missing values
4. Finds duplicate rows
5. Removes unnecessary spaces
6. Standardizes city names
7. Standardizes gender values
8. Converts Age and Marks into numbers
9. Removes duplicate rows
10. Handles missing values
11. Cleans student names
12. Creates a Performance column
13. Sorts students by marks
14. Calculates city-wise average marks
15. Saves the cleaned dataset

## Data Cleaning Flow

students.csv

↓

Read Data

↓

Understand Data

↓

Find Problems

↓

Clean Text

↓

Standardize Categories

↓

Convert Numbers

↓

Remove Duplicates

↓

Handle Missing Values

↓

Create Performance Category

↓

Analyze Data

↓

Export Cleaned Data

## Installation

Open the terminal inside the project folder.

Run:

pip install -r requirements.txt

## Run the Project

Run:

python main.py

## Output

The cleaned dataset will be created here:

data/students_cleaned.csv

## Important Pandas Concepts

This project introduces:

- read_csv()
- head()
- shape
- columns
- dtypes
- isna()
- unique()
- value_counts()
- duplicated()
- describe()
- str.strip()
- replace()
- to_numeric()
- drop_duplicates()
- dropna()
- fillna()
- sort_values()
- apply()
- groupby()
- to_csv()

## Learning Principle

For every cleaning operation, understand:

What is wrong?

↓

How do we identify the problem?

↓

Which Pandas operation can solve it?

↓

Why does that operation work?

↓

What changed in the data?   