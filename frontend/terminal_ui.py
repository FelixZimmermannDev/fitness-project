class TerminalUI:

    def __init__(self, tracker):
        self.tracker = tracker

    #Parse
    def parse_amount(self, user_input):
        user_input = user_input.strip()

        try:
            return int(user_input)

        except ValueError:
            return None

    #Userchoice
    def show_menu(self):
        print("Welcome to the Terminal UI!\n")
        print("1. Add workout")
        print("2. Remove workout")
        print("3. Show workouts")
        print("4. Change workouts")
        print("5. Exit")

    def show_workouts(self):
        print("Current workouts:")

        for workout in self.tracker.workouts:
            print(workout)

    def input_menu_choice(self):
        return self.parse_amount(input("Enter menu choice: "))

    def handle_menu_choice(self, choice):
        if choice == 1:
            self.handle_add_workout()
        if choice == 2:
            pass
        if choice == 3:
            self.show_workouts()

    #Add_Workout
    def input_workout_name(self):
        return input("Enter workout name: ")

    def input_workout_reps(self):
        return self.parse_amount(input("Enter workout reps: "))

    def handle_add_workout(self):
        name = self.input_workout_name().strip().lower()
        reps = self.input_workout_reps()

        if reps is None:
            print("Invalid Reps")
            return

        self.tracker.add_workout(name, reps)
        print("Workout added!")



    #Flow
    def run(self):
        while True:
            self.show_menu()
            choice = self.input_menu_choice()

            if choice is None:
                print("Invalid choice!")
                continue

            if choice == 5:
                print("Exiting...")
                break

            self.handle_menu_choice(choice)


