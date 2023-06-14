def read_input_information():
    start_position = input("Enter start coordinates separated by , :\n").split(",")
    target_position = input("Enter destination coordinates with , separated:\n").split(",")
    start_position = [int(x) for x in start_position]
    target_position = [int(x) for x in target_position]
    return start_position, target_position