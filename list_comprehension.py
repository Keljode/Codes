numbers = [57, 10, 82, 36, 89, 46, 13, 23, 92, 48]
even_num =[]
#for num in numbers:
    
    #even_num.append(num%2 == 0)
    
even_num = [ num for num in numbers if num % 2 ==0]
print(even_num)
print(numbers)
