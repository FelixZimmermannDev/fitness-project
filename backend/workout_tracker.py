from backend.workout import Workout
#Verwaltet Daten

class WorkoutTracker:

    def __init__(self):
        self.workouts = []

    ## Helpers
    def get_workouts(self):
        return self.workouts

    def has_workouts(self):
        return len(self.workouts) > 0

    ## Add
    def add_workout(self, name, reps):
        workout = Workout(name, reps)

        self.workouts.append(workout)
        return True

    ## Remove / Update
    def has_valid_index(self, index):   #Workout Liste hat Eintraege
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

    def update_workout(self, index, reps):
        if not self.has_valid_index(index):
            return False

        self.workouts[index].reps = reps
        return True

    ## Rename
    def rename_workout(self, index, new_name):
        if not self.has_valid_index(index):
            return False

        self.workouts[index].name = new_name
        return True

    ## Search
    def get_workouts_by_name(self, name):

        results = []

        for workout in self.workouts:
            if workout.name == name:
                results.append(workout)

        return results

    def has_workouts_by_name(self, name):
        results = self.get_workouts_by_name(name)

        return len(results) > 0

    ## Filter
    def get_workouts_with_min_total_reps(self, min_reps):
        results = []

        for workout in self.workouts:
            total_reps = workout.get_total_reps()

            if total_reps >= min_reps:
                results.append(workout)

        return results

    def has_workouts_with_min_total_reps(self, min_reps):
        results = self.get_workouts_with_min_total_reps(min_reps)

        return len(results) > 0

    def get_workouts_with_max_total_reps(self, max_reps):
        results = []

        for workout in self.workouts:
            total_reps = workout.get_total_reps()

            if total_reps <= max_reps:
                results.append(workout)

        return results

    def has_workouts_with_max_total_reps(self, max_reps):
        results = self.get_workouts_with_max_total_reps(max_reps)

        return len(results) > 0
