from secrets import token_hex
import random, string
from os import system
from time import sleep

txt = open("accounts.txt","a+",encoding="utf-8")
eng = ("").join(random.choices(string.ascii_letters + string.digits, k=3))
emz = f"A{eng}O{token_hex(3)}M"
pwz = f"{token_hex(6)}AOM"

txt.write(f"Email:{emz}@gmail.com - Passw:{pwz}\n")
print("-------------")
print("Email :"+emz)
input()
print("Passw :"+pwz)
print("-------------")
input()