from backend.workout import Workout

class WorkoutTracker:

    def __init__(self):
        self.workouts = []  #Hier stehen workout.reps und workout.name drin

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
        return len(self.workouts) #Returned anzahl der workouts gespeichert

    def get_total_reps(self):
        total = 0

        for workout in self.workouts:   #Geht liste durch
            total += sum(workout.reps)       #Added Total abhaengig wv reps in Liste stehen

        return total

    def get_total_reps_by_name(self):
        summary = {}

        for workout in self.workouts:
            if workout.name not in summary:
                summary[workout.name] = 0

            summary[workout.name] += sum(workout.reps)

        return summary
