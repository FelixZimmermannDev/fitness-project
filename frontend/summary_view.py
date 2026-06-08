#Show Summary
from frontend.formatters import format_workout

class SummaryView:

    def __init__(self, tracker, stats):
        self.tracker = tracker
        self.stats = stats

    def show_summary(self):
        if not self.tracker.has_workouts():
            print("No workouts available")
            return

        total_workouts = self.stats.get_total_workouts()
        total_reps = self.stats.get_total_reps()
        highest_total_reps = self.stats.get_highest_total_reps()
        lowest_total_reps = self.stats.get_lowest_total_reps()
        highest_total_reps_by_name = self.stats.get_highest_total_reps_by_name()
        lowest_total_reps_by_name = self.stats.get_lowest_total_reps_by_name()
        workout_with_highest_total_reps = self.stats.get_workout_with_highest_total_reps()
        workout_with_lowest_total_reps = self.stats.get_workout_with_lowest_total_reps()
        workout_with_most_sets = self.stats.get_workout_with_most_sets()
        workout_with_fewest_sets = self.stats.get_workout_with_fewest_sets()

        print(f"Total workouts: {total_workouts}")
        print(f"Total reps: {total_reps}")
        print(f"Highest total reps in one workout: {highest_total_reps}")
        print(f"Lowest total reps in one workout: {lowest_total_reps}")
        print(f"Highest total reps by name: {highest_total_reps_by_name}")
        print(f"Lowest total reps by name: {lowest_total_reps_by_name}")
        print(f"Workout with highest total reps: {format_workout(workout_with_highest_total_reps)}")
        print(f"Workout with lowest total reps: {format_workout(workout_with_lowest_total_reps)}")
        print(f"Workout with most sets: {format_workout(workout_with_most_sets)}")
        print(f"Workout with fewest sets: {format_workout(workout_with_fewest_sets)}")
        print()

        summary = self.stats.get_total_reps_by_name()

        for name, reps in summary.items():
            print(f"{name}: {reps} reps")
