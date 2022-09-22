file_path = "do-not-touch.txt"


def write_climb_values(left_hook_zero: str, right_hook_zero: str):
    file = open(file_path, "w")
    file.write(left_hook_zero + "\n")
    file.write(right_hook_zero)
    file.close()


def read_climb_values() -> (str, str):
    file = open(file_path, "r+")
    left_hook_zero = file.readline().strip()
    right_hook_zero = file.readline().strip()
    file.close()
    return left_hook_zero, right_hook_zero
