from __future__ import annotations

import pandas as pd


def transform(df_raw: pd.DataFrame) -> pd.DataFrame:
    """
    Transform: 前処理・正規化を行い、ロード可能なスキーマに揃える。
    既存の正規化ロジックをここへ移す。
    """
    df = df_raw.copy()

    # 例：空白除去（必要なものだけ残す）
    df.columns = [c.strip() for c in df.columns]

    # 例：必須カラムの存在チェック（運用想定として“壊れ方”を明確にする）
    required_cols = ["date", "product", "amount"]  # ←既存に合わせて変更
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    # 例：型の正規化
    df["date"] = pd.to_datetime(df["date"], errors="coerce").dt.date
    df["product"] = df["product"].astype(str).str.strip()
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

    # 例：欠損の扱い（既存方針に合わせる）
    df = df.dropna(subset=["date", "product", "amount"])

    # 例：並び順固定（再現性）
    df = df.sort_values(["date", "product"]).reset_index(drop=True)

    return df
