#!/usr/bin/python3

import requests
import json
from dewiki import parser
import sys


def put_usage():
    print('Usage: request_wikipedia.py search_text\n')
    sys.exit(1)


def parse_response(responce):
    pages = responce['query']['pages']
    revisions = None
    for page_id, page in pages.items():
        revisions = page.get('revisions')
        if revisions is None:
            print('Nothing found\n')
            sys.exit(1)
    found = revisions[0]['*']
    return parser.Parser().parse_string(found)


def put_search_result(api_url, search_text):
    request_param = {
        "action": "query",
        "prop": "revisions",
        "titles": search_text,
        "rvprop": "content",
        "format": "json",
        "redirects": ""
    }
    try:
        R = requests.get(url=api_url, params=request_param)
        if R.ok == False:
            print("Error {} :: {}".format(R.status_code, R.reason))
            exit(1)
        resp = R.json()
        if 'error' in resp.keys():
            print("Error in response: %s" % resp['error']['info'])
            exit(1)
        if 'query' not in resp.keys():
            print("No result for the search.")
            exit(1)
        parsed_response = parse_response(resp)    
        with open(search_text.replace(' ', '_') + '.wiki', 'w') as f:
            f.write(parsed_response)
    except Exception as e:
        print("Unknown error. Error description: {}".format(e))     


def get_search_text():
    argv = sys.argv
    if len(argv) == 2:
        return argv[1]
    else:
        put_usage()


if __name__ == '__main__':
    search_text = get_search_text()
    api_url = 'https://fr.wikipedia.org/w/api.php'
    put_search_result(api_url, search_text)