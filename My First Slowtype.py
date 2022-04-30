#Modules:
import sys
import time

#Functions:
def slowtype(txt):
  for i in txt:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.06)
  sys.stdout.write("\n")

#Script:
slowtype("*********************")
slowtype("* My First Slowtype *")
slowtype("*********************\n")
slowtype("This is my very first slowtype.")
