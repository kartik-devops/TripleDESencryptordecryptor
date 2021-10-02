import cryptography
import os
from hashlib import md5
from Crypto.Cipher import DES3
import pyfiglet
def TripleDESIMG(imgnm,tdeskey) :
	choice = int(input("Enter 1 to encrypt and 2 to decrypt :")) 
	keyhash = md5(tdeskey.encode('ascii')).digest()
	Final_parity_key = DES3.adjust_key_parity(keyhash)
	cipher = DES3.new(Final_parity_key , DES3.MODE_EAX , nonce=b'0')
	
	with open(imgnm , 'rb') as inp_img:
		filedata = inp_img.read()
		if choice==1 :
			filedata2 = cipher.encrypt(filedata)
		else :
			filedata2 = cipher.decrypt(filedata)
	                
	with open(imgnm , 'wb') as oup_res :
		oup_res.write(filedata2)
		
result = pyfiglet.figlet_format("3DES Encryptor and Decryptor", font = "digital" )
print(result)
imgnm = input("Enter the image name to encrypt or decrypt:")
if os.path.exists(imgnm)==False :
	print ("Image does not exist")
else :
        print("Path is valid")
        tdeskey = input("Enter tdes key : ")
        TripleDESIMG(imgnm,tdeskey);
       
