from pystyle import *
from geopy.distance import geodesic

print(Box.Lines("[+] Learn Python With Muhammed  [+]"))
Write.Print("This Programe For Space Between Cities \n", Colors.blue_to_red, 0.1)
print(Box.DoubleCube("Example 6"))
Write.Print("[+] Space Between Cities is : \n", Colors.purple_to_red, 0.1)
first_place = (31.20194, 29.91611) #Alexandria
second_place = (27.17750, 31.18583) #Assiut
dis = int(geodesic(first_place, second_place).km)
print (dis, "kilo_Meters\n")
input("press any key to exit...")