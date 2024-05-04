from pystyle import *
from forex_python.converter import CurrencyRates

print(Box.Lines("[+] Learn Python With Muhammed  [+]"))
Write.Print("This Programe For Convert Money\n", Colors.blue_to_red, 0.1)
print(Box.DoubleCube("Example B"))
cr = CurrencyRates()
money = int(input("Please Enter Amount You Want Convert : "))
cv_from = input("Money Country 1 : ").upper()
cv_to = input("Money Country 2 : ").upper()
print ("You Are Converting ", money, cv_from, "To", cv_to)
output = cr.convert(cv_from, cv_to, money)
print("The Converted Rate Is : ", output)