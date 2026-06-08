from frontend.parsers import (
    parse_positive_amount,
    parse_index,
    parse_choice,
    parse_name,
    parse_list,
)
from backend.workout_stats import WorkoutStats
from frontend.formatters import format_workout
from frontend.menus import show_menu, show_filter_menu
from frontend.summary_view import SummaryView

class TerminalUI:

    def __init__(self, tracker):
        self.tracker = tracker
        self.stats = WorkoutStats(tracker)
        self.summary = SummaryView(self.tracker, self.stats)

    ## Menu
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
            self.summary.show_summary()
        elif choice == 7:
            self.handle_search_workout()
        elif choice == 8:
            self.handle_filter_workouts_by_reps()

    def show_workouts(self):
        print("Current workouts:")

        if not self.tracker.has_workouts():
            print("No current workouts")
            return

        for index, workout in enumerate(self.tracker.get_workouts(), start=1):
            print(f"{index}. {format_workout(workout)}")

    ## Add
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

    ## Remove / Update
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

    ## Search
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
            print(format_workout(workout))

    ## Filter
    def input_filter_total_reps(self):
        return parse_positive_amount(input("Enter total reps: "))

    def input_filter_choice(self):
        return parse_choice(input("Enter choice: "), [1, 2])

    def handle_filter_workouts_by_reps(self):
        show_filter_menu()

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

    ## Flow
    def run(self):
        while True:
            show_menu()
            choice = self.input_menu_choice()

            if choice is None:
                print("Invalid choice")
                continue

            if choice == 6:
                print("Exiting...")
                break

            self.handle_menu_choice(choice)
