from pystyle import *

print(Box.Lines("[+] Learn Python With Muhammed [+]"))
Write.Print("This App For Calculater\n", Colors.light_green, 0.1)
print(Box.DoubleCube("Example 2\n"))
while True:
    number1 = int(Write.Input("Write First Number\n", Colors.yellow_to_green, 0.1))
    operator = Write.Input("Please Enter Operator\n", Colors.yellow_to_green, 0.1)
    number2 = int(Write.Input("Write Seconde Number\n", Colors.yellow_to_green, 0.1))
    if operator == '+':
        Write.Print("[+] The Resault is =  ", Colors.green, 0.1)
        print(number1 + number2)
        break
    elif operator == '-': 
        Write.Print("[+] The Resault is =  ", Colors.green, 0.1)
        print(number1 - number2)
        break

    elif operator == '*': 
        Write.Print("[+] The Resault is =  ", Colors.green, 0.1)
        print(number1 * number2)
        break
    elif operator == '/': 
        Write.Print("[+] The Resault is =  ", Colors.green, 0.1)
        print(number1 / number2)
        break
    else:
        Write.Print("\n[-] Please Enter Only This Operator [+ - * /] \n", Colors.red, 0.1)


