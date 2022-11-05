import booking.constants as const
import os
from selenium import webdriver
from selenium.webdriver.common.by import By


class Booking(webdriver.Chrome):
	def __init__(self, driver_path="C:/SeleniumDrivers", teardown=False):
		self.driver_path = driver_path
		self.teardown = teardown
		os.environ["PATH"] = self.driver_path
		super(Booking, self).__init__()
		self.implicitly_wait(30)
		self.maximize_window()

	def __exit__(self, exc_type, exc_val, exc_tb):
		if self.teardown:
			self.quit()

	def land_first_page(self):
		self.get(const.BASE_URL)

	def change_currency(self, currency=None):
		currency_element = self.find_element(By.CSS_SELECTOR, "button[data-tooltip-text='Choose your currency']")
		currency_element.click()
		selected_currency_element = self.find_element(By.CSS_SELECTOR, f"a[data-modal-header-async-url-param*='selected_currency={currency}']")
		selected_currency_element.click()

	def select_place_to_go(self, place_to_go=None):
		search_field = self.find_element(By.NAME, "ss")
		search_field.clear()
		search_field.send_keys(place_to_go)

		first_result = self.find_element(By.CSS_SELECTOR, "li[data-i='0']")
		first_result.click()

	def select_dates(self, check_in_date, check_out_date):
		check_in_element = self.find_element(By.CSS_SELECTOR, f"td[data-date='{check_in_date}']")
		check_in_element.click()
		check_out_element = self.find_element(By.CSS_SELECTOR, f"td[data-date='{check_out_date}']")
		check_out_element.click()

	def select_adult(self, count=1):
		selection_element = self.find_element(By.ID, "xp__guests__toggle")
		selection_element.click()

		while True:
			decrease_adult_element = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Decrease number of Adults"]')
			decrease_adult_element.click()
			adult_value_element = self.find_element(By.ID, "group_adults")
			adult_value = adult_value_element.get_attribute("value")

			if int(adult_value) == 1:
				break

			print(adult_value)

		increase_adult_element = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Increase number of Adults"]')
		for _ in range(count-1):
			increase_adult_element.click()

	def click_search(self):
		search_button = self.find_element(By.CSS_SELECTOR, "button[type='search']")
		search_button.click()