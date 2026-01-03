from __future__ import annotations

from pathlib import Path
import sqlite3
import pandas as pd


def load_to_sqlite(
    df: pd.DataFrame,
    *,
    db_path: str | Path,
    table_name: str,
    if_exists: str = "replace",
) -> None:
    """
    Load: SQLiteへ格納する。
    - バッチ再実行を想定して if_exists は基本 replace（または運用に合わせて変更）
    """
    db_path = Path(db_path)
    db_path.parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(db_path) as conn:
        df.to_sql(table_name, conn, if_exists=if_exists, index=False)
