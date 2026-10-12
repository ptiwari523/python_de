import logging

logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("🚀 Pipeline Started!")

try:
    amount = "100"
    total = amount + 50
    logging.info(f"Total amount calculated: {total}")
except Exception as e:
    logging.error(f"🚫 Pipeline failed: {e}")

logging.info("✅ Pipeline completed successfully!")
    
