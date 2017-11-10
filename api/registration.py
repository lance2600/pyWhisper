#!/usr/bin/python3
import requests
import base64
from requests.auth import HTTPBasicAuth
import hashlib



api_url = 'https://textsecure-service.whispersystems.org'

class WhisperRegister:




    def request_code(self,number):

        r = requests.get(api_url+'/v1/accounts/sms/code/'+number,verify=False)
        return r.text

    def verify_code(self,verfication_code, phone, password):
        password = hashlib.sha256(password.encode()).hexdigest()[0:16]
        r = requests.put(api_url+'/v1/accounts/code/', auth=HTTPBasicAuth(phone, password), data=payload)

        payload = {
            "signalingKey" : "{base64_encoded_52_byte_key}", #signalingKey is a randomly generated 32 byte AES key and a 20 byte HMAC-SHA1 MAC key, concatenated together and Base64 encoded.
            "supportsSms" : true, #supportsSms indicates whether a client supports SMS as a transport.
            "registrationId" : "{14-bit number}" #registrationId is a 14 bit integer that's randomly generated at client install time. This will be used for clients to detect whether an app has reinstalled and lost their session state.
        }


