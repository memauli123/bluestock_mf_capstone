"""
Master execution script for Bluestock Mutual Fund Analytics Capstone.
Runs the ETL pipeline from ingestion to database loading.
"""

import subprocess

print("Starting ETL Pipeline...")

subprocess.run(
    ["python", "scripts/data_ingestion.py"]
)

subprocess.run(
    ["python", "scripts/data_cleaning.py"]
)

subprocess.run(
    ["python", "scripts/load_to_sqlite.py"]
)

print("ETL Pipeline Completed Successfully.")