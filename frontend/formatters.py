#Formattierung

def format_workout(workout):
    reps_text = ", ".join(str(rep) for rep in workout.reps)
    return f"{workout.name} - {reps_text} reps"

