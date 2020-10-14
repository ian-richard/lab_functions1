def return_10():
    return 10

def add (num1, num2):
    add_result = num1 + num2
    return add_result

def subtract(n1, n2):
    subtract_result = n1 - n2
    return subtract_result

def multiply(n1, n2):
    multiply_result = n1 * n2
    return multiply_result

def divide(n1, n2):
    divide_result = n1 / n2
    return divide_result

def length_of_string(string):
    return len(string)

def join_string(s1,s2):
    return f"{s1}{s2}"

def add_string_as_number(p1, p2):
    return int(p1) + int(p2)

def number_to_full_month_name(month_number):
    month_tuple = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
    month_number -= 1
    return month_tuple[month_number]

def number_to_short_month_name(month_number):
    month_tuple = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
    month_number -= 1
    return month_tuple[month_number]

def get_volume_of_cube(length_of_side):
    volume_of_cube = length_of_side ** 3
    return volume_of_cube

def reverse_string(input_string):
    string_output = input_string [::-1]
    return string_output

def convert_fahrenheit_to_celsius(temp_in_fahrenheit):
    converted_temp = (temp_in_fahrenheit - 32) * 5/9
    return converted_temp
