""" test class """
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

GLOBAL_VAR = 2


def print_hi(name):
    """

    :param name:
    :return:
    """
    # Use a breakpoint in the code line below to debug your script.
    your_age = 43
    local_var = GLOBAL_VAR
    print(f"Hi, {name} {your_age}")  # Press Ctrl+F8 to toggle the breakpoint.
    some_list = (1, 2, 3, 4)
    for some_item in some_list:
        print(some_item**local_var)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print_hi("PyCharm")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
