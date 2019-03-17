# Configuration file
from configuration import User_Settings
import main
import json

list_of_all_environments = {
    'Production': 'https://endpointclosing.com',
    'Staging': 'https://google.com',
    'Dev': 'None'
}

users_info_json = open(main.base_directory + '/configuration/users.json')
users_info = json.load(users_info_json)
users_info_json.close()


class Config:
    def __init__(self):
        self.base_url = list_of_all_environments[User_Settings.EnvToRunTestsOn]
        self.browser = User_Settings.WebDriverBrowser
        self.credentials = users_info
