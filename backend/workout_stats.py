#Auswertung von Workouts

class WorkoutStats:

    def __init__(self, tracker):
        self.tracker = tracker

    def has_workouts(self):
        return self.tracker.has_workouts()

    def get_workouts(self):
        return self.tracker.get_workouts()
    def get_total_workouts(self):
        return len(self.get_workouts())

    def get_total_reps(self):
        total = 0

        for workout in self.get_workouts():
            total += sum(workout.reps)

        return total
    def get_total_reps_by_name(self):
        summary = {}

        for workout in self.get_workouts():
            if workout.name not in summary:
                summary[workout.name] = 0

            summary[workout.name] += sum(workout.reps)

        return summary

    def get_highest_total_reps(self):
        if not self.has_workouts():
            return None

        highest = 0

        for workout in self.get_workouts():
            total = sum(workout.reps)

            if total > highest:
                highest = total

        return highest
    def get_highest_total_reps_by_name(self):
        if not self.has_workouts():
            return None

        summary = self.get_total_reps_by_name()
        return max(summary.values())

    def get_lowest_total_reps(self):
        if not self.has_workouts():
            return None

        lowest = sum(self.get_workouts()[0].reps)

        for workout in self.get_workouts():
            total = sum(workout.reps)

            if total < lowest:
                lowest = total

        return lowest
    def get_lowest_total_reps_by_name(self):
        if not self.has_workouts():
            return None

        summary = self.get_total_reps_by_name()
        return min(summary.values())

    def get_workout_with_highest_total_reps(self):
        if not self.has_workouts():
            return None

        highest = 0
        best_workout = None

        for workout in self.get_workouts():
            total = sum(workout.reps)

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
            total = sum(workout.reps)

            if total < lowest:
                lowest = total
                lowest_workout = workout

        return lowest_workout

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
