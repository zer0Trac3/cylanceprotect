import requests

class Policy(object):
    '''The Policy API for Cylance Protect.'''
    __module__ = 'cylanceprotect'

    def __init__(self, token=None, url=None):
        self._token = token
        self.url = url

    def get_policy(self, policy_id):
        '''Allows the caller to get details for a single policy.'''

        url = '%s/policies/v2' % self.url
        headers = {"Accept": "application/json; charset=utf-8", "Authorization": "Bearer %s " % self._token}
        resp = requests.get(url, headers=headers)
        return resp

    def get_policies(self, policy_id, page=None, page_size=None):
        '''Allows the caller to get a list of Tenant policies where the Tenant ID is retrieved from the JWT token
        provided in the request.'''
        url = '%s/policies/v2' % self.url
        data= {'page': page, 'page_size': page_size}
        headers = {"Accept": "application/json; charset=utf-8", "Authorization": "Bearer %s " % self._token}
        resp = requests.get(url, headers=headers, params=data)
        return resp


    def create_policy(self, user_id, conf_control_mode, conf_device_class, ex_list_control_mode, ex_list_product_id,
                      ex_list_serial_number, ex_list_vendor_id, file_ex_file_hash, file_ex_md5, file_ex_file_name,
                      file_ex_category_id, file_ex_reason, mem_violations_action, mem_violations_violation_type,
                      mem_violation_ext_action, mem_violation_ext_violation_type, policy_name, policy_value,
                      pn_policy_name, pn_control_mode, gs_control_mode, ms_control_mode, ps_console_mode,
                      ps_control_mode, sf_actions, sf_file_type, tf_actions, tf_file_type, lp_log_upload, lp_maxlogsize,
                      lp_retentiondays):
        '''Allows the caller to create a policy.'''
        url = '%s/policies/v2' % self.url
        data = {
            "user_id" : user_id, "policy" :
                { "device_control":
                      { "configurations":
                            [
                                {
                                    "control_mode": conf_control_mode,
                                    "device_class": conf_device_class
                                }
                            ],
                          "exclusion_list":
                              [
                                  {
                                      "control_mode": ex_list_control_mode,
                                      "product_id": ex_list_product_id,
                                      "serial_number": ex_list_serial_number,
                                      "vendor_id": ex_list_vendor_id
                                  }
                              ]
                      },
                    "file_exclusions":
                        [
                            {
                                "file_hash": file_ex_file_hash,
                                "md5": file_ex_md5,
                                "file_name": file_ex_file_name,
                                "category_id": file_ex_category_id,
                                "reason": file_ex_reason
                            }
                        ],
                    "memoryviolation_actions":
                        {
                            "memory_violations":
                                [
                                    {
                                        "action": mem_violations_action,
                                        "violation_type": mem_violations_violation_type
                                    }
                                ],
                            "memory_violations_ext":
                                [
                                    {"action": mem_violation_ext_action,
                                     "violation_type": mem_violation_ext_violation_type
                                     }
                                ],
                            "memory_exclusion_list": "[]" },
                    "policy":
                        [
                            {
                                "name": policy_name,
                                "value": policy_value
                            }
                        ],
                    "policy_name": pn_policy_name,
                    "script_control":
                        {
                            "activescript_settings":
                                {
                                    "control_mode": pn_control_mode
                                },
                            "global_settings": {
                                "allowed_folders": "",
                                "control_mode": gs_control_mode
                            },
                            "macro_settings": {
                                "control_mode": ms_control_mode
                            },
                            "powershell_settings": {
                                "console_mode": ps_console_mode,
                                "control_mode": ps_control_mode
                            }
                        },
                    "filetype_actions":
                        {
                            "suspicious_files":
                                [
                                    {
                                        "actions": sf_actions,
                                        "file_type": sf_file_type
                                    }
                                ],
                            "threat_files": [
                                {
                                    "actions": tf_actions,
                                    "file_type": tf_file_type
                                }
                            ]
                        },
                    "logpolicy":
                        {
                            "log_upload": lp_log_upload,
                            "maxlogsize": lp_maxlogsize,
                            "retentiondays": lp_retentiondays
                        }
                }
        }
        headers = {"Content-Type": "application/json", "Authorization": "Bearer %s " % self._token}
        resp = requests.post(url, headers=headers, data=data)
        return resp


    def update_policy(self, user_id, conf_control_mode, conf_device_class, ex_list_control_mode, ex_list_product_id,
                      ex_list_serial_number, ex_list_vendor_id, file_ex_file_hash, file_ex_md5, file_ex_file_name,
                      file_ex_category_id, file_ex_reason, mem_violations_action, mem_violations_violation_type,
                      mem_violation_ext_action, mem_violation_ext_violation_type, policy_name, policy_value,
                      pn_policy_name, pn_control_mode, gs_control_mode, ms_control_mode, ps_console_mode,
                      ps_control_mode, sf_actions, sf_file_type, tf_actions, tf_file_type, lp_log_upload, lp_maxlogsize,
                      lp_retentiondays):
        '''Allows the caller to create a policy.'''
        url = '%s/policies/v2' % self.url
        data = {
            "user_id" : user_id, "policy" :
                { "device_control":
                      { "configurations":
                            [
                                {
                                    "control_mode": conf_control_mode,
                                    "device_class": conf_device_class
                                }
                            ],
                          "exclusion_list": [
                              {
                                  "control_mode": ex_list_control_mode,
                                  "product_id": ex_list_product_id,
                                  "serial_number": ex_list_serial_number,
                                  "vendor_id": ex_list_vendor_id
                              }
                          ]
                      },
                    "file_exclusions":
                        [
                            {
                                "file_hash": file_ex_file_hash,
                                "md5": file_ex_md5,
                                "file_name": file_ex_file_name,
                                "category_id": file_ex_category_id,
                                "reason": file_ex_reason
                            }
                        ],
                    "memoryviolation_actions":
                        {
                            "memory_violations":
                                [
                                    {
                                        "action": mem_violations_action,
                                        "violation_type": mem_violations_violation_type
                                    }
                                ],
                            "memory_violations_ext":
                                [
                                    {"action": mem_violation_ext_action,
                                     "violation_type": mem_violation_ext_violation_type
                                     }
                                ],
                            "memory_exclusion_list": "[]"},
                    "policy":
                        [
                            {
                                "name": policy_name,
                                "value": policy_value
                            }
                        ],
                    "policy_name": pn_policy_name,
                    "script_control":
                        {
                            "activescript_settings":
                                {
                                    "control_mode": pn_control_mode
                                },
                            "global_settings": {
                                "allowed_folders": "",
                                "control_mode": gs_control_mode
                            },
                            "macro_settings": {
                                "control_mode": ms_control_mode
                            },
                            "powershell_settings": {
                                "console_mode": ps_console_mode,
                                "control_mode": ps_control_mode
                            }
                        },
                    "filetype_actions":
                        {
                            "suspicious_files":
                                [
                                    {
                                        "actions": sf_actions,
                                        "file_type": sf_file_type
                                    }
                                ],
                            "threat_files": [
                                {
                                    "actions": tf_actions,
                                    "file_type": tf_file_type
                                }
                            ]
                        },
                    "logpolicy":
                        {
                            "log_upload": lp_log_upload,
                            "maxlogsize": lp_maxlogsize,
                            "retentiondays": lp_retentiondays
                        }
                }
        }
        headers = {"Content-Type": "application/json",
                   "Authorization": "Bearer %s " % self._token}
        resp = requests.put(url, headers=headers, data=data)
        return resp

    def delete_policy(self, policy_id):
        '''Delete a policy from the Console.'''

        url = '%s/policies/v2%s' % (self.url, policy_id)
        headers = { "Authorization": "Bearer %s " % self._token}
        resp = requests.delete(url, headers=headers)
        return resp

    def delete_policies(self, policies=[]):
        '''Delete multiple policies from the Console.'''

        url = '%s/policies/v2' % self.url
        headers = {"Authorization": "Bearer %s " % self._token}
        data = {"tenat_policy_ids": [policies]}
        resp = requests.delete(url, headers=headers, data=data)
        return resp
