"""
==========================================================
IntentIQ

File: run_pipeline.py

Description:
Runs the complete IntentIQ data pipeline.

Pipeline:
1. Scrape product prices
2. Load latest prices into price_history
3. Generate notifications
4. Dispatch email notifications

Author: Arjun S Nair
==========================================================
"""
import time
from src.config.logger import logger
from src.scraper import (
    amazon_scraper,
    flipkart_scraper,
    croma_scraper,
    reliance_digital_scraper,
    apple_store_scraper
)

from src.etl import price_history_loader

from src.notifications import (
    notification_engine,
    notification_dispatcher
)

# ==========================
# Pipeline Configuration
# ==========================

PIPELINE_STEPS = [

    (
        "Amazon Scraper",
        amazon_scraper.main
    ),

    (
        "Flipkart Scraper",
        flipkart_scraper.main
    ),

    (
        "Croma Scraper",
        croma_scraper.main
    ),

    (
        "Reliance Digital Scraper",
        reliance_digital_scraper.main
    ),

    (
        "Apple Store Scraper",
        apple_store_scraper.main
    ),

    (
        "Price History Loader",
        price_history_loader.main
    ),

    (
        "Notification Engine",
        notification_engine.main
    ),

    (
        "Notification Dispatcher",
        notification_dispatcher.main
    )
]

# ==========================
# Pipeline Runner
# ==========================

def run_pipeline():

    print("\n" + "=" * 60)
    print("IntentIQ Pipeline Started")
    print("=" * 60)

    logger.info("Pipeline started.")

    pipeline_results = []
    start_time = time.time()

    for step_name, step_function in PIPELINE_STEPS:

        print(f"\nRunning: {step_name}")

        logger.info(f"Starting: {step_name}")

        step_start = time.time()

        try:

            step_function()

            duration = time.time() - step_start

            pipeline_results.append(
                {
                "step": step_name,
                "status": "FAILED",
                "duration": duration
                }
            )
            logger.exception(f"{step_name} failed.")

            break

    print("\n" + "=" * 60)
    print("IntentIQ Pipeline Summary")
    print("=" * 60)

    for result in pipeline_results:
        print(
            f"{result['step']:<30}"
            f"{result['status']:<10}"
            f"{result['duration']:.2f} sec"
            )
        
    print("-" * 60)

    print(f"Total Runtime: {total_runtime:.2f} sec")

    print("=" * 60)

    logger.info (
    f"Pipeline completed in "
    f"{total_runtime:.2f} seconds."
    )

    total_runtime = time.time() - start_time
    logger.info("Pipeline finished.")

# ==========================
# Main
# ==========================

if __name__ == "__main__":

    run_pipeline()
