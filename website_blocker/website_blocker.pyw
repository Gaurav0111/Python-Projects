# for blocking the websites we have to ruk this python as in background so that it can be activated all the time and can block the given website in the given time 


import time
from datetime import datetime as dt

# in host path you have specify the path of the HOSTS file of you O.S. 
host_path = "hosts"
# host_path = "C:\\Windows\\System32\\drivers\\etc\\hosts"

redirect = "127.0.0.1"

# it containes all the list of websites which we wants to block 
website = ["www.facebook.com","facebook.com","www.instagram.com","instagram.com"]

while True:
    # this condition will check weather the time is between 8am to 4pm:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16): 
        with open (host_path,"r+") as file:
            content = file.read()
            for a in website:
                if a in content:
                    pass
                else:
                    file.write("\n" +redirect+" "+a)
        print("Working hours")
    else:
        with open(host_path,"r+") as file:
            content = file.readlines()
            file.seek(0) #this will tale the cursor at first position in host file
            for line in content:
                if not any (a  in line for a in website):
                    file.write(line)
            file.truncate() #this will delete the content which is below the cursor
        print("Not in working hours")
    time.sleep(3) # this will run the program in every given seconds
