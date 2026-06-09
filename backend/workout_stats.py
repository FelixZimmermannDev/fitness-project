#Auswertung von Daten
from backend import workout


class WorkoutStats:

    def __init__(self, tracker, reps):
        self.tracker = tracker

    ## Helpers
    def has_workouts(self):
        return self.tracker.has_workouts()

    def get_workouts(self):
        return self.tracker.get_workouts()

    ## Totals
    def get_total_workouts(self):
        return len(self.get_workouts())

    def get_total_reps(self):
        total = 0

        for workout in self.get_workouts():
            total += self.tracker.get_total_reps()

        return total

    ## By Name
    def get_total_reps_by_name(self):
        summary = {}

        for workout in self.get_workouts():
            if workout.name not in summary:
                summary[workout.name] = 0

            summary[workout.name] += workout.get_total_reps()

        return summary

    def get_highest_total_reps_by_name(self):
        if not self.has_workouts():
            return None

        summary = self.get_total_reps_by_name()
        return max(summary.values())

    def get_lowest_total_reps_by_name(self):
        if not self.has_workouts():
            return None

        summary = self.get_total_reps_by_name()
        return min(summary.values())

    ## By Reps
    def get_highest_total_reps(self):
        if not self.has_workouts():
            return None

        highest = 0

        for workout in self.get_workouts():
            total = workout.get_total_reps()

            if total > highest:
                highest = total

        return highest

    def get_lowest_total_reps(self):
        if not self.has_workouts():
            return None

        lowest = sum(self.get_workouts()[0].reps)

        for workout in self.get_workouts():
            total = workout.get_total_reps()

            if total < lowest:
                lowest = total

        return lowest

    ## Workout Selection
    def get_workout_with_highest_total_reps(self):
        if not self.has_workouts():
            return None

        highest = 0
        best_workout = None

        for workout in self.get_workouts():
            total = workout.get_total_reps()

            if total > highest:
                highest = total
                best_workout = workout

        return best_workout

    def get_workout_with_lowest_total_reps(self):
        if not self.has_workouts():
            return None

        lowest = sum(self.get_workouts()[0].reps)
        lowest_workout = self.get_workouts()[0]

        for workout in self.get_workouts():
            total = workout.get_total_reps()

            if total < lowest:
                lowest = total
                lowest_workout = workout

        return lowest_workout

    ## Set Selection
    def get_workout_with_most_sets(self):
        if not self.has_workouts():
            return None

        most_sets = 0
        best_workout = None

        for workout in self.get_workouts():
            set_count = len(workout.reps)

            if set_count > most_sets:
                most_sets = set_count
                best_workout = workout

        return best_workout

    def get_workout_with_fewest_sets(self):
        if not self.has_workouts():
            return None

        fewest_sets = len(self.get_workouts()[0].reps)
        worst_workout = self.get_workouts()[0]

        for workout in self.get_workouts():
            set_count = len(workout.reps)

            if set_count < fewest_sets:
                fewest_sets = set_count
                worst_workout = workout

        return worst_workout
