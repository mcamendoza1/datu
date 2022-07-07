import sys

from nifi_api_helper import *


def example_v1(username, password, domain):
    nifi_api_helper = NiFiAPIHelper(username, password, domain)
    access_token = nifi_api_helper.get_access_token()
    print('Example 1: ')
    print(access_token)


def example_v2(username, password, domain):
    nifi_api_helper = NiFiAPIHelper()
    nifi_api_helper.set_domain(domain)
    nifi_api_helper.set_auth(username, password)
    access_token = nifi_api_helper.get_access_token()
    print('Example 2: ')
    print(access_token)


def main():
    domain = sys.argv[1]
    username = str(sys.argv[2])
    password = str(sys.argv[3])
    example_v1(username, password, domain)
    example_v2(username, password, domain)


if __name__ == "__main__":
    main()
