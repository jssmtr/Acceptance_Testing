from tests.acceptance.locators.home_page import HomePageLocators
from tests.acceptance.page_model.base_page import BasePage


class HomePage(BasePage):

    @property #En una clase, si le pones este decorador a una clase que no requiera argumentos. La puedes llamar sin los ()
    def url(self):
        return super(HomePage, self).url + '/'

    @property
    def blog_link(self):
        return self.driver.find_element(*HomePageLocators.NAVIGATION_LINK)