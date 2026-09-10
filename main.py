import pandas as pd

from cleaning import (
    clean_whitespace,
    standardize_categories,
    convert_numeric_columns,
    remove_duplicates,
    handle_missing_values,
    clean_names,
    add_performance_category
)


def main():

    # 1. Read the dataset
    df = pd.read_csv("students.csv")

    print("\n===== ORIGINAL DATA =====")
    print(df)

    # 2. Understand the data
    print("\n===== DATASET INFORMATION =====")
    print("Rows:", df.shape[0])
    print("Columns:", df.shape[1])
    print("Column Names:", df.columns.tolist())

    print("\n===== DATA TYPES =====")
    print(df.dtypes)

    # 3. Find problems
    print("\n===== MISSING VALUES =====")
    print(df.isna().sum())

    print("\n===== DUPLICATES =====")
    print("Duplicate rows:", df.duplicated().sum())

    # 4. Clean the data
    df = clean_whitespace(df)

    df = standardize_categories(df)

    df = convert_numeric_columns(df)

    df = remove_duplicates(df)

    df = handle_missing_values(df)

    df = clean_names(df)

    # 5. Add new information
    df = add_performance_category(df)

    # 6. Sort the data
    df = df.sort_values(
        by="Marks",
        ascending=False
    )

    # 7. Show cleaned data
    print("\n===== CLEANED DATA =====")
    print(df)

    # 8. Analyze data
    print("\n===== CITY-WISE AVERAGE MARKS =====")

    city_average = df.groupby("City")["Marks"].mean()

    print(city_average)

    # 9. Final missing-value check
    print("\n===== FINAL MISSING VALUES =====")
    print(df.isna().sum())

    # 10. Export
    output_path = "students_cleaned.csv"

    df.to_csv(
        output_path,
        index=False
    )

    print("\n===== PROJECT COMPLETED =====")
    print("Cleaned file saved to:", output_path)


if __name__ == "__main__":
    main()