file_path = "do-not-touch.txt"


def write_climb_values(left_hook_zero: str, right_hook_zero: str):
    """
    Writes the left and right hook zeroes to the saved text file.
    :param left_hook_zero: The string of the left hook zero.
    :param right_hook_zero: The string of the right hook zero.
    :return:
    """
    file = open(file_path, "w")
    file.write(left_hook_zero + "\n")
    file.write(right_hook_zero)
    file.close()


def read_climb_values() -> (str, str):
    """
    Reads the left and right hook zeroes from the saved text file.
    :return: (leftHookZero, rightHookZero) in a tuple of strings.
    """
    file = open(file_path, "r+")
    left_hook_zero = file.readline().strip()
    right_hook_zero = file.readline().strip()
    file.close()
    return left_hook_zero, right_hook_zero
