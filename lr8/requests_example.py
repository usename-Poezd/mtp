from __future__ import annotations

import logging
from typing import Final

import requests


logger = logging.getLogger(__name__)

DEFAULT_URL: Final[str] = "https://httpbin.org/get"


def fetch_status(url: str = DEFAULT_URL) -> int:
    """Выполнить GET-запрос и вернуть HTTP-статус код ответа."""

    logger.info("Requesting URL %s", url)
    response = requests.get(url, timeout=5)
    logger.info("Received status code %s", response.status_code)
    return response.status_code


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(name)s: %(message)s")

    status = fetch_status()
    print(f"Status code from {DEFAULT_URL}: {status}")


if __name__ == "__main__":
    main()
