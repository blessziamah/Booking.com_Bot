from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BookingFiltration:
	def __init__(self, driver: WebDriver):
		self.driver = driver

	def apply_star_rating(self, *star_values):
		star_filter_box = self.driver.find_element(By.ID, "filter-class")
		star_child_element = star_filter_box.find_elements(By.CSS_SELECTOR, "*")

		for star_value in star_values:
			for star_element in star_child_element:
				if str(star_element.get_attribute("innerHTML")).strip() == f"{star_value} stars":
					star_element.click()

	def sort_price_lowest_first(self):
		element = self.driver.find_element(By.CSS_SELECTOR, "li[data-id='price']")
		element.click()
