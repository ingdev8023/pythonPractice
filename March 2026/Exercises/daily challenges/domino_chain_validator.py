def is_valid_domino_chain(dominoes):
    last_value = dominoes[0][1]
    for i in dominoes[1:]:
        if i[0] != last_value:
            return False
        last_value = i[1]
                   
    return True     
   

print(is_valid_domino_chain([[1, 3], [3, 6], [6, 5]]))
print(is_valid_domino_chain([[4, 3], [3, 1], [1, 6], [6, 6], [6, 5], [5, 1], [1, 1], [1, 4], [4, 4], [4, 2]]))