import requests
from requests import Session, Request


class DependencyTrackClient:
    def __init__(self, url, api_key):
        self.url = url.strip('/')
        self.api_key = api_key
        self.headers = {
            "X-Api-Key": api_key,
            "accept": "application/json"
        }
        self.client = requests.Session()
        self.client.headers.update(self.headers)

    def get_projects_by_name(self, project_name):
        params = {'name': project_name}
        return self.client.get(f"{self.url}/api/v1/project", params=params).json()

    def create_project(self, project_name, version, sbom_file):
        data = {
            "autoCreate": "true",
            "projectName": project_name,
            "projectVersion": version,
            "bom": open(sbom_file, 'rb')
        }
        request = Request("POST", f"{self.url}/api/v1/bom", headers=self.headers, files=data).prepare()
        session = Session()
        return session.send(request)

    def tag_project(self, project_name, version, tags, description):
        params = {'name': project_name, 'version': version}
        project = self.client.get(f"{self.url}/api/v1/project/lookup", params=params).json()
        project["tags"] = tags
        if description:
            project["description"] = description
        return self.client.post(f"{self.url}/api/v1/project", json=project)
