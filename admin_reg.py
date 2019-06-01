# -*- coding: utf-8 -*-
"""
Created on Tue May 21 11:04:43 2019

@author: champion
"""

import os
from passlib.hash import sha256_crypt

def getaddress():
    import re, uuid 
  
    # joins elements of getnode() after each 2 digits. 
    # using regex expression 
    print ("The MAC address in formatted and less complex way is : ", end="") 
    s=':'.join(re.findall('..', '%012x' % uuid.getnode()))
    print(s)
    return s

admin='cojag'
secret_key='root'
username=input('Enter the Admin UserName : ' )
password=input('Enter the Admin Password: ')

if admin==username and secret_key==password:
        print('Successfully Logged in as the Admin, Proceed for the configuration of Device')
        print("Note: Please Switch Off the Random Hardware Address Feature")
        print("Setting-> Internet & Connectivity -> Wifi -> Random Hardware address")
        print("Do you want to include this device as the Master host?? ")
        choice=input("Confirm [y/n]  : ")
        if choice=='n':
            print("Thank you,Bye ")
        else:
            print("Configuring your MAC Address......")
            mac_address=getaddress()
            f=open('register_file.txt','w')
            hash = sha256_crypt.hash(mac_address)
            f.write(hash+" \n")
            f.close()
            print("Your device is configured")         
else:
    print("Username or Password not correct, Please call the Admin.....")