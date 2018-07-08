#!/usr/bin/env python3

import subprocess
import time
import sys

print (50 * '#')
print (50 * '-')
print ("             WELCOME TO LIE DETECTOR")
print (50 * '-')
print (50 * '#')
time.sleep(1)
print ("MIT License, v. 1.0")
time.sleep(2)
print()

def main():
   
    print ("Are you a liar? ")

    choice = input("yes or no?  ").lower() 
    
    if choice.startswith('y'):
       print()
       time.sleep(2.0)
       print("LIAR!!!")
      
    else:
       choice.startswith('n')
       print()
       time.sleep(2.0)
       print("LYING LIAR PANTS!!!")
       
main()
