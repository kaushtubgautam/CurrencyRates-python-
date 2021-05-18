#By @kaushtubgautam
#1$ to Inr rupee 
from forex_python.converter import CurrencyRates
c=CurrencyRates()
x=1
r=c.convert("USD" , "INR" , x)
print(x, "dollar =",r,"rupee")