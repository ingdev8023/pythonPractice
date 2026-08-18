def square_root_bisection(number, tolerance = 0.001, iterations = 100 ):
    if number < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if number == 0 or number == 1:
        print(f'The square root of {number} is {number}')
        return number
    
    #step 1

    #fx= x^2 - N

    real_iterations = 0
    first_interval = 0
    second_interval = max(1, number)
    error = 1
    

    cal_1 = first_interval ** 2 - number
    cal_2 = second_interval ** 2 - number

    if cal_1 == 0:
        return first_interval

    if cal_2 == 0:
        return second_interval

    while real_iterations < iterations:

        middle_point = (first_interval + second_interval) / 2
        middle_cal = middle_point ** 2 - number

        # Exact root found
        if middle_cal == 0:
            print(
                f'The square root of {number} '
                f'is approximately {middle_point}'
            )
            return middle_point

        # Keep the half containing the root
        if cal_1 * middle_cal < 0:
            second_interval = middle_point
            cal_2 = middle_cal
        else:
            first_interval = middle_point
            cal_1 = middle_cal

        # Error estimate
        error = (second_interval - first_interval) / 2

        if error <= tolerance:
            root = (first_interval + second_interval) / 2

            print(
                f'The square root of {number} '
                f'is approximately {root}'
            )

            return root

        real_iterations += 1

    print(f'Failed to converge within {iterations} iterations')
    return None



    

print(square_root_bisection(81, 1e-3, 50))
print(square_root_bisection(0.25, 1e-7, 50))
print(square_root_bisection(0.001, 1e-7, 50))