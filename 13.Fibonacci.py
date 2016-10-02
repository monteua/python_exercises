number_of_numbers = raw_input("How many Fibonnaci numbers generate?")
number_of_numbers = int(number_of_numbers)
fibonacci_sequence = [1, 1]

def fibonacci():
    for number in range(number_of_numbers-2):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
fibonacci()
print fibonacci_sequence
