import enum
import sys
import requests

import httpheaders 

def get_access_token(username, password, domain):
    url = '{domain}/nifi_api/access/token'.format(domain=domain)
    # headers = Header.Form{
    #     "Accept-Encoding": "gzip, deflate, br",
    #     "Accept": "*/*",
    #     "Content-Type": "application/x-www-form-urlencoded",
    # }
    headers = httpheaders.Header.Form.value
    print(headers)
    # body = {'username': username, 'password': password}
    # response = requests.post(url, data=body, headers=headers)
    # return response


def update_processor_status(access_token, processor_id, ):
    url = '{domain}/nifi_api/access/token'.format(domain=domain)
    headers = {
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "*/*",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    body = {'username': username, 'password': password}
    response = requests.post(url, data=body, headers=headers)
    return response


def main():

    nifi_api = sys.argv[1]
    username = str(sys.argv[2])
    password = str(sys.argv[3])

    print(get_access_token(username, password, nifi_api))


if __name__ == "__main__":
    main()
