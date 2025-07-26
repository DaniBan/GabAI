import logging

def setup_logging(
    level: int = logging.INFO,
    format_string: str = "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s"
):
    logging.basicConfig(
        level=level,
        format=format_string
    )

def get_logger(name: str):
    return logging.getLogger(name)