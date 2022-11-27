import function

import time

now = time.strftime("%a %b %d, %Y")
print("To day is: ", now)

while True:
    user_option = input("type your command add/view/edit/delete/quite: ")
    if user_option.startswith("add"):
        contents = user_option[4:] + "\n"

        data = function.get_data()

        data.append(contents)

        function.write_data(data)

    elif user_option.startswith("view"):
        data = function.get_data()
        for index, line in enumerate(data):
            print(f"{index + 1}-{line.strip()}")

    elif user_option.startswith("edit"):
        try:
            edit_index = int(user_option[5:])
            data = function.get_data()
            edit_contain = input("Enter your containt: ")

            data[edit_index - 1] = edit_contain + "\n"

            function.write_data(data)

        except ValueError:
            print("your command not correct")
            continue

    elif user_option.startswith("delete"):
        try:
            delete_index = int(user_option[7:])
            data = function.get_data()

            data.pop(delete_index - 1)

            function.write_data(data)

        except IndexError:
            print("No data to delete")
            continue

    elif user_option.startswith("quite"):
        break
    else:
        print("Invalid command")

print("Good buy your data is saved")
