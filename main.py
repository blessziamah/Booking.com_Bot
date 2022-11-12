from booking.booking import Booking


with Booking() as bot:
	bot.land_first_page()
	bot.change_currency("GHS")
	bot.select_place_to_go(input("Where's your destination? "))
	bot.select_dates(check_in_date=input("Checkin date? "), check_out_date=input("Checkout date? "))
	bot.select_adult(int(input("Enter number of people: ")))
	bot.click_search()
	bot.apply_filtration()
	bot.refresh()
	bot.report_results()
