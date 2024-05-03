from pystyle import *
import pyshorteners as short 

print(Box.Lines("[+] Learn Python With Muhammed  [+]"))
Write.Print("This Programe For Short Urls \n", Colors.blue_to_red, 0.1)
print(Box.DoubleCube("Example 4"))
url = Write.Input("[+] Please Insert Url For Short : ", Colors.blue_to_green, 0.2)
S_hort = short.Shortener()
Write.Print(S_hort.tinyurl.short(url), Colors.blue_to_green, 0.1)
print('\n')
input("press any key to exit...")