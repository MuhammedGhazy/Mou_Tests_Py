import time
from pystyle import *
from tqdm import tqdm

print(Box.Lines("[+] Learn Python With Muhammed  [+]"))
Write.Print("This Programe For Progress Par \n", Colors.blue_to_red, 0.1)
print(Box.DoubleCube("Example A"))
with tqdm(total = 100) as pbar:
    for i in range(100):
        time.sleep(0.1)
        pbar.update(1)
print("Finish And Fetched Data\n")        
input("press any key to exit....")