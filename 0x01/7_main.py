from pystyle import *
import emoji
import random

print(Box.Lines("[+] Learn Python With Muhammed  [+]"))
Write.Print("This Programe For Chat With Emoji \n", Colors.blue_to_red, 0.1)
print(Box.DoubleCube("Example 8"))
Write.Print("[-] You can use only 'hello, or, whats your name'\n", Colors.blue_to_cyan, 0.1)
e1 = emoji.emojize(":red_heart:")
e2 = emoji.emojize(":yellow_heart:")
e3 = emoji.emojize(":purple_heart:")
e4 = emoji.emojize(":white_heart:")
e5 = emoji.emojize(":green_heart:")
emj = [e1, e2, e3, e4, e5]
hi = ["Welcome", "Hello", "Hey", "Welcome Dear"]
name = ["Muhammed", "Mou", "Molto", "Mody_Ghazy"]
while True:
    chat = input("Enter Your Message : ")
    if chat == 'hello' :
        answer = random.choice(hi)
        emj_answer = random.choice(emj)
        print(answer + " " + emj_answer)
    elif chat == "whats your name" :
        answer = random.choice(name)
        emj_answer = random.choice(emj)
        print(answer + " " + emj_answer)  
    else:
        print(emoji.emojize("Sorry Try Again :broken_heart:"))      