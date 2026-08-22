#Generic HTTP behavior

import requests
from framework.utils.logger import get_logger

logger = get_logger(__name__)


class BaseClient:

    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint):
        logger.info(f"Sending GET request to {self.base_url + endpoint}")
        response = requests.get(self.base_url + endpoint)
        logger.info(f"GET request response: {response.status_code}")
        return response

    def post(self, endpoint, json=None):
        logger.info(f"Sending POST request to {self.base_url + endpoint}")                  
        response = requests.post(
            self.base_url + endpoint,
            json=json
        )
        logger.info(f"POST request response: {response.status_code}")
        return response

    def put(self, endpoint, json=None):
        logger.info(f"Sending PUT request to {self.base_url + endpoint}")
        response = requests.put(
            self.base_url + endpoint,
            json=json
        )
        logger.info(f"PUT request response: {response.status_code}")
        return response

    def delete(self, endpoint):
        logger.info(f"Sending DELETE request to {self.base_url + endpoint}")
        response = requests.delete(self.base_url + endpoint)
        logger.info(f"DELETE request response: {response.status_code}")
        return response