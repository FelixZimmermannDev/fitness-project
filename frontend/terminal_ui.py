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

    def parse_reps(self, user_input):
        parts = user_input.strip().split()
        reps = []

        for part in parts:
            try:
                reps.append(int(part))  #Try ob userinput eine zahl ist

            except ValueError:
                return None

        return reps     #Return die Liste

    #Menu
    def show_menu(self):
        print("Welcome to the Terminal UI!\n")
        print("1. Add workout")
        print("2. Remove workout")
        print("3. Show workouts")
        print("4. Change workouts")
        print("5. Show summary")
        print("6. Exit")

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
        if choice == 5:
            self.show_summary()

    #Show_Workouts
    def show_workouts(self):
        print("Current workouts:")

        if not self.tracker.has_workouts():
            print("No current workouts")
            return

        for index, workout in enumerate(self.tracker.get_workouts(), start=1):
            reps_text = ", ".join(str(rep) for rep in workout.reps)
            print(f"{index}. {workout.name} - {reps_text} reps")

    #Add_Workout
    def input_workout_name(self):
        return input("Enter workout name: ")

    def input_workout_reps(self):
        return self.parse_reps(input("Enter workout reps: "))

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
            print("Invalid workout number")
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

    #Summary_Workout
    def show_summary(self):
        total_workouts = self.tracker.get_total_workouts()
        total_reps = self.tracker.get_total_reps()

        print(f"Total workouts: {total_workouts}")
        print(f"Total reps: {total_reps}")
        print()

        summary = self.tracker.get_total_reps_by_name()

        for name, reps in summary.items():
            print(f"{name}: {reps} reps")

    #Flow
    def run(self):
        while True:
            self.show_menu()
            choice = self.input_menu_choice()

            if choice not in [1, 2, 3, 4, 5, 6]:
                print("Invalid choice")
                continue

            if choice == 6:
                print("Exiting...")
                break

            self.handle_menu_choice(choice)
