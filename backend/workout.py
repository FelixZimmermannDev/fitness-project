class Workout:

    def __init__(self, name, reps):
        self.name = name
        self.reps = reps

    def get_total_reps(self):
        return sum(self.reps)

        #Name offensichtlich, version sowas wie leicht, mittel, schwer
        #Speater noch Kategorie
        #Speater noch Punktesystem.

        #Aktuell ist Workout der simple name. Execution durch Workout(Pushup, 15)

        #Entweder Workout(Pushups, Reps) als einzelnes wie hier oder als ganzes Workout, also Pushups, Version A(10 Reps) oder so. Variante fuer spaeter
