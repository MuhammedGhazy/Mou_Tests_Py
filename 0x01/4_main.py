from pystyle import *
import speedtest
print(Box.Lines("[+] Learn Python With Muhammed  [+]"))
Write.Print("This Programe For Speed Net \n", Colors.blue_to_red, 0.1)
print(Box.DoubleCube("Example 5"))
st = speedtest.Speedtest()
dst = st.download()
d = round(dst / (10 ** 6), 2)
ust = st.upload()
u = round(ust / (10 ** 6), 2)
#print(dst)
#print(ust)
Write.Print("[-] Net Speed is : \n", Colors.red_to_yellow, 0.1)
print("Your Download Speed Is : ", d , "MB \n")
print("Your Upload Speed Is : ", u, "MB \n")
input("press any key to exit...")