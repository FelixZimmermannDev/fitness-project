from backend.workout import Workout


def test_get_total_reps_sums_all_sets():
    workout = Workout("Pushups", [15, 12, 10])

    assert workout.get_total_reps() == 37


def test_get_total_reps_returns_zero_for_empty_sets():
    workout = Workout("Pushups", [])

    assert workout.get_total_reps() == 0
