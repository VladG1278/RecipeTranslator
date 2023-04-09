import time
import sys
import PySimpleGUI as sg
from deep_translator import GoogleTranslator

# https://www.geeksforgeeks.org/user-input-in-pysimplegui/#
sg.theme('LightBlue1')


layout = [
    [sg.Text('Please enter the desired language and file to convert.')],
    [sg.Text('Language to Convert To:', size=(20, 1)), sg.InputText()],
    [sg.Text('File Location:', size=(20, 1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window('Translator', layout)
event, values = window.read()
window.close()

# end of gui code from geeksforgeeks
language = values[0]
fileLocation = values[1].replace("\\", "\\\\").replace("\"", "")
originalRecipe = open(fileLocation, "r")
originalRecipeInput = originalRecipe.read()
originalRecipe.close()
translated = GoogleTranslator(source='auto', target=language).translate(originalRecipeInput)
length = len(fileLocation)
length = length - fileLocation.rindex("\\") - 1
name = fileLocation[-length:]
layout = [[sg.Text(translated)],
         [sg.Button('close')]]
window = sg.Window("Translated Output", layout)
while True:
    event, vales = window.read()
    if event == "close":
        break
window.close()
