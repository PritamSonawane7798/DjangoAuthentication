import requests 
  
class Currency_convertor: 
    # empty dict to store the conversion rates 
    rates = {}  
    def __init__(self, url): 
        data = requests.get(url).json() 
  
        # Extracting only the rates from the json data 
        self.rates = data["rates"]  
  
    # function to do a simple cross multiplication between  
    # the amount and the conversion rates 
    def convert(self, from_currency, to_currency, amount): 
        initial_amount = amount 
        if from_currency != 'EUR' : 
            amount = amount / self.rates[from_currency] 
  
        # limiting the precision to 2 decimal places 
        amount = round(amount * self.rates[to_currency], 2) 
        print('{} {} = {} {}'.format(initial_amount, from_currency, amount, to_currency)) 
  
# Driver code 
if __name__ == "__main__": 
  
    YOUR_ACCESS_KEY = 'cfce5fcfb8b0e8921d62b48e04fc40b2' 
    url = 'http://data.fixer.io/api/latest?access_key={}'.format(YOUR_ACCESS_KEY) 
    c = Currency_convertor(url) 
    from_country = input("From Country: ") 
    to_country = input("TO Country: ") 
    amount = int(input("Amount: ")) 
  
    c.convert(from_country, to_country, amount) 
# ##################################################
# From Country: USD 
# TO Country: INR 
# Amount: 1 
# #################################################
# 1 USD = 70.69 INR
# #################################################