# this is a simple text-to-speech program using pyttsx3
# make sure to install the pyttsx3 library first using pip
import pyttsx3

engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("I will speak this text")
engine.runAndWait()+-
