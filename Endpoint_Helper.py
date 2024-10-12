import yaml
import requests
from urllib.parse import urlparse
from Endpoint import Endpoint

#function to load raw endpoints from a filepath.
def load_endpoints(file_path):
    with open(file_path, "r") as f:
        load = yaml.safe_load(f)
    return load

#function to parse raw endpoints into objects. name and URL are required
def parse_endpoints(endpoints):
    endpoint_objects = []
    for raw in endpoints:
        name = raw.get("name")
        url = raw.get("url")
        method = raw.get("method","GET")
        headers = raw.get("headers")
        body = raw.get("body")
        endpoint = Endpoint(name, url, method, headers, body)
        endpoint_objects.append(endpoint)
    return endpoint_objects

def url_parser(url):
    parsed = urlparse(url)
    return parsed.hostname

def endpoint_checker(endpoint):
    method = endpoint.method
    url = endpoint.url
    headers = endpoint.headers
    body = endpoint.body
    try:
        response = requests.request(method,url,headers=headers,json=body,timeout=.5)
        if 200 <= response.status_code < 300:
            return True
        return False
    except requests.exceptions.Timeout:
        return False
