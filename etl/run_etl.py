import argparse
import logging
from pathlib import Path

from etl.extract import extract_all_csv  
from etl.transform import transform_all  
from etl.load import load_to_sqlite      

logger = logging.getLogger(__name__)


def parse_args():
    p = argparse.ArgumentParser(description="Sales KPI ETL batch")
    p.add_argument("--input", default="data/raw", help="raw csv directory")
    p.add_argument("--output", default="data/processed", help="processed output directory")
    p.add_argument("--db", default="db/app.sqlite", help="sqlite db path")
    p.add_argument("--table", default="kpi_mart", help="destination table name")
    return p.parse_args()


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    args = parse_args()

    input_dir = Path(args.input)
    output_dir = Path(args.output)
    db_path = Path(args.db)

    logger.info("ETL start input=%s output=%s db=%s table=%s", input_dir, output_dir, db_path, args.table)

    # extract
    df_raw = extract_all_csv(input_dir)   
    logger.info("extract done: rows=%d cols=%d", len(df_raw), len(df_raw.columns))

    # transform
    df = transform_all(df_raw)            
    logger.info("transform done: rows=%d cols=%d", len(df), len(df.columns))
    output_dir.mkdir(parents=True, exist_ok=True)
    (df
     .to_csv(output_dir / "kpi_mart.csv", index=False)
    )
    logger.info("write processed: %s", output_dir / "kpi_mart.csv")

    # load
    load_to_sqlite(df, db_path=db_path, table_name=args.table)  
    logger.info("load done")

    logger.info("ETL success")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
