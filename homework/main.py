def filter_even(numbers): 
    myList = []
    for number in numbers:
        if number % 2 == 0:
            myList.append(number)        
    return myList        


def calculate_sum(even_numbers):
    even_number = 0
    for number in even_numbers:
        even_number += number
    return even_number


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter_even(numbers)
sum_even = calculate_sum(even_numbers)

print("Сумма четных чисел:", sum_even)