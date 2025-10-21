#Tip Calculator
#Given the price of your meal and a custom tip percent, return an array with three tip values; 15%, 20%, and the custom amount.

#Prices will be given in the format: "$N.NN".
#Custom tip percents will be given in this format: "25%".
#Return amounts in the same "$N.NN" format, rounded to two decimal places.

def calculate_tips(meal_price, custom_tip):
    meal_real_price = float(meal_price.replace('$', ''))
    custom_number = float(custom_tip.replace('%', ''))
    tips= [0.15,0.20,custom_number/100]
    results= []
    for i in tips:
        tip_amount = i * meal_real_price
        results.append(f"${tip_amount:.2f}")
    return results

calculate_tips("$10.00", "25%")
calculate_tips("$89.67", "26%")
calculate_tips("$19.85", "9%")