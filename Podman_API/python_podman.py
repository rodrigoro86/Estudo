import requests
import json
import sys
import pandas as pd
import socket

class PODMAN():
    def __init__(self) -> None:
        self.service = "http://localhost:8080/v1.40.0/libpod"
    
    """def _get_comand(self, comando):
        url = f"{self.service}/{comando}"
        response = requests.get(url)
        jsonresponse = json.loads(response.text)
        return jsonresponse"""
    
    def _get_command(self, comando, parametro=None):
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

    def list_containers(self, all_containers=False):
        list_containers = self._get_command('containers/json', {'all':all_containers})
        pd_containers = pd.DataFrame.from_dict(list_containers)
        return pd_containers

    def status_container(self):
        list_status = self._get_command('containers/stats', {'stream':False})
        pd_status = pd.DataFrame(list_status['Stats'])
        return pd_status

    def logs_container(self, container):
        url = f"{self.service}/containers/{container}/logs"
        headers = {'Content-type': 'application/json'}
        response = requests.request("GET", url, headers=headers, params={'since':'2017-08-07T10:10:09.055837383-04:00'})
        print(str(response.text))


pod = PODMAN()
#print(pod.list_containers(all_containers=True))    
#print(pod.status_container())
print(pod.logs_container('hopeful_blackwell'))
