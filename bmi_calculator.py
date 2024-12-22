def calculate_bmi():
    print("BMI Calculator")
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    bmi = weight / (height ** 2)
    print(f"Your BMI is: {bmi:.2f}")

    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obesity"
    print(f"You are categorized as: {category}")

if __name__ == "__main__":
    calculate_bmi()
import random

def guess_the_number():
    print("Welcome to 'Guess the Number'!")
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

if __name__ == "__main__":
    guess_the_number()
def display_tasks(tasks):
    print("\nYour To-Do List:")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task}")
    print()

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

def delete_task(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to delete: "))
        removed_task = tasks.pop(task_num - 1)
        print(f"Task '{removed_task}' deleted.")
    except (IndexError, ValueError):
        print("Invalid task number.")

def main():
    tasks = []
    while True:
        print("\nTo-Do List Options:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
def length_converter():
    print("\nLength Converter")
    meters = float(input("Enter length in meters: "))
    kilometers = meters / 1000
    print(f"{meters} meters is {kilometers} kilometers.")

def weight_converter():
    print("\nWeight Converter")
    grams = float(input("Enter weight in grams: "))
    kilograms = grams / 1000
    print(f"{grams} grams is {kilograms} kilograms.")

def main():
    while True:
        print("\nUnit Converter Options:")
        print("1. Convert Length (meters to kilometers)")
        print("2. Convert Weight (grams to kilograms)")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            length_converter()
        elif choice == "2":
            weight_converter()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
