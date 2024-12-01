"""
Author: Johnson
Description: This utility module provides a standardized logging setup for all pipeline components. 
It ensures consistent logging format and log levels across the pipeline.
"""

import logging

def setup_logger(name, log_file, level=logging.INFO):
    """
    Sets up a logger with the specified name, log file, and log level.

    Args:
        name (str): Name of the logger (e.g., the module or script name).
        log_file (str): Path to the log file where logs will be written.
        level (int): Logging level (default is logging.INFO).

    Returns:
        logging.Logger: Configured logger instance.
    """
    # Create a logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create file handler which logs messages to a file
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(level)

    # Create console handler to output logs to the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)

    # Define log message format
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
