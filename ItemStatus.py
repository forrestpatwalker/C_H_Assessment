import requests
import os
from dotenv import load_dotenv


def get_item_status(item_key: str, value: str):
    """get_item_status.

    A function that when called makes an API call to the dsco REST API to grab the status of an item.

    :param item_key: A string of the item identifier to query
    :param value: A string of the item identifier to find
    :return: Void
    """
    # Load the .env variables
    load_dotenv()
    headers = {'Authorization': os.environ.get('DscoAuth')}
    parameters = {
        'itemKey':  item_key,
        'value': value
    }

    resp = requests.get(os.environ.get('DscoURL'), headers=headers, params=parameters)
    json_data = resp.json()

    print(f"upc: {json_data['upc']}")
    print(f"quantityAvailable: {json_data['quantityAvailable']}")


if __name__ == '__main__':
    get_item_status('sku', 'TESTSKU01')
