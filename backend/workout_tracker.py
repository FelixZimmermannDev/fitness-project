from backend.workout import Workout

class WorkoutTracker:

    def __init__(self):
        self.workouts = []

    #Show_Workouts
    def get_workouts(self):
        return self.workouts

    def has_workouts(self):
        return len(self.workouts) > 0

    #Add_Workout
    def add_workout(self, name, reps):
        workout = Workout(name, reps)

        self.workouts.append(workout)
        return True

    #Remove_Workout
    def has_valid_index(self, index):
        if index < 0:
            return False

        if index >= len(self.workouts):
            return False

        return True

    def remove_workout(self, index):
        if not self.has_valid_index(index):
            return False

        self.workouts.pop(index)
        return True

    #Update_Workout
    def update_workout(self, index, reps):
        if not self.has_valid_index(index):
            return False

        self.workouts[index].reps = reps
        return True

    #Summary_Workout
    def get_total_workouts(self):
        return len(self.workouts)

    def get_total_reps(self):
        total = 0

        for workout in self.workouts:
            total += sum(workout.reps)

        return total

    def get_total_reps_by_name(self):
        summary = {}

        for workout in self.workouts:
            if workout.name not in summary:
                summary[workout.name] = 0

            summary[workout.name] += sum(workout.reps)

        return summary

    #Search_Workout
    def get_workouts_by_name(self, name):

        results = []

        for workout in self.workouts:
            if workout.name == name:
                results.append(workout)

        return results

    def has_workouts_by_name(self, name):
        results = self.get_workouts_by_name(name)

        return len(results) > 0

    #Filter_Reps
    def get_workouts_with_min_total_reps(self, min_reps):
        results = []

        for workout in self.workouts:
            total_reps = sum(workout.reps)

            if total_reps >= min_reps:
                results.append(workout)

        return results

    def has_workouts_with_min_total_reps(self, min_reps):
        results = self.get_workouts_with_min_total_reps(min_reps)

        return len(results) > 0

    def get_workouts_with_max_total_reps(self, max_reps):
        results = []

        for workout in self.workouts:
            total_reps = sum(workout.reps)

            if total_reps <= max_reps:
                results.append(workout)

        return results

    def has_workouts_with_max_total_reps(self, max_reps):
        results = self.get_workouts_with_max_total_reps(max_reps)

        return len(results) > 0

    #Highest_Rep
    def get_highest_total_reps(self):
        if not self.has_workouts():
            return None

        highest = 0

        for workout in self.workouts:
            total = sum(workout.reps)   #Geht Liste durch

            if total > highest:
                highest = total

        return highest

    def get_highest_total_reps_by_name(self):
        if not self.has_workouts():
            return None

        summary = self.get_total_reps_by_name()
        return max(summary.values())

    #Lowest_Rep
    def get_lowest_total_reps(self):
        if not self.has_workouts():
            return None

        lowest = sum(self.workouts[0].reps)

        for workout in self.workouts:
            total = sum(workout.reps)

            if total < lowest:
                lowest = total

        return lowest

    def get_lowest_total_reps_by_name(self):
        if not self.has_workouts():
            return None

        summary = self.get_total_reps_by_name()
        return min(summary.values())

    #Drill 4 - Get Highest Workout
    def get_workout_with_highest_total_reps(self):
        if not self.has_workouts():
            return None

        highest = 0
        best_workout = None

        for workout in self.workouts:
            total = sum(workout.reps)   #Jeder Eintrag in Liste wird summiert

            if total > highest:
                highest = total
                best_workout = workout

        return best_workout

    def get_workout_with_lowest_total_reps(self):
        if not self.has_workouts():
            return None

        lowest = sum(self.workouts[0].reps)
        lowest_workout = self.workouts[0]

        for workout in self.workouts:
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

        for workout in self.workouts:
            set_count = len(workout.reps)

            if set_count > most_sets:
                most_sets = set_count
                best_workout = workout

        return best_workout

    def get_workout_with_fewest_sets(self):
        if not self.has_workouts():
            return None

        fewest_sets = len(self.workouts[0].reps)
        worst_workout = self.workouts[0]

        for workout in self.workouts:
            set_count = len(workout.reps)

            if set_count < fewest_sets:
                fewest_sets = set_count
                worst_workout = workout

        return worst_workout
