from pystyle import *

print(Box.Lines("[+] Learn Pyhton With Muhammed [+]"))
Write.Print("[-] This Programe For simple Calcaulter [-] \n", Colors.blue_to_cyan, 0.1)
print(Box.DoubleCube("Example 3"))
while True:
    number = int(Write.Input("[+] Write Your number : ", Colors.blue_to_purple, 0.1))
    for i in range(1, 11):
        print(number, "X", i, "= ", number * i)
    #break