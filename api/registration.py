#!/usr/bin/python3
import requests
import base64
from requests.auth import HTTPBasicAuth
import hashlib
import sys
import ciphers
import json


api_url = 'https://textsecure-service.whispersystems.org'
confirmkeys = ciphers.CryptoGen()

class WhisperRegister:




    def request_code(self,number):

        r = requests.get(api_url+'/v1/accounts/sms/code/'+number,verify=False)
        return r.text

    def verify_code(self,verfication_code, phone, password):
        payload = confirmkeys.gen_sig_key()
        password = hashlib.sha256(password.encode()).hexdigest()[0:16]
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        r = requests.put(api_url+'/v1/accounts/code/'+verfication_code, auth=HTTPBasicAuth(phone, password), json=payload,headers=headers,verify=False)
        print(r,r.headers,r.status_code,r.content,r.url,r.json(),r.text)


def main():
    number = "+17602624141"
    register = WhisperRegister()
    #register.request_code(number)
    register.verify_code('828-119',number,"p@ssw0rd!@#")
main()