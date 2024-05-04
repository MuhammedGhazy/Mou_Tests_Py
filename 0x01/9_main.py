import datetime
from pystyle import *
print(Box.Lines("[+] Learn Python With Muhammed  [+]"))
Write.Print("This Programe For Count Age \n", Colors.blue_to_red, 0.1)
print(Box.DoubleCube("Example 10"))
now_date = datetime.datetime.now()
#print(now_date)
birth_day = Write.Input("Enter Your Year Of Birth Day : ", Colors.blue_to_purple, 0.1)
year = now_date.year
get = year - int(birth_day)
Write.Print("[+] Your Age Is : ", Colors.cyan_to_green, 0.2)
print(get, "\n")
Write.Input("Press Any Key To Exit...", Colors.green_to_white, 0.1)
