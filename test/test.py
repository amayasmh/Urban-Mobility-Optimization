import json
import logging
from idlelib.colorizer import color_config

import httpx
from black import color_diff, datetime

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)  # Logger creation

# URL and headers definition
url = "https://prim.iledefrance-mobilites.fr/marketplace/estimated-timetable"
headers = {"apikey": "bl51pll3Cxab4dbEKmxU7qKGFbsKTAY7"}

try:
    # Requête à l'API
    response = httpx.get(url, headers=headers)
    response.raise_for_status()  # Verify if the request was successful

    # JSON response recuperation
    data = response.json()

    # Save data in a JSON file
    with open(
        f"data_{datetime.now().strftime('%Y%m%d%H%M%S')}.json", "w", encoding="utf-8"
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
