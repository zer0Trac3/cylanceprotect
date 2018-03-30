from cylanceprotect.threat import Threats
from cylanceprotect.user import Users
from cylanceprotect.device import Devices
from cylanceprotect.global_list import GlobalList
from cylanceprotect.policy import Policy
from cylanceprotect.zone import Zone
import json
import requests
import jwt
from datetime import datetime, timedelta
import uuid
import logging

class CylanceProtectApi(object):

    def __init__(self, app_id, app_secret, tid_vad, region_code, timeout=1800, scp=None):
        ''' The initial set paramemters
        app_id is the application's unique identifier
        app_secret  is the applicaiton secret to sign the auth token with
        tid_vad is the Tenat's unique identifier
        region_code is also required (review documentation for further info on region code)
        '''
        self._appId = app_id
        self._appSecret = app_secret
        self._tidVad = tid_vad
        self._regionCode = region_code
        self.timeout = timeout
        self.scp = scp
        self.url = 'https://protectapi.%s.cylance.com' % region_code
        self._token = self.authentication_token()
        self.threat = Threats(self._token, self.url)
        self.user = Users(self._token, self.url)
        self.device = Devices(self._token, self.url)
        self.global_list = GlobalList(self._token, self.url)
        self.policy = Policy(self._token, self.url)
        self.zone = Zone(self._token, self.url)

    def authentication_token(self):
        ''' Authentication Token contains the ID of the Application to which a client system is requesting access.
        The Application contains two attributes: Application ID and Application Secret, the latter is cryptographic
        nonce used to sign the token, thus ensuring the authenticity of the caller and therefore, it must be shared
        between client and server.

        The key is valid for no more than 30 min.
        '''

        auth_url = self.url + "/auth/v2/token"
        jti_val = str(uuid.uuid4())

        # Setup the time based timeout
        if self.timeout <= 1800:
            now = datetime.utcnow()
            timeout_datetime = now + timedelta(seconds=self.timeout)
            epoch_time = int((now - datetime(1970, 1, 1)).total_seconds())
            epoch_timeout = int((timeout_datetime - datetime(1970, 1, 1)).total_seconds())

            # Create the package
            data = {
                "exp": epoch_timeout,
                "iat": epoch_time,
                "iss": "http://cylance.com",
                "sub": self._appId,
                "tid": self._tidVad,
                "jti": jti_val,
            }
            if self.scp is not None:
                # ToDo: Test for invalid SCP
                data['scp'] = self.scp
            encoded = jwt.encode(data, self._appSecret, algorithm='HS256')
            payload = {"auth_token": encoded.decode('utf-8')}
            headers = {"Content-Type": "application/json; charset=utf-8"}
            resp = requests.post(auth_url, headers=headers, data=json.dumps(payload))
            return json.loads(resp.text)['access_token']
        else:
            logging.error("Your time must be 30 min or less")
