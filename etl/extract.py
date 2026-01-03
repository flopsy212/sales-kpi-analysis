from __future__ import annotations

from pathlib import Path
import pandas as pd


def extract_csv(csv_path: str | Path, *, encoding: str = "utf-8") -> pd.DataFrame:
    """
    Extract: CSVを読み込んで生のDataFrameを返す。
    """
    csv_path = Path(csv_path)
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV not found: {csv_path}")

    df = pd.read_csv(csv_path, encoding=encoding)
    return df
