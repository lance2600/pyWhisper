from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Hash import SHA, SHA256, HMAC
import base64
import json
import uuid

digits = uuid.uuid4().int & (1<<14)-1
static_keys = {'aespass': b'testkey1234567890!@#', 'sha1pass': b'testkey987654321!@#', 'regid':digits}

class CryptoGen:


    def gen_sig_key(self):
        true = 'false'
        sha2 = SHA256.new()
        sha2.update(static_keys['aespass'])
        aeskey = sha2.hexdigest()
        mac = HMAC.new(static_keys['sha1pass'], digestmod=SHA)
        hmac_key = mac.hexdigest()
        sig_key_hex = aeskey+hmac_key
        sig_key_b64 = (base64.b64encode(str(sig_key_hex).encode()))
        payload = {'signalingKey':sig_key_b64.decode(),
                      'supportsSms':False, 'registrationId':static_keys['regid']}
        return payload
