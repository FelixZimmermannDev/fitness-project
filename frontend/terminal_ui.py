class TerminalUI:

    def __init__(self, tracker):
        self.tracker = tracker

    #Parse
    def parse_amount(self, user_input):
        user_input = user_input.strip()

        try:
            return int(user_input)

        except ValueError:
            return None

    #Menu
    def show_menu(self):
        print("Welcome to the Terminal UI!\n")
        print("1. Add workout")
        print("2. Remove workout")
        print("3. Show workouts")
        print("4. Change workouts")
        print("5. Exit")

    def input_menu_choice(self):
        return self.parse_amount(input("Enter menu choice: "))

    def handle_menu_choice(self, choice):
        if choice == 1:
            self.handle_add_workout()
        if choice == 2:
            self.handle_remove_workout()
        if choice == 3:
            self.show_workouts()
        if choice == 4:
            self.handle_update_workout()

    #Show_Workouts
    def show_workouts(self):
        print("Current workouts:")

        if not self.tracker.has_workouts():
            print("No current workouts")
            return

        for index, workout in enumerate(self.tracker.get_workouts(), start=1):
            print(f"{index}. {workout.name} - {workout.reps} reps")

    #Add_Workout
    def input_workout_name(self):
        return input("Enter workout name: ")

    def input_workout_reps(self):
        return self.parse_amount(input("Enter workout reps: "))

    def handle_add_workout(self):
        name = self.input_workout_name().strip().lower()
        name = name.capitalize()

        if len(name.split()) != 1:
            print("Workout name must contain only one word")
            return

        reps = self.input_workout_reps()

        if reps is None:
            print("Invalid Reps")
            return

        self.tracker.add_workout(name, reps)
        print("Workout added!")

    #Remove_Workout
    def input_remove_workout(self):
        return self.parse_amount(input("Enter workout number to remove: "))

    def handle_remove_workout(self):
        self.show_workouts()

        number = self.input_remove_workout()

        if number is None:
            print("Invalid workout number)
            return

        index = number - 1

        if self.tracker.remove_workout(index):
            print("Workout removed!")
        else:
            print("Workout not found")

    #Update_Workout
    def input_update_workout(self):
        return self.parse_amount(input("Enter workout number to update: "))

    def handle_update_workout(self):
        self.show_workouts()

        number = self.input_update_workout()

        if number is None:
            print("Invalid workout number")
            return

        index = number - 1
        reps = self.input_workout_reps()

        if reps is None:
            print("Invalid Reps")
            return

        if self.tracker.update_workout(index, reps):
            print("Workout updated!")
        else:
            print("Workout not found")


    #Flow
    def run(self):
        while True:
            self.show_menu()
            choice = self.input_menu_choice()

            if choice not in [1, 2, 3, 4, 5]:
                print("Invalid choice")
                continue

            if choice == 5:
                print("Exiting...")
                break

            self.handle_menu_choice(choice)
