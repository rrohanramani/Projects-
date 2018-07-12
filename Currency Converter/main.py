import funcs
# This is the main file where we get user input
currency1 = input("What is the currency that you would like to convert?: ")
currency2 = input("What is the currency that you would like to have the money converted to?: ")
amount = input("How may " + currency1 + " would you like to convert?: ")
rough_conversion = funcs.currency_converter(currency1, currency2, float(amount))
print ("The rough conversion is " + str(rough_conversion))