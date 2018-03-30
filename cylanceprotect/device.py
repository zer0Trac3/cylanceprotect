import requests


class Devices(object):
    '''The Device API for Cylance Protect.'''
    __module__ = 'cylanceprotect'

    def __init__(self, token=None, url=None):
        self._token = token
        self.url = url

    def get_devices(self, page=None, page_size=None):
        '''Allows a caller to request a page with a list of Console device resources belonging to a Tenant, sorted by
        registration (created) date in descending order (most recent device registered listed first). The page number
        and page size parameters are optional. When the values are not specified, these default to 1 and 10
        respectively.'''

        url = '%s/devices/v2' % self.url
        headers = {"Accept": "application/json; charset=utf-8", "Authorization": "Bearer %s " % self._token}
        data = {'page': page, 'page_size': page_size}
        resp = requests.get(url, headers=headers, params=data)
        return resp

    def get_device(self, device_id):
        '''Allows a caller to request a specific device resource belonging to a Tenant.'''

        url = '%s/devices/v2/%s' % (self.url, device_id)
        headers = {"Accept": "application/json; charset=utf-8", "Authorization": "Bearer %s " % self._token}
        resp = requests.get(url, headers=headers)
        return resp

    def update_device(self, device_id, name, policy_id=None, add_zone_ids=None, remove_zone_ids=None):
        '''Allows a caller to update a specific Console device resource belonging to a Tenant.'''

        url = '%s/devices/v2/%s' % (self.url, device_id)
        headers = {"Accept": "application/json; charset=utf-8", "Content-Type": "application/json",
                   "Authorization": "Bearer %s " % self._token}
        data = {"name":name, "policy_id":policy_id, "add_zone_ids":[add_zone_ids], "remove_zone_ids":[remove_zone_ids]}
        resp = requests.put(url, headers=headers, data=data)
        return resp

    def get_device_threats(self, device_id, page=None, page_size=None):
        '''Allows a caller to request a page with a list of threats found on a specific device. The page number and
        page size parameters are optional. When the values are not specified, these default to 1 and 10 respectively.
        The maximum page size that can be specified is 200 entries per page.'''

        url = '%s/devices/v2/%s/threats' % (self.url, device_id)
        headers = {"Accept": "application/json; charset=utf-8", "Authorization": "Bearer %s " % self._token}
        data = {'page': page, 'page_size': page_size}
        resp = requests.get(url, headers=headers, params=data)
        return resp

    def update_device_threat(self, device_id, threat_id, event):
        '''Allows a caller to update the status (waive or quarantine) of a convicted threat.'''

        url = '%s/devices/v2/%s/threats' % (self.url, device_id)
        headers = {"Accept": "application/json; charset=utf-8", "Content-Type": "application/json",
                   "Authorization": "Bearer %s " % self._token}
        data = {"threat_id": threat_id, "event": event}
        resp = requests.put(url, headers=headers, data=data)
        return resp

    def get_zone_devices(self, unique_zone, page, page_size):
        '''Allows a caller to request a page with a list of Console device resources belonging to a Zone, sorted by
        registration (created) date, in descending order (most recent registered listed first). The page number and
        page size parameters are optional. When the values are not specified, these default to 1 and 10 respectively.
        The maximum page size that can be specified is 200 entries per page.'''

        url = '%s/devices/v2/%s/devices' % (self.url, unique_zone)
        headers = {"Accept": "application/json; charset=utf-8", "Authorization": "Bearer %s " % self._token}
        data = {'page': page, 'page_size': page_size}
        resp = requests.get(url, headers=headers, params=data)
        return resp

    def get_agent_installer_link(self, region_code, product, os, package, architecture, build):
        '''Allows a caller to request a secured link to download the Agent installer.'''

        url = '%s/devices/v2/installer'
        headers = {"Accept": "application/json; charset=utf-8", "Authorization": "Bearer %s " % self._token}
        data = {'product': product, 'os': os, 'package': package, 'architecture': architecture, 'build': build}
        resp = requests.get(url, headers=headers, params=data)
        return resp

    def delete_devices(self, device_id, callback_url=None):
        '''Allows a caller to delete one or more devices from an organization.
        Note: This is an asynchronous operation
        and could take up to two hours to delete the devices. If a callback URL is provided, the callback will occur
        when deletion is complete.'''

        url = '%s/devices/v2/'
        headers = {"Accept": "application/json; charset=utf-8", "Content-Type": "application/json",
                   "Authorization": "Bearer %s " % self._token}

        data = {"device_ids":[device_id], "callback_url": callback_url}
        resp = requests.delete(url, headers=headers, data=data)
        return resp

    def delete_devices_post(self, device_id, callback_url=None):
        '''Note: Not all clients support sending a DELETE request. For this instance, use the following POST instead.'''

        url = '%s/devices/v2/delete'
        headers = {"Accept": "application/json; charset=utf-8", "Content-Type": "application/json",
                   "Authorization": "Bearer %s " % self._token}
        data = {"device_ids": [device_id], "callback_url": callback_url}
        resp = requests.post(url, headers=headers, data=data)
        return resp

    def device_by_mac_address(self, mac):
        '''Allows a caller to request a specific device resource belonging to a Tenant, by using the MAC address of
        the device. Use the following formats: 00-00-00-00-00-00 or 00:00:00:00:00:00'''

        url = '%s/devices/v2/macaddress/%s' % mac
        headers = {"Accept": "application/json; charset=utf-8", "Authorization": "Bearer %s " % self._token}
        resp = requests.get(url, headers=headers)
        return resp



