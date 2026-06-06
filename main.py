
from backend.workout_tracker import WorkoutTracker
from frontend.terminal_ui import TerminalUI

def main():
    workout = WorkoutTracker()
    terminal_ui = TerminalUI(workout)
    terminal_ui.run()

if __name__ == "__main__":
    main()
