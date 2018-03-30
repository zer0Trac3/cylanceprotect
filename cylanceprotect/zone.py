import requests


class Zone(object):
    '''The Zone API for Cylance Protect.'''
    __module__ = 'cylanceprotect'

    def __init__(self, token=None, url=None):
        self._token = token
        self.url = url

    def create_zone(self, name, policy_id, criticality):
        '''Create (add) a zone to your Console.'''

        url = '%s/zones/v2' % self.url
        headers = {"Accept": "application/json; charset=utf-8", "Content-Type": "application/json",
                   "Authorization": "Bearer %s " % self._token}
        data = {"name": name, "policy_id": policy_id, "criticality": criticality}
        resp = requests.post(url, data=data, headers=headers)
        return resp

    def get_zones(self, page=None, page_size=None):
        '''Request zone information for your organization. This will return the top 100 records.'''

        url = '%s/zones/v2' % self.url
        headers = {"Accept": "application/json; charset=utf-8", "Authorization": "Bearer %s " % self._token}
        data = {"page": page, "page_size": page_size}
        resp = requests.get(url, params=data, headers=headers)
        return resp

    def get_device_zones(self, zone_id, page, page_size):
        '''Request zone information for a specified device in your organization. This will return the top 100 records'''

        url = '%s/zones/v2/%s' % (self.url, zone_id)
        headers = {"Accept": "application/json; charset=utf-8", "Authorization": "Bearer %s " % self._token}
        data = {"page": page, "page_size": page_size}
        resp = requests.get(url, params=data, headers=headers)
        return resp

    def get_zone(self, zone_id):
        '''Request zone information for a specific zone in your organization.'''

        url = '%s/zones/v2/%s' % (self.url, zone_id)
        headers = {"Accept": "application/json; charset=utf-8", "Authorization": "Bearer %s " % self._token}
        resp = requests.get(url,  headers=headers)
        return resp

    def update_zone(self, zone_id, name, policy_id, criticality):
        '''Update a zone in your organization.'''

        url = '%s/zones/v2/%s' % (self.url, zone_id)
        headers = {"Accept": "application/json; charset=utf-8", "Content-Type": "application/json",
                   "Authorization": "Bearer %s " % self._token}

        data = {"name": name, "policy_id": policy_id, "criticality": criticality}
        resp = requests.put(url, headers=headers, data=data)
        return resp

    def delete_zone(self, zone_id):
        '''Delete (remove) a zone from your Console.'''

        url = '%s/zones/v2/%s' % (self.url, zone_id)
        headers = {"Authorization": "Bearer %s " % self._token}
        resp = requests.delete(url, headers=headers)
        return resp
