import json
import logging
import os
from datetime import datetime

import httpx
from dotenv import load_dotenv


def main():
    """
    Main function
    """
    # Logger configuration
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - [test][%(levelname)s] - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename="test.log",
    )
    logger = logging.getLogger(__name__)  # Logger creation

    # URL and headers definition
    url = "https://prim.iledefrance-mobilites.fr/marketplace/estimated-timetable"
    headers = {"apikey": ""}
    # API key recuperation from .env file
    load_dotenv()
    headers["apikey"] = os.getenv("API_KEY")

    try:
        # Requête à l'API
        response = httpx.get(url, headers=headers)
        response.raise_for_status()  # Verify if the request was successful

        # JSON response recuperation
        data = response.json()

        # Save data in a JSON file
        with open(
            f"data_{datetime.now().strftime('%Y%m%d%H%M%S')}.json",
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        logger.info("Data saved in data.json.")

    except httpx.HTTPStatusError as e:
        logger.error(f"HTTP Error {e.response.status_code}: {e}")
    except httpx.RequestError as e:
        logger.error(f"Request Error: {e}")
    except json.JSONDecodeError:
        logger.error("Error : JSON response could not be decoded.")
    except Exception as e:
        logger.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
