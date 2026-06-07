class TerminalUI:

    def __init__(self, tracker):
        self.tracker = tracker

    #Parse
    def parse_amount(self, user_input): #Als Einzelwert
        user_input = user_input.strip()

        try:
            return int(user_input)

        except ValueError:
            return None

    def parse_reps(self, user_input):   #Als Liste
        parts = user_input.strip().split()

        if len(parts) == 0:
            return None

        reps = []

        for part in parts:
            try:
                rep = int(part)
            except ValueError:
                return None

            if rep <= 0:
                return None

            reps.append(rep)

        return reps

    def parse_name(self, user_input):
        name = user_input.strip().lower().capitalize()

        if len(name.split()) != 1:
            return None         #If mehr als 1 Wort

        if not name.isalpha():
            return None

        return name

    #Menu
    def show_menu(self):
        print("Welcome to the Terminal UI!\n")
        print("1. Add workout")
        print("2. Remove workout")
        print("3. Show workouts")
        print("4. Change workouts")
        print("5. Show summary")
        print("6. Exit")
        print("7. Search workout")
        print("8. Filter by reps")

    def input_menu_choice(self):
        return self.parse_amount(input("Enter menu choice: "))

    def handle_menu_choice(self, choice):
        if choice == 1:
            self.handle_add_workout()
        elif choice == 2:
            self.handle_remove_workout()
        elif choice == 3:
            self.show_workouts()
        elif choice == 4:
            self.handle_update_workout()
        elif choice == 5:
            self.show_summary()
        elif choice == 7:
            self.handle_search_workout()
        elif choice == 8:
            self.handle_filter_workouts_by_reps()

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
        return self.parse_name(input("Enter workout name: "))

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

    #Search_Workout
    def input_search_workout(self):
        name = self.input_workout_name()

        if name is None:
            print("Invalid workout name")
            return

        return name

    def handle_search_workout(self):
        name = self.input_search_workout()

        if name is None:
            return

        results = self.tracker.get_workouts_by_name(name)

        if len(results) == 0:
            print("Workout not found")
            return

        print("Found!")

        for workout in results:
            reps_text = ', '.join(str(rep) for rep in workout.reps)
            print(f"{workout.name} - {reps_text} reps")

    #Filter_Reps
    def input_filter_total_reps(self):
        return self.parse_amount(input("Enter total reps: "))

    def show_filter_menu(self):
        print("1. Filter for minimum total reps")
        print("2. Filter for maximum total reps")

    def input_filter_choice(self):
        return self.parse_amount(input("Enter filter choice: "))

    def handle_filter_workouts_by_reps(self):
        self.show_filter_menu()

        choice = self.input_filter_choice()

        if choice is None:
            print("Invalid choice")
            return

        if choice == 1:
            min_reps = self.input_filter_total_reps()

            if min_reps is None:
                print("Invalid Reps")
                return

            results = self.tracker.get_workouts_with_min_total_reps(min_reps)

        elif choice == 2:
            max_reps = self.input_filter_total_reps()

            if max_reps is None:
                print("Invalid Reps")
                return

            results = self.tracker.get_workouts_with_max_total_reps(max_reps)

        else:
            print("Invalid choice")
            return

        if len(results) == 0:
            print("No workouts found")
            return

        for workout in results:
            reps_text = ", ".join(str(rep) for rep in workout.reps)
            print(f"{workout.name} - {reps_text} reps")

    #Flow
    def run(self):
        while True:
            self.show_menu()
            choice = self.input_menu_choice()

            if choice not in [1, 2, 3, 4, 5, 6, 7, 8]:
                print("Invalid choice")
                continue

            if choice == 6:
                print("Exiting...")
                break

            self.handle_menu_choice(choice)
