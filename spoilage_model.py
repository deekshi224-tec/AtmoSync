
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
CSV_FILE = BASE_DIR / "sensor_data.csv"

REQUIRED_COLUMNS = [
    "container_id",
    "commodity",
    "timestamp",
    "temperature",
    "humidity",
    "vibration"
]

NUMERIC_COLUMNS = ["temperature", "humidity", "vibration"]


def analyze_sensor_data():
    if not CSV_FILE.exists():
        print("Sensor data not found. Run the simulator first.")
        return

    try:
        df = pd.read_csv(CSV_FILE)
    except (pd.errors.ParserError, OSError) as error:
        print("Unable to read sensor data:", error)
        return

    if df.empty:
        print("The sensor data file is empty.")
        return

    missing_columns = [
        col for col in REQUIRED_COLUMNS if col not in df.columns
    ]

    if missing_columns:
        print("Missing required columns:", missing_columns)
        return

    print("\n--- Sensor Data Validation ---")

    df["timestamp"] = pd.to_datetime(
        df["timestamp"], errors="coerce", utc=True
    )

    for column in NUMERIC_COLUMNS:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    print("\n--- Missing Values Before Handling ---")
    print(df[REQUIRED_COLUMNS].isnull().sum())

    # Remove records without essential identification details.
    initial_rows = len(df)
    df = df.dropna(subset=["container_id", "commodity", "timestamp"])
    removed_records = initial_rows - len(df)

    # Replace missing sensor measurements with each column's median.
    for column in NUMERIC_COLUMNS:
        if df[column].notna().any():
            median_value = df[column].median()
            df[column] = df[column].fillna(median_value)

    print("\n--- Missing Value Handling ---")
    print("Records removed due to missing identifiers or timestamps:",
          removed_records)

    print("Remaining missing sensor values:")
    print(df[NUMERIC_COLUMNS].isnull().sum())

    # Check sensor measurement ranges.
    invalid_records = (
        ~df["humidity"].between(0, 100)
        | (df["vibration"] < 0)
        | ~df["temperature"].between(-50, 100)
    )

    print("Invalid sensor records:", int(invalid_records.sum()))
    df = df.loc[~invalid_records].copy()

    if df.empty:
        print("No valid sensor readings available.")
        return

    print("\n--- Valid Sensor Data ---")
    print("Valid readings:", len(df))
    print("Containers:", df["container_id"].nunique())

    print("\n--- Average Temperature ---")
    print(df.groupby("container_id")["temperature"].mean().round(2))

    print("\n--- Average Humidity ---")
    print(df.groupby("container_id")["humidity"].mean().round(2))

    # Demonstration threshold, not a validated avocado quality limit.
    threshold = 25
    df["temperature_alert"] = df["temperature"] > threshold

    print("\n--- Temperature Alerts ---")
    print(
        df.groupby("container_id")["temperature_alert"]
        .sum()
        .astype(int)
    )


if __name__ == "__main__":
    analyze_sensor_data()
