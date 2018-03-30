# CylanceProtect API

This is a python wrapper class for the CylanceProtect API v2.0

## API Test

Not all of the API function were tested during development

### Validated and Tested
* Authentication
* Threat

### Not Tested
* Device API
* Global List API
* Policy
* User
* Zone

## How to Use
1. Install package
* `python setup install`
* `pip install cylanceprotect`
* `from cylanceprotect import CylanceProtectApi`
* `appId = '0000000-0000-0000-0000-00000000000'`
* `appSecret = '0000000-0000-0000-0000-00000000000'`
* `tenantId = '0000000-0000-0000-0000-00000000000'`
* `regionCode = 'euc1' # Note look at region code in documentation`
* `cp = CylanceProtectApi(app_id=appId, app_secret=appSecret, tid_vad=tenantId region_code=regionCode)`
* `threat = cp.threat.get_threats(page=1, page_size=20)`
* `print(threat.text)`

## Supported Info

### Dependencies 
requests
PyJWT

### Python Supported Version
* Python 3.x