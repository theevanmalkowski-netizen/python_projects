hoursworked = float(input("How many hours did you work? "))
wage = float(input("What is your hourly wage? "))
tax = float(input("What percent was taken out for Connecticut tax/withholding? "))
overtime = input("Did you work overtime? ")

gross_pay = hoursworked * wage
withholding = gross_pay * (tax / 100)
take_home = gross_pay - withholding

print("Hours worked:", hoursworked)
print("Hourly wage:", wage)
print("Gross pay:", gross_pay)
print("Estimated withholding:", withholding)
print("Estimated take-home pay:", take_home)
