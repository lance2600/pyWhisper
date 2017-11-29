import requests





class TextSecureAPI:

    def api_send(self,api_url, uri,payload,basicauth=auth):
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        req = requests.put(api_url + '/'+ uri, auth=HTTPBasicAuth(basicauth[username],basicauth[password]), json=payload,headers=headers, verify=False)
        return {"status":req.status_code,"content":req.text}




