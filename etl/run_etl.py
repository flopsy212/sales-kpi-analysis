from __future__ import annotations

import argparse
import logging
from pathlib import Path

from etl.extract import extract_csv
from etl.transform import transform
from etl.load import load_to_sqlite


logger = logging.getLogger(__name__)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Run ETL batch (CSV -> pandas -> SQLite)")
    p.add_argument("--csv", required=True, help="Input CSV path")
    p.add_argument("--db", required=True, help="Output SQLite db path")
    p.add_argument("--table", default="normalized_sales", help="Destination table name")
    p.add_argument("--encoding", default="utf-8", help="CSV encoding")
    return p.parse_args()


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    args = parse_args()

    csv_path = Path(args.csv)
    db_path = Path(args.db)

    logger.info("ETL start: csv=%s db=%s table=%s", csv_path, db_path, args.table)

    df_raw = extract_csv(csv_path, encoding=args.encoding)
    logger.info("Extract done: rows=%d cols=%d", len(df_raw), len(df_raw.columns))

    df_norm = transform(df_raw)
    logger.info("Transform done: rows=%d cols=%d", len(df_norm), len(df_norm.columns))

    load_to_sqlite(df_norm, db_path=db_path, table_name=args.table, if_exists="replace")
    logger.info("Load done")

    logger.info("ETL success")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
