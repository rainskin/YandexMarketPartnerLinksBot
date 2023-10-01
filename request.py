import requests

import config

API_URL = 'https://api.content.market.yandex.ru/v3/affiliate/partner/link/create'


def create_partner_url(product_url: str):
    resp = requests.get(API_URL, params={'url': product_url, 'clid': config.CLID},
                        headers={'Authorization': config.API_KEY})
    return resp.json()['link']['shortUrl']
