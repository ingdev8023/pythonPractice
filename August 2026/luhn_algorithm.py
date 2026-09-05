def verify_card_number(card_number):
    clean_number = (card_number.replace("-", "").replace(" ",""))[::-1]

    sum_check = 0

    for index in range(len(clean_number)):
    
        if index % 2 != 0:
            number_check = int(clean_number[index]) * 2
            if number_check < 9:
                sum_check += number_check
            elif number_check > 9:
                sum_check += (number_check - 9)
        else:
            sum_check += int(clean_number[index])
        
    
    final_check = "VALID!" if sum_check % 10 == 0 else "INVALID!" 
    
    return final_check


print(verify_card_number('4111-1111-1111-1111'))
print(verify_card_number('453914889'))
print(verify_card_number('453914881'))

