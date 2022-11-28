import function
import PySimpleGUI as sg

label = sg.Text("Type in your command ")
input_box = sg.InputText(key="to_do")
add_button = sg.Button("Add")

list_box = sg.Listbox(values=function.get_data(), key="list",
                      enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")
window = sg.Window("My Adding App", layout=[[label], [input_box, add_button],
                                            [list_box, edit_button]])

while True:
    event, value = window.read()
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

        case "Edit":
            todo_edit = value["list"][0]
            new_todo = value["to_do"]

            data = function.get_data()

            index = data.index(todo_edit)
            data[index] = new_todo
            function.write_data(data)
            window["list"].update(values=data)
        case "list":
            window["to_do"].update(value=value['list'][0])


        case sg.WIN_CLOSED:
            break
print(event)
print(value)
window.close()