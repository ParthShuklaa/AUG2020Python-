"""
Step:1 Import Lib/Package
Step:2 Use Class/Methods
Step:3 Display/Save Output
"""
import gtts
import os

myVoice = gtts.gTTS(text="Hi Every One", lang='en',slow= False
                    #Calling Constructor
myVoice.save("MyVOICE1.mp3")
#Saving Info
os.system("MyVOICE1.mp3")
#Output
