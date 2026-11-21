"""Data analysis pipeline for golden-vortex."""

import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


def load_data(data_dir: str) -> pd.DataFrame:
    """Load and concatenate CSV files from a directory."""
    data_path = Path(data_dir)
    files = list(data_path.glob("*.csv"))
    if not files:
        raise FileNotFoundError(f"No CSV files found in {data_dir}")
    dfs = [pd.read_csv(f) for f in files]
    return pd.concat(dfs, ignore_index=True)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and preprocess the data."""
    df = df.drop_duplicates()
    df = df.dropna(subset=["value"])
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df.sort_values("timestamp")


def analyze(df: pd.DataFrame) -> dict:
    """Compute summary statistics."""
    return {
        "count": len(df),
        "mean": df["value"].mean(),
        "std": df["value"].std(),
        "min": df["value"].min(),
        "max": df["value"].max(),
    }


def visualize(df: pd.DataFrame, output_dir: str):
    """Generate and save plots."""
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(12, 6))
    df.plot(x="timestamp", y="value", ax=ax)
    ax.set_title("Time Series Analysis")
    fig.savefig(out / "timeseries.png", dpi=150, bbox_inches="tight")

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.histplot(df["value"], kde=True, ax=ax)
    ax.set_title("Value Distribution")
    fig.savefig(out / "distribution.png", dpi=150, bbox_inches="tight")

    plt.close("all")


def main():
    parser = argparse.ArgumentParser(description="golden-vortex data analysis")
    parser.add_argument("--data", required=True, help="Data directory")
    parser.add_argument("--output", default="results", help="Output directory")
    args = parser.parse_args()

    print(f"Loading data from {args.data}...")
    df = load_data(args.data)
    print(f"Loaded {len(df)} rows")

    df = clean_data(df)
    stats = analyze(df)
    print(f"Stats: {stats}")

    visualize(df, args.output)
    print(f"Plots saved to {args.output}")


if __name__ == "__main__":
    main()