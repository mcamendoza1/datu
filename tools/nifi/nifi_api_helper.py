import json 

import requests

from http_headers import HttpHeader


class NiFiAPIHelper:

    def __init__(self, username=None, password=None, domain=None):
        self.domain = domain
        self.username = username
        self.password = password
        self.access_token = None

        self.ACCESS = '/nifi-api/access'
        self.PROCESSOR = '/nifi-api/processors'
        if domain != None and username != None and password != None:
            self.set_auth(username, password, domain)

    def set_domain(self, url):
        self.domain = url

    def get_domain(self):
        return self.domain

    def set_auth(self, username, password, domain=None):
        if domain == None:
            domain = self.get_domain()

        url = f'{domain}{self.ACCESS}/token'
        headers = HttpHeader.FORM.value
        body = {'username': username, 'password': password}
        self.access_token = requests.post(url, data=body, headers=headers).text

    def get_access_token(self):
        return self.access_token

    # def get_processs_details(domain):
    #     return 0

    # def update_processor_state(self, access_token, processor_id, state):
    #     url = f'{self.domain}{self.PROCESSOR}/{processor_id}/run-status'
    #     headers = HttpHeader.JSON.value
    #     auth = {'Authorization': f'Bearer {self.access_token}'}
    #     # response = requests.put(url, data=body, headers=headers)
    #     print(auth, url)

        # return response

# {
#     "revision": {
# 	    "clientId": "d320a5df-0181-1000-2f03-3c780149ce44",
# 	    "version": 0
# 	},
#     "state": "STOPPED",
#     "disconnectedNodeAcknowledged": true
# }
