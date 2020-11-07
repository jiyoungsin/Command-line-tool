from typing import List
from urllib.parse import urlparse
import requests


# GETTERS
def get_response_code(url):
    header = requests.head(url)
    return header.status_code


def get_urls_from_url(url: str) -> List[str]:
    url_obj = urlparse(url)
    data = requests.get(url).json()
    # for entry in data:
    #     list_of_urls.append(f"{url_obj.scheme}://{url_obj.netloc}{entry['url']}")
    return [f"{url_obj.scheme}://{url_obj.netloc}{entry['url']}" for entry in data]


def get_urls_from_file(path: str) -> List[str]:
    """
    this function reads the given file and returns an array of urls.
    """
    # Open the file and read all lines
    with open(path, "rt", encoding="utf-8") as urls_file:
        all_lines = urls_file.readlines()

    # Loop on each line and append it to the list
    return [line.strip() for line in all_lines]


def check_urls(list_of_urls):
    return [{url: get_response_code(url)} for url in list_of_urls]


if __name__ == "__main__":
    urls = get_urls_from_url("https://telescope.cdot.systems/posts")
    links_with_status_code = check_urls(urls)
