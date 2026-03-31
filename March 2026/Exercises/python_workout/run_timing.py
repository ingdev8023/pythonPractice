"""Write a function (run_timing) that asks how long it took for you to run 10 km. The
function continues to ask how long (in minutes) it took for additional runs, until the
user presses Enter. At that point, the function exits—but only after calculating and dis￾playing the average time that the 10 km runs took.
 For example, here’s what the output would look like if the user entered three data
points:
Enter 10 km run time: 15
Enter 10 km run time: 20
Enter 10 km run time: 10
Enter 10 km run time: <enter>
Average of 15.0, over 3 runs
Note that the numeric inputs and outputs should all be floating-point values. This
exercise is meant to help you practice converting inputs into appropriate types, along
with tracking information over time."""

 
            
def run_timing():

    total = 0
    count = 0

    while True:
        time_input = input('Enter 10km run time: ')

        if time_input == '':
            if count == 0:
                print("No runs entered.")
                return
            print(f"Average of {total / count}, over {count} runs")
            return

        try:
            time = float(time_input)
            total += time
            count += 1
        except ValueError:
            print("Please enter a valid number.")
            

run_timing()