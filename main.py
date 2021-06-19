import traceback

#contexe (continue execution ), takes care of telling script to stop if it needs to restart
global contexe
contexe=1



#Continually be running the code 
while True:
#Handle any exceptions 
 

   
   
   

  #These lines will read the script 
  scriptfileread = open("script.py", "r")
  scriptlines=scriptfileread.read()
  
  #These lines will read 
  scriptfilewrite=open("script.txt","w+")
  scriptfilewrite.write(scriptlines)

  #Read the whats stored in the text file to compare with the script lines 
  textversionofscriptfile=open("script.txt","r")
  textlines=textversionofscriptfile.read()

  #If code edited logic 
  if scriptlines!=textlines:
   
   #Clean the terminal
   print(chr(27)+'[2j')
   print('\033c')
   print('\x1bc')
   #STOP SCRIPT LOOP
   contexe=0
   #ALLOW SCRIPT LOOP TO RESTART ON BOOT
   contexe=1
   #This line will run the script
   exec(open("script.py").read())
  #If code not edited logic 
  else: 
    #if the code has not been edited do nothing, removing this will cause an infinite loop
    continue
 

  


def checkforneedrestart():
  return contexe