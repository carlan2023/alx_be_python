# daily_reminder.py

# Program: Daily Reminder
# Objective: Ask the user for a single task, its priority, and time-sensitivity.
#            Then, print a customized reminder using match-case, conditionals, and a loop.

while True:
    # Prompt user for task details
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Process task using match-case
    match priority:
        case "high":
            if time_bound == "yes":
                print(f"\nReminder: '{task}' is a HIGH priority task that requires immediate attention today!\n")
            else:
                print(f"\nReminder: '{task}' is a HIGH priority task. Please try to complete it soon.\n")

        case "medium":
            if time_bound == "yes":
                print(f"\nReminder: '{task}' is a MEDIUM priority task that should be scheduled today.\n")
            else:
                print(f"\nReminder: '{task}' is a MEDIUM priority task. Work on it when you have time.\n")

        case "low":
            if time_bound == "yes":
                print(f"\nReminder: '{task}' is a LOW priority but time-bound task. Plan to complete it today.\n")
            else:
                print(f"\nNote: '{task}' is a LOW priority task. You can do it whenever you have free time.\n")

        case _:
            print("\nInvalid input. Please enter high, medium, or low for priority.\n")

    # Exit loop after one reminder (since only one task is needed)
    break
