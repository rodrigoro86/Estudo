import requests
import json
import sys


class PODMAN():
    def __init__(self) -> None:
        self.service = "http://localhost:8080/v1.40.0/libpod"
    
    """def _get_comand(self, comando):
        url = f"{self.service}/{comando}"
        response = requests.get(url)
        jsonresponse = json.loads(response.text)
        return jsonresponse"""
    
    def _get_command(self, comando, parametro):
        url = f"{self.service}/{comando}"
        headers = {'Content-type': 'application/json'}
        response = requests.request("GET", url, headers=headers, params=parametro)
        jsonresponse = json.loads(response.text)
        return jsonresponse

    def _post_comand(self, comando, parametros):
        url = f"{self.service}/{comando}"
        headers = {'Content-type': 'application/json'}
        response = requests.request("POST", url, headers=headers, params=parametros)
        jsonresponse = json.loads(response.text)
        return jsonresponse
    
    def podman_pull(self):
        payload = {'reference':'fedora'}
        self._post_comand('images/pull', payload)
    
    def list_images(self):
        list_images = self._get_comand('images/json')

        for imagem in list_images:
            print(imagem['Id'])
            print(imagem['Names'])
            print(imagem)

    def list_containers(self):
        
        list_containers = self._get_command('containers/json', {'pod':True})
        for container in list_containers:
            print(container)
            print("#"*100)

pod = PODMAN()
print(pod.list_containers())    

