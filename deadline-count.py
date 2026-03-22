## this is a deadline counter application

import datetime


user_input = input("enter your goal with the dead line spearated by colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = (datetime.datetime.strptime(deadline,"%d.%m.%Y"))
todays_date = (datetime.datetime.today())
# calculation of the deadline from today to how many days from today
time_remain = deadline_date - todays_date
print(f"dear user your time remaining for the deadline of {goal} is {time_remain.days} days")
