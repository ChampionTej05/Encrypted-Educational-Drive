# -*- coding: utf-8 -*-
"""
Created on Tue May 21 11:22:05 2019

@author: champion
"""

def getaddress():
    import re, uuid 
  
    # joins elements of getnode() after each 2 digits. 
    # using regex expression 
    print ("The MAC address in formatted and less complex way is : ", end="") 
    s=':'.join(re.findall('..', '%012x' % uuid.getnode()))
    print(s)
    return s

from passlib.hash import sha256_crypt
try:
	f=open(r'G:\register_file.txt','r')
	address_arr=f.read().strip()
	print(len(address_arr))
	f.close()

	host_address=getaddress()
	hashed_address=sha256_crypt.hash(host_address)

	if sha256_crypt.verify(getaddress(),address_arr):
		print("Champion, you are in")
		import base64
		import os
		
		
		pw = "champion"   #Default Password
		encode = base64.b64encode(bytes(pw,'utf-8'))
		
		pw = str(input("Enter your password for Lock or Unlock your folder: "))
		
		if pw == base64.b64decode(encode).decode('utf-8'):
		# Change Dir Path where you want Locker Folder
			os.chdir(r"G:\xampplite\htdocs\website")
		# If Locker folder or Recycle bin does not exist then we will be create Locker Folder 
			if not os.path.exists("Champion Protected"):
				if not os.path.exists("Champion Protected.{645ff040-5081-101b-9f08-00aa002f954e}"):
					os.mkdir("Champion Protected")
				else:
					os.popen('attrib -h Champion Protected.{645ff040-5081-101b-9f08-00aa002f954e}')
					os.rename("Champion Protected.{645ff040-5081-101b-9f08-00aa002f954e}","Champion Protected")
					#sys.exit()
			else:
				# Change Dir Path where you will have Locker Folder (after creation)
				os.chmod(r"G:\xampplite\htdocs\website\Champion Protected", 0o777)
				os.rename("Champion Protected","Champion Protected.{645ff040-5081-101b-9f08-00aa002f954e}")
				os.popen('attrib +h Champion Protected.{645ff040-5081-101b-9f08-00aa002f954e}')
		else:
			print ("Wrong password!, Please Enter right password")
			import time
			time.sleep(2)
	else:
		import tkinter
		from tkinter import messagebox
		top = tkinter.Tk()
		messagebox.showerror("Error", "You are not Worthy")
		top.mainloop()
		import time
		time.sleep(2)
		top.withdraw()
		quit()
except IOError as k:
	print("First Register the Device",k)
except Exception as e:
	print(e)
	
   
    
    