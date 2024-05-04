from pystyle import *
print(Box.Lines("[+] Learn Python With Muhammed  [+]"))
Write.Print("This Programe For Calculating Student Grades \n", Colors.blue_to_red, 0.1)
print(Box.DoubleCube("Example 9"))
name = input("Write Your Name : ")
Write.Print("Welcome : ", Colors.green, 0.2)
print(name)
Write.Print("[-] Write Your Grades Now : \n", Colors.green_to_blue, 0.2)
math = float (input("Write Math Grade : "))
arabic = float(input("Write Your Arabic Grade : "))
english = float(input("Write Your English Grade : "))
sport = float(input("Write Your Sport Grade : "))
final_grade = {
    "math" : math,
    "arabic" : arabic,
     "english" : english,
     "sport" : sport,
}
for k, v in final_grade.items() :
    print(k, v)
    final = math + arabic + english + sport
if final > 60 :
    Write.Print("Your Final Grade Is : ", Colors.blue_to_purple, 0.2)
    print(final)
    Write.Print("[+] You are successful... ", Colors.blue_to_purple, 0.2)
elif final < 60 :
    Write.Print("[-] Lazy Student", Colors.red_to_blue, 0.2)


