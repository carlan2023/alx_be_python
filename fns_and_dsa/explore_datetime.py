from datetime import datetime, timedelta

def display_current_datetime():
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return display_current_datetime
def calculate_future_date(days_to_add: int):

    #Calculate the future date after adding given days to the curent date.
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)
    print("Future date:", future_date.strftime("%Y-%M-%d"))
    return future_date
def main():
    # Part 1: Display current datetime
    display_current_datetime()
    
    # Part 2: Prompt user and calculate future date
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days)
    except ValueError:
        print("Invalid input! Please enter a valid integer.")