from booking.booking import Booking


with Booking() as bot:
	bot.land_first_page()
	# bot.change_currency("GHS")
	bot.select_place_to_go("New York")
	bot.select_dates(check_in_date='2022-11-07', check_out_date='2022-11-14')
	bot.select_adult(3)
	bot.click_search()
