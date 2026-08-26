def quick_sort(array):
    if len(array) <= 1:
        return array
    
    sorted_array = []
    pivot = array[0]

    first_part = [x for x in array if x < pivot]  

    second_part = [x for x in array if x == pivot]    
    
    third_part = [x for x in array if x > pivot]    
      
    
    
    sorted_array.extend(first_part)
    sorted_array.extend(second_part)
    sorted_array.extend(third_part)

    return (
        quick_sort(first_part)
        + second_part
        + quick_sort(third_part)
    )