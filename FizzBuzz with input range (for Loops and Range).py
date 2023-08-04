#Write your code below this row 👇

numbers_to_print = input("What is the range of numbers you would like to print? Separate them with a space. ")

numbers_to_print = numbers_to_print.split(" ")

beginning_range = int(numbers_to_print[0])
end_range = int(numbers_to_print[1])

#FizzBuzz formula
for n in range(beginning_range, end_range + 1):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
