def selection_sort(numbers):
    
    
    for i in range(len(numbers)):
       
        minimum = i
        
        for x in range(i + 1, len(numbers)):
            if numbers[x] < numbers[minimum]:
                print(f'{numbers[x]} is less than {numbers[minimum]}')
                minimum = x
            
        if minimum != i:
            numbers[i], numbers[minimum] = (
                numbers[minimum],
                numbers[i]
            )      
                
        
            
                        
    return numbers

#print(selection_sort([33, 1, 89, 2, 67, 245]))
#print(selection_sort([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]) )
print(selection_sort([5, 16, 99, 12, 567, 23, 15, 72, 3]) )
    