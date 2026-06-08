from backend.workout_tracker import WorkoutTracker
from frontend.workout_view import WorkoutView


def test_show_workouts_prints_empty_message(capsys):
    view = WorkoutView()

    view.show_workouts([])

    assert capsys.readouterr().out == (
        "Current workouts:\n"
        "No current workouts\n"
    )


def test_show_workouts_prints_numbered_workouts(capsys):
    tracker = WorkoutTracker()
    tracker.add_workout("Pushups", [15, 12, 10])
    view = WorkoutView()

    view.show_workouts(tracker.get_workouts())

    assert capsys.readouterr().out == (
        "Current workouts:\n"
        "1. Pushups - 15, 12, 10 reps\n"
    )


def test_show_workout_results_prints_not_found_message(capsys):
    view = WorkoutView()

    view.show_workout_results([])

    assert capsys.readouterr().out == "Workout not found\n"


def test_show_workout_results_prints_matching_workouts(capsys):
    tracker = WorkoutTracker()
    tracker.add_workout("Pushups", [15, 12])
    tracker.add_workout("Pushups", [10])
    view = WorkoutView()

    view.show_workout_results(tracker.get_workouts())

    assert capsys.readouterr().out == (
        "Pushups - 15, 12 reps\n"
        "Pushups - 10 reps\n"
    )
