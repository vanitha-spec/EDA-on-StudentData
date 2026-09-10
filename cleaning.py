import pandas as pd


def clean_whitespace(df):
    """
    Remove unnecessary spaces from text columns.
    """

    result = df.copy()

    result["Name"] = result["Name"].str.strip()
    result["Gender"] = result["Gender"].str.strip()
    result["City"] = result["City"].str.strip()

    return result


def standardize_categories(df):
    """
    Standardize Gender and City values.
    """

    result = df.copy()

    result["City"] = result["City"].replace({
        "hyderabad": "Hyderabad",
        "HYDERABAD": "Hyderabad",

        "chennai": "Chennai",
        "CHENNAI": "Chennai",

        "bengaluru": "Bengaluru",
        "BENGALURU": "Bengaluru",

        "mumbai": "Mumbai",
        "MUMBAI": "Mumbai",
    })

    result["Gender"] = result["Gender"].replace({
        "M": "Male",
        "m": "Male",
        "MALE": "Male",

        "F": "Female",
        "f": "Female",
        "FEMALE": "Female",
    })

    return result


def convert_numeric_columns(df):
    """
    Convert Age and Marks into numbers.
    """

    result = df.copy()

    result["Age"] = pd.to_numeric(
        result["Age"],
        errors="coerce"
    )

    result["Marks"] = pd.to_numeric(
        result["Marks"],
        errors="coerce"
    )

    return result


def remove_duplicates(df):
    """
    Remove duplicate rows.
    """

    result = df.copy()

    result = result.drop_duplicates()

    return result


def handle_missing_values(df):
    """
    Handle missing names, invalid ages,
    and missing marks.
    """

    result = df.copy()

    # Name is required
    result = result.dropna(
        subset=["Name"]
    )

    # Invalid ages become missing
    result.loc[
        (result["Age"] < 1) | (result["Age"] > 100),
        "Age"
    ] = pd.NA

    # Fill missing marks with average marks
    result["Marks"] = result["Marks"].fillna(
        result["Marks"].mean()
    )

    return result


def clean_names(df):
    """
    Convert names to title case.
    """

    result = df.copy()

    result["Name"] = result["Name"].str.title()

    return result


def add_performance_category(df):
    """
    Create a Performance column based on Marks.
    """

    result = df.copy()

    def performance_category(mark):

        if mark >= 90:
            return "Excellent"

        elif mark >= 75:
            return "Good"

        else:
            return "Needs Improvement"

    result["Performance"] = result["Marks"].apply(
        performance_category
    )

    return result