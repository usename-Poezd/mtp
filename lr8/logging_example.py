from __future__ import annotations

import logging


def configure_logging(level: int = logging.DEBUG) -> logging.Logger:
    logger = logging.getLogger("lr8.demo")
    logger.setLevel(level)

    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(
            logging.Formatter("[%(asctime)s] [%(levelname)s] %(name)s: %(message)s")
        )
        logger.addHandler(handler)

    return logger


def main() -> None:
    logger = configure_logging()

    logger.debug("Debug message: for detailed tracing during development")
    logger.info("Info message: high-level information about program flow")
    logger.warning("Warning message: something unexpected happened, but we can continue")
    logger.error("Error message: an error occurred")


if __name__ == "__main__":  # pragma: no cover - точка входа для ручного запуска
    main()
