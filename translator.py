import pyperclip
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
# makes the file location readable by changing \ to \\ because of escape keys
language = values[0].lower()
fileLocation = values[1].replace("\\", "\\\\").replace("\"", "")
# opens the file and reads it
originalRecipe = open(fileLocation, "r")
originalRecipeInput = originalRecipe.read()
originalRecipe.close()
# translates the recipe
translated = GoogleTranslator(source='auto', target=language).translate(originalRecipeInput)
# GUI
# https://stackoverflow.com/questions/64028319/pysimplegui-make-text-selectable-with-mouse for line right below
layout = [[sg.InputText(translated, use_readonly_for_disable=True, disabled=True, key='-IN-')],
         [sg.Button('close'), sg.Button('copy')]]
window = sg.Window("Translated Output", layout)
while True:
    event, vales = window.read()
    if event == "WIN_CLOSED" or event == "close":
        break
    # copies to clipboard
    if event == "copy":
        pyperclip.copy(translated)
window.close()
