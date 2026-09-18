import requests
from framework.utils.logger import get_logger

logger = get_logger(__name__)


class BaseClient:

    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint):
        url = self.base_url + endpoint
        logger.info(f"Sending GET request to {url}")

        response = requests.get(url)

        logger.info(
            f"GET response: {response.status_code} | "
            f"Body: {response.text}"
        )

        return response

    def post(self, endpoint, json=None):
        url = self.base_url + endpoint
        logger.info(
            f"Sending POST request to {url} | "
            f"Payload: {json}"
        )

        response = requests.post(
            url,
            json=json
        )

        logger.info(
            f"POST response: {response.status_code} | "
            f"Body: {response.text}"
        )

        return response

    def put(self, endpoint, json=None):
        url = self.base_url + endpoint
        logger.info(
            f"Sending PUT request to {url} | "
            f"Payload: {json}"
        )

        response = requests.put(
            url,
            json=json
        )

        logger.info(
            f"PUT response: {response.status_code} | "
            f"Body: {response.text}"
        )

        return response

    def delete(self, endpoint):
        url = self.base_url + endpoint
        logger.info(f"Sending DELETE request to {url}")

        response = requests.delete(url)

        logger.info(
            f"DELETE response: {response.status_code} | "
            f"Body: {response.text}"
        )

        return response