# Class with base methods that are inherited and reused across the Framework
from configuration.config import Config
config = Config()


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.base_url = config.base_url

    def go(self, url):
        self.driver.get(self.base_url + url)
        return None

    @property
    def get_current_url(self):
        return self.driver.current_url
