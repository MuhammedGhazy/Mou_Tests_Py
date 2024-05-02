from pystyle import *

print(Box.Lines("[+] Learn Python With Muhammed [+]"))
Write.Print("[+] This programe for login page [+]\n", Colors.blue_to_purple, 0.1)
Write.Print("[+] Write User Name And Password [+]\n\n", Colors.blue_to_purple, 0.1)
print(Box.DoubleCube("Example [1]"))

while True:
    username = Write.Input("Write User Name : ", Colors.blue_to_green, 0.1)
    password = Write.Input("Wite Password : ", Colors.blue_to_green, 0.1)
    if username == 'Muhammed' and password == '1234567':
        Write.Print("[+] Welcome Admim [+] \n", Colors.cyan_to_blue, 0.1)
        input("press any key to exit...")
        exit()
    else:
        Write.Print("[-] Error Try Again [-]\n", Colors.red_to_blue, 0.1)

