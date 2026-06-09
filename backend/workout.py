class Workout:

    def __init__(self, name, reps):
        self.name = name
        self.reps = reps

    def get_total_reps(self):
        return sum(self.reps)

    def get_set_count(self):
        return len(self.reps)
    # Name offensichtlich, version sowas wie leicht, mittel, schwer
    # Speater noch Kategorie
    # Speater noch Punktesystem

