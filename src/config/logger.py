"""
==========================================================
IntentIQ

File: logger.py

Description:
Centralized logging configuration for IntentIQ.

Author: Arjun S Nair
==========================================================
"""
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

# --------------------------
# Log Directory
# --------------------------

BASE_DIR = Path(__file__).resolve().parents[2]

LOG_DIR = BASE_DIR / "logs"

LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "intentiq.log"

# --------------------------
# Logger
# --------------------------

logger = logging.getLogger("IntentIQ")

logger.setLevel(logging.INFO)

# Avoid duplicate handlers

if not logger.handlers:
    
    formatter = logging.Formatter(

        "%(asctime)s | %(levelname)s | %(message)s",

        datefmt="%Y-%m-%d %H:%M:%S"

    )

    # Console

    console_handler = logging.StreamHandler()

    console_handler.setFormatter(formatter)

    # Rotating File

    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=1_000_000,
        backupCount=5,
        encoding="utf-8"
    )

    file_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
