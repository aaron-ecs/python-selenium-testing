from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


class GooglePage:
    def __init__(self, driver):
        self.driver = driver

    def search(self, search_term):
        return self.driver.find_element_by_name('q').send_keys(search_term + Keys.ENTER)

    def check_results(self):
        WebDriverWait(self.driver, 5).until(
            lambda driver: self.driver.find_elements_by_class_name("r"))
        results = self.driver.find_elements_by_class_name("r")
        all_results = []
        for result in results[:2]:
            all_results.append(result.find_element_by_tag_name("a").get_attribute("href"))
        return all_results
