import requests


class Threats(object):
    '''The threat API for Cylance Protect. Threat API uses SHA 256 hashes '''
    __module__ = 'cylanceprotect'

    def __init__(self, token=None, url=None):
        self._token = token
        self.url = url

    def get_threat(self, hash_256):
        '''Request threat details for a specific threat.'''

        url = '%s/threats/v2/%s' % (self.url, hash_256)
        headers = {"Accept": "application/json; charset=utf-8", "Authorization": "Bearer %s " % self._token}
        resp = requests.get(url, headers=headers)
        return resp

    def get_threats(self, page=None, page_size=None):
        '''Allows a caller to request a page with a list of Console threat resources belonging to a Tenant, sorted by
        the last found date, in descending order (most recent policy listed first). The page number and page size
        parameters are optional. When the values are not specified the default values are 1 and 10 respectively.
        The maximum page size that can be specified is 200 entries per page.'''

        url = '%s/threats/v2' % self.url
        headers = {"Accept": "application/json; charset=utf-8", "Authorization": "Bearer %s " % self._token}
        data = {'page': page, 'page_size': page_size}
        resp = requests.get(url, headers=headers, params=data)
        return resp

    def get_threat_device(self,  hash256, page=None, page_size=None):
        '''Request threat details for a specific threat.'''

        url = '%s/threats/v2/%s/devices' % (self.url, hash256)
        headers = {"Accept": "application/json; charset=utf-8", "Authorization": "Bearer %s " % self._token}
        data = {'page': page, 'page_size': page_size}
        resp = requests.get(url, headers=headers, params=data)
        return resp

    def get_threat_download_url(self,  hash256):
        '''Request a download link for a given file. Use the download link to download the file.'''

        url = '%s/threats/v2/%s' % (self.url, hash256)
        headers = {"Accept": "application/json; charset=utf-8", "Authorization": "Bearer %s " % self._token}
        resp = requests.get(url, headers=headers)
        return resp
