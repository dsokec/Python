def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        # print("Leap year.")
        return True
      else:
        # print("Not leap year.")
        return False
    else:
      # print("Leap year.")
      return True
  else:
    # print("Not leap year.")
    return False

def days_in_month(userYear, userMonth):
    if userMonth > 12 or userMonth < 1:
        return "Invalid Input!"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(userYear) == True and userMonth == 2:
        return 29
    return month_days[userMonth - 1]
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)







