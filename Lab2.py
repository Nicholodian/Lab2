def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def calc_average():
    print("calc_average")
def get_user_input():
    # Step 1: Read a sequence of numbers from the user
    user_input = input()

    # Step 2: Split the user-entered string into a list of strings
    num_strings = user_input.split(',')

    # Step 3: Convert the list of strings to a list of floats
    num_list = [float(num) for num in num_strings]

    # Step 4: Return the list of floats
    return num_list

def calc_average_temperature(num_list):
    average = sum(num_list)/len(num_list)

def calc_min_max_temperature(num_list):
    min = min(num_list)
    max = max(num_list)

    return[min,max]

def sort_temperature(num_list):
    sortedlist = sorted(num_list)
    return(sortedlist)

def calc_median_temperature(num_list):
    sorted_temperatures = sorted(num_list)


    n = len(sorted_temperatures)

    if n % 2 == 0:
        middle1 = sorted_temperatures[n // 2 - 1]
        middle2 = sorted_temperatures[n // 2]
        median_temp = (middle1 + middle2) / 2
    else:
        median_temp = sorted_temperatures[n // 2]

    return median_temp

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()


if __name__ == "__main__":
    main()