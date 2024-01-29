import subprocess

def passwordrevealer(ssid):
    result=subprocess.check_output(['netsh','wlan','show','profile',
    'name='+ssid,'key=clear'],universal_newlines=True)
    key_index=result.find("key Content")
    if(key_index!=-1):
       password_start=result.find(":",key_index)+1
       password_end=result.find("\n",password_start)
       password =result[password_start:password_end].strip()

       return password
    
    else:
       return "password not found"

wifi_name=input("enter name of the wifi")

password = passwordrevealer(wifi_name)
print(f"the password of the wifi is {password}")