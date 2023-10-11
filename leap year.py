def check_leap_year(year):
  """
    Check if the given year is a leap year or not.
    """
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        print(f"{year} is a leap year")
      else:
        print(f"{year} is not a leap year")
    else:
      print(f"{year} is a leap year")
  else:
    print(f"{year} is not a leap year")


check_leap_year(2000)  # This 2000 is a leap year
check_leap_year(2016)  # This 2016 is a leap year
check_leap_year(2100)  # This 2100 is not a leap year
