from frontend.parsers import (
    parse_amount,
    parse_positive_amount,
    parse_index,
    parse_choice,
    parse_name,
    parse_list,
)

class TerminalUI:

    def __init__(self, tracker):
        self.tracker = tracker

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
        return parse_choice(input("Enter menu choice: "), [1, 2, 3, 4, 5, 6, 7, 8])

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
        return parse_name(input("Enter workout name: "))

    def input_workout_reps(self):
        return parse_list(input("Enter workout reps: "))

    def handle_add_workout(self):
        name = self.input_workout_name()

        if name is None:
            print("Invalid workout name")
            return

        reps = self.input_workout_reps()

        if reps is None:
            print("Invalid Reps")
            return

        self.tracker.add_workout(name, reps)
        print("Workout added!")

    #Remove_Workout
    def input_remove_workout(self):
        return parse_index(input("Enter workout number to remove: "))

    def handle_remove_workout(self):
        self.show_workouts()

        index = self.input_remove_workout()

        if index is None:
            print("Invalid workout number")
            return

        if self.tracker.remove_workout(index):
            print("Workout removed!")
        else:
            print("Workout not found")

    #Update_Workout
    def input_update_workout(self):
        return parse_index(input("Enter workout number to update: "))

    def handle_update_workout(self):
        self.show_workouts()

        index = self.input_update_workout()

        if index is None:
            print("Invalid workout number")
            return

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
        if not self.tracker.has_workouts():
            print("No workouts available")
            return

        total_workouts = self.tracker.get_total_workouts()
        total_reps = self.tracker.get_total_reps()
        highest_total_reps = self.tracker.get_highest_total_reps()
        lowest_total_reps = self.tracker.get_lowest_total_reps()
        highest_total_reps_by_name = self.tracker.get_highest_total_reps_by_name()
        lowest_total_reps_by_name = self.tracker.get_lowest_total_reps_by_name()

        print(f"Total workouts: {total_workouts}")
        print(f"Total reps: {total_reps}")
        print(f"Highest total reps in one workout: {highest_total_reps}")
        print(f"Lowest total reps in one workout: {lowest_total_reps}")
        print(f"Highest total reps by name: {highest_total_reps_by_name}")
        print(f"Lowest total reps by name: {lowest_total_reps_by_name}")
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

        self.show_workout_results(results)

    def show_workout_results(self, results, empty_message="Workout not found"):
        if len(results) == 0:
            print(empty_message)
            return

        for workout in results:
            reps_text = ", ".join(str(rep) for rep in workout.reps)
            print(f"{workout.name} - {reps_text} reps")

    #Filter_Reps
    def show_filter_menu(self):
        print("1. Filter for minimum total reps")
        print("2. Filter for maximum total reps")

    def input_filter_total_reps(self):
        return parse_positive_amount(input("Enter total reps: "))

    def input_filter_choice(self):
        return parse_choice(input("Enter choice: "), [1, 2])

    def handle_filter_workouts_by_reps(self):
        self.show_filter_menu()

        choice = self.input_filter_choice()

        if choice is None:
            print("Invalid choice")
            return

        total_reps = self.input_filter_total_reps()

        if total_reps is None:
            print("Invalid Reps")
            return

        if choice == 1:
            results = self.tracker.get_workouts_with_min_total_reps(total_reps)
        else:
            results = self.tracker.get_workouts_with_max_total_reps(total_reps)

        self.show_workout_results(results, empty_message="No workouts found")



    #Flow
    def run(self):
        while True:
            self.show_menu()
            choice = self.input_menu_choice()

            if choice is None:
                print("Invalid choice")
                continue

            if choice == 6:
                print("Exiting...")
                break

            self.handle_menu_choice(choice)
