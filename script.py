import os

import pyfiglet
import asyncio
import time
import main

#DELETE TO GET RID OF FANCY BOOTING 
boot_banner = pyfiglet.figlet_format("Alfred V4")






def speak(text:str):
   print(f"Would speak: {text}")




class AlfCommands():
  
  async def time():
   import time

   t = time.localtime()
   current_time = time.strftime("%H:%M:%S", t)
   print(current_time)
async def parser():
# print( AlfCommands.__dict__.values())
  for callable in AlfCommands.__dict__.values():
    try:
        await callable()    
    except TypeError:
        pass
  
def on_boot():
 
  print(boot_banner)
  print("Hello, Gunnar")
  speak("Hello Gunner")
 


#allows the script to be rebooted 
def runloopswitch():
   runloop=asyncio.new_event_loop()
   runloop.create_task(parser())
   while main.checkforneedrestart():
    runloop.run_forever()
 




on_boot()



    


