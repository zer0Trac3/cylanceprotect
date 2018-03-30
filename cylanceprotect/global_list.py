import requests
import logging


class GlobalList(object):
    '''The Global List API for Cylance Protect.'''
    __module__ = 'cylanceprotect'

    def __init__(self, token=None, url=None):
        self._token = token
        self.url = url

    def get_global_list(self, list_type_id, page=None, page_size=None):
        '''Allows a caller to request a page with a list of global list resources for a Tenant, sorted by the date when
        the hash was added to the Global List, in descending order (most recent policy listed first). The page number
        and page size parameters are optional. When the values are not specified, these default to 1 and 10
        respectively. The maximum page size that can be specified is 200 entries per page. The listTypeId parameter is
        required and can be either 0 (GlobalQuarantine) or 1 (GlobalSafe).'''

        url = '%s/globallists/v2' % self.url
        headers = {"Accept": "application/json; charset=utf-8", "Authorization": "Bearer %s " % self._token}
        data = {'listTypeId': list_type_id, 'page': page, 'page_size': page_size}
        resp = requests.get(url, headers=headers, params=data)
        return resp

    def add_to_global_list(self, sha256, list_type, reason, category=None):
        '''Allows a caller to add a convicted threat to either the Global Quarantine or the Global Safe list for a
        particular Tenant.

        category = Only required if using Global Safe in list_type
            Only allowed field (Admin Tool, Commerical Software, Drivers, Internal Application, Operating System,
            Security Software, None

        list_type = GlobalQuarantine or GlobalSafe
        '''

        url = '%s/globallists/v2/'
        headers = {"Accept": "application/json; charset=utf-8", "Content-Type": "application/json",
                   "Authorization": "Bearer %s " % self._token}
        if list_type is "GlobalSafe" and category is None:
            logging.error("If using GlobalSafe. You must use a category")
        else:
            data = {"sha256": sha256, "list_type": list_type, "category": category, "reason": reason}

            resp = requests.post(url, headers=headers, data=data)
            return resp

    def delete_from_global_list(self, sha256, list_type):
        '''Allows a caller to remove a convicted threat from either the Global Quarantine or the Global Safe list for a
        particular Tenant.

        list_type = GlobalQuarantine or GlobalSafe

        '''

        url = '%s/globallists/v2/'
        headers = {"Accept": "application/json; charset=utf-8", "Content-Type": "application/json",
                   "Authorization": "Bearer %s " % self._token}
        data = {"sha256": sha256, "list_type": list_type}
        resp = requests.delete(url, headers=headers, data=data)
        return resp
