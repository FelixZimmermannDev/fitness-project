from frontend.formatters import format_workout

class WorkoutView:

    def show_workouts(self, workouts):
        print("Current workouts:")

        if len(workouts) == 0:
            print("No current workouts")
            return

        for index, workout in enumerate(workouts, start=1):
            print(f"{index}. {format_workout(workout)}")

    def show_workout_results(self, results, empty_message="Workout not found"):
        if len(results) == 0:
            print(empty_message)
            return

        for workout in results:
            print(format_workout(workout))
