from backend.workout_stats import WorkoutStats
from backend.workout_tracker import WorkoutTracker
from frontend.summary_view import SummaryView


def create_summary_view(tracker):
    return SummaryView(tracker, WorkoutStats(tracker))


def test_show_summary_prints_totals_and_grouped_reps(capsys):
    tracker = WorkoutTracker()
    tracker.add_workout("Pushups", [15, 12])
    tracker.add_workout("Pushups", [10])
    tracker.add_workout("Squats", [20])
    summary_view = create_summary_view(tracker)

    summary_view.show_summary()

    output = capsys.readouterr().out

    assert "Total workouts: 3\n" in output
    assert "Total reps: 57\n" in output
    assert "Highest total reps in one workout: 27\n" in output
    assert "Lowest total reps in one workout: 10\n" in output
    assert "Highest total reps by name: 37\n" in output
    assert "Lowest total reps by name: 20\n" in output
    assert "Workout with highest total reps: Pushups - 15, 12 reps\n" in output
    assert "Workout with lowest total reps: Pushups - 10 reps\n" in output
    assert "Workout with most sets: Pushups - 15, 12 reps\n" in output
    assert "Workout with fewest sets: Pushups - 10 reps\n" in output
    assert "Pushups: 37 reps\n" in output
    assert "Squats: 20 reps\n" in output


def test_show_summary_prints_no_workouts_message(capsys):
    tracker = WorkoutTracker()
    summary_view = create_summary_view(tracker)

    summary_view.show_summary()

    assert capsys.readouterr().out == "No workouts available\n"
