from backend.workout_tracker import WorkoutTracker
from backend.workout_stats import WorkoutStats


def create_stats():
    tracker = WorkoutTracker()
    tracker.add_workout("Pushups", [15, 12])
    tracker.add_workout("Squats", [20, 20])
    tracker.add_workout("Pullups", [5, 5, 5])
    return WorkoutStats(tracker)


def test_get_total_workouts():
    stats = create_stats()

    assert stats.get_total_workouts() == 3


def test_get_total_reps():
    stats = create_stats()

    assert stats.get_total_reps() == 82


def test_get_total_reps_by_name():
    stats = create_stats()

    assert stats.get_total_reps_by_name() == {
        "Pushups": 27,
        "Squats": 40,
        "Pullups": 15,
    }


def test_get_highest_and_lowest_total_reps():
    stats = create_stats()

    assert stats.get_highest_total_reps() == 40
    assert stats.get_lowest_total_reps() == 15


def test_get_highest_and_lowest_total_reps_by_name():
    stats = create_stats()

    assert stats.get_highest_total_reps_by_name() == 40
    assert stats.get_lowest_total_reps_by_name() == 15


def test_get_workout_with_highest_and_lowest_total_reps():
    stats = create_stats()

    highest = stats.get_workout_with_highest_total_reps()
    lowest = stats.get_workout_with_lowest_total_reps()

    assert highest.name == "Squats"
    assert highest.reps == [20, 20]
    assert lowest.name == "Pullups"
    assert lowest.reps == [5, 5, 5]


def test_get_workout_with_most_and_fewest_sets():
    stats = create_stats()

    most_sets = stats.get_workout_with_most_sets()
    fewest_sets = stats.get_workout_with_fewest_sets()

    assert most_sets.name == "Pullups"
    assert most_sets.reps == [5, 5, 5]
    assert fewest_sets.name == "Pushups"
    assert fewest_sets.reps == [15, 12]


def test_empty_stats_returns_none():
    tracker = WorkoutTracker()
    stats = WorkoutStats(tracker)

    assert stats.get_highest_total_reps() is None
    assert stats.get_lowest_total_reps() is None
    assert stats.get_highest_total_reps_by_name() is None
    assert stats.get_lowest_total_reps_by_name() is None
    assert stats.get_workout_with_highest_total_reps() is None
    assert stats.get_workout_with_lowest_total_reps() is None
    assert stats.get_workout_with_most_sets() is None
    assert stats.get_workout_with_fewest_sets() is None
