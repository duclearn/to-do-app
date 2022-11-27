def get_data(file="data.txt"):
    """ get data from the data.txt
    and assign to the data
    """
    with open(file, "r") as file:
        data = file.readlines()
        return data


def write_data(data_arg, file_path="data.txt"):
    with open("data.txt", "w") as file:
        file.writelines(data_arg)



if __name__ == "__main__":
    print("hello from function")