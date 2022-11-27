import function
import PySimpleGUI as sg

label = sg.Text("Type in your command ")
input_box = sg.InputText()
add_button = sg.Button("Add")

window = sg.Window("My Adding App", layout=[[label], [input_box, add_button]])
window.read()

window.close()