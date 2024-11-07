from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        dict = toml.loads(content)

        dict_poetry=(dict['tool']['poetry'])
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(dict_poetry['name'], dict_poetry['description'], 
                       dict_poetry['license'], dict_poetry['authors'],
                       dict_poetry['dependencies'], dict_poetry['group']['dev']['dependencies'])