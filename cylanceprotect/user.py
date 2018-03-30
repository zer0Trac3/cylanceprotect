import requests
import logging


class Users(object):
    '''The User API for Cylance Protect.'''
    __module__ = 'cylanceprotect'

    def __init__(self, token=None, url=None):
        self._token = token
        self.url = url

    def create_user(self, email, user_role, first_name, last_name, zones=[]):
        url = '%s/users/v2' % self.url
        headers = {"Accept": "application/json; charset=utf-8", "Content-Type": "application/json",
                   "Authorization": "Bearer %s " % self._token}
        data = {'email': email, "user_role": user_role, "first_name": first_name, "last_name": last_name,
                "zones": [zones]}
        resp = requests.post(url, data=data, headers=headers)
        return resp

    def get_users(self, page=None, page_size=None):
        url = '%s/users/v2' % self.url
        headers = {"Accept": "application/json; charset=utf-8", "Authorization": "Bearer %s " % self._token}
        data = {'page': page, 'page_size': page_size}
        resp = requests.get(url, headers=headers, params=data)
        return resp

    def get_user(self, user_id=None, email=None):
        url = '%s/users/v2' % self.url
        headers = {"Accept": "application/json; charset=utf-8", "Authorization": "Bearer %s " % self._token}
        if None in user_id and None in email:
            logging.error(msg="You must select one of the other")
        elif bool(user_id) is True and bool(email) is True:
            logging.error(msg="You must select only one type user_id or email")
        elif bool(user_id) is True:
            url = url + "/%s" % user_id
            resp = requests.get(url, headers=headers)
            return resp
        else:
            url = url + "/%s" % email
            resp = requests.get(url, headers=headers)
            return resp

    def update_user(self, user_id, email, user_role, first_name, last_name, zones=[]):
        url = '%s/users/v2/%s' % (self.url, user_id)
        headers = {"Accept": "application/json; charset=utf-8", "Content-Type": "application/json",
                   "Authorization": "Bearer %s " % self._token}
        data = {'email': email, "user_role": user_role, "first_name": first_name, "last_name": last_name,
                "zones": [zones]}
        resp = requests.put(url, data=data, headers=headers)
        return resp

    def delete_user(self, user_id):
        url = '%s/users/v2/%s' % (self.url, user_id)
        headers = {"Authorization": "Bearer %s " % self._token}
        resp = requests.delete(url, headers=headers)
        return resp

    def send_invite_email(self, email):
        url = '%s/users/v2/%s/invite' % (self.url, email)
        headers = {"Authorization": "Bearer %s " % self._token}
        resp = requests.post(url, headers=headers)
        return resp

    def send_reset_password_email(self, email):
        url = '%s/users/v2/%s/resetpassword' % (self.url, email)
        headers = {"Authorization": "Bearer %s " % self._token}
        resp = requests.post(url, headers=headers)
        return resp
