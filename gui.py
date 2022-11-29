import function
import PySimpleGUI as sg
import time


clock = sg.Text("", key="clock")
label = sg.Text("Type in your command ")
input_box = sg.InputText(key="to_do")
add_button = sg.Button("Add")

list_box = sg.Listbox(values=function.get_data(), key="list",
                      enable_events=True, size=[40,10])
edit_button = sg.Button("Edit")
delete_button = sg.Button("Delete")
exit_button = sg.Button("Exit")
window = sg.Window("My Adding App",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, delete_button],
                           [exit_button]],
                   font=("helvetica", 20))

while True:
    event, value = window.read(timeout=100)
    window["clock"].update(value= time.strftime("%a %b %d, %Y %H:%M:%S"))
    print(event)
    print(value)
    print(value["list"])
    print(value["to_do"])
    match event:
        case "Add":
            data = function.get_data()
            data.append(value["to_do"] + "\n")
            function.write_data(data)
            window["list"].update(values=data)
            window["to_do"].update(value="")
        case "Edit":
            try:
                todo_edit = value["list"][0]
                new_todo = value["to_do"]

                data = function.get_data()

                index = data.index(todo_edit)
                data[index] = new_todo
                function.write_data(data)
                window["list"].update(values=data)
            except IndexError:
                sg.popup("Please select item in list box", font=("helvetica", 20))
        case "Delete":
            try:
                todo_delete = value["list"][0]
                data = function.get_data()
                data.remove(todo_delete)
                function.write_data(data)
                window["list"].update(values=data)
                window["to_do"].update(value="")
            except IndexError:
                sg.popup("Please select the item", font=("helvetica", 20))
        case "Exit":
           break
        case "list":
            window["to_do"].update(value["list"][0])


        case sg.WIN_CLOSED:
            break
print(event)
print(value)
window.close()