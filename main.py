
# MY WORKOUT TRACKER 💪

workouts = []

def add_workout():
    print("\nADD A WORKOUT")

    exercise = input("What exercise did you do? ")
    minutes = int(input("How many minutes? "))
    day = input("What day was it? ")

    workout = [exercise, minutes, day]
    workouts.append(workout)

    print("Workout saved!")


def show_workouts():
    print("\nWORKOUT HISTORY")

    if len(workouts) == 0:
        print("No workouts yet!")
    else:
        for workout in workouts:
            print("----------------")
            print("Exercise:", workout[0])
            print("Minutes:", workout[1])
            print("Day:", workout[2])


def show_chart():
    print("\nYOUR TRAINING CHART")

    if len(workouts) == 0:
        print("No workouts to show!")
        return

    for workout in workouts:
        print(workout[0])
        print("#" * workout[1], workout[1], "minutes")


while True:
    print("\n======================")
    print("   WORKOUT TRACKER")
    print("======================")
    print("1. Add workout")
    print("2. View workouts")
    print("3. Show chart")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_workout()

    elif choice == "2":
        show_workouts()

    elif choice == "3":
        show_chart()

    elif choice == "4":
        print("Great job training!")
        break

    else:
        print("Choose 1, 2, 3 or 4.")