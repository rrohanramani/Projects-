import json
from urllib.request import urlopen

with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
    source = response.read()

data = json.loads(source)
usd_rates = dict()

for item in data['list']['resources']:
    name = item.get('resource').get('fields').get('name')
    price = item.get('resource').get('fields').get('price')
    usd_rates[name] = price


def get_in_terms_of_usd(currency) :
    return usd_rates[currency]


def add_us (currency) :
    return "USD/" + currency

# Currency 1 is the currency we wish to translate
# Currency 2 is the currency we want to translate it too
# Amount is the amount of currency 1 you want to translate, default set to 1


def currency_converter (currency1, currency2, amount=1) :
    if currency1 == "USD" and currency2 == "USD" :
        return amount
    elif currency1 == "USD" :
        return float(get_in_terms_of_usd(add_us(currency2))) * amount
    elif currency2 == "USD" :
        a = float(get_in_terms_of_usd(add_us(currency1)))
        b = 1/a
        return b * amount
    conversion = (float(get_in_terms_of_usd(add_us(currency2))) / float(get_in_terms_of_usd(add_us(currency1)))) * amount
    return conversion
