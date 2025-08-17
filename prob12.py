# the following code is for text-to-speech conversion using pyttsx3 library
# Make sure to install the library first using: pip install pyttsx3
import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("I will speak this text")
engine.runAndWait()