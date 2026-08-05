def unique_even_squares(numbers):

    unique_numbers = set(numbers)
    
  
    results = []
    for number in unique_numbers:
        if number % 2 == 0:
            results.append(number ** 2)
    return results

    

print(unique_even_squares([1, 2, 3, 4, 5, 6, 2, 4]))

