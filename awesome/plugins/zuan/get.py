import requests

url = 'https://nmsl.shadiao.app/api.php?from=fgnwhguqipweHFG'


def get_zuan():
    r = requests.get(url=url)
    return r.text
