from backend.workout_tracker import WorkoutTracker


def test_add_workout():
    tracker = WorkoutTracker()

    result = tracker.add_workout("pushups", 15)

    assert result is True
    assert len(tracker.get_workouts()) == 1


def test_has_workouts_returns_false_when_empty():
    tracker = WorkoutTracker()

    assert tracker.has_workouts() is False


def test_has_workouts_returns_true_when_not_empty():
    tracker = WorkoutTracker()

    tracker.add_workout("pushups", 15)

    assert tracker.has_workouts() is True


def test_can_remove_workout_with_valid_index():
    tracker = WorkoutTracker()

    tracker.add_workout("pushups", 15)

    assert tracker.can_remove_workout(0) is True


def test_can_remove_workout_with_invalid_index():
    tracker = WorkoutTracker()

    tracker.add_workout("pushups", 15)

    assert tracker.can_remove_workout(5) is False


def test_remove_workout():
    tracker = WorkoutTracker()

    tracker.add_workout("pushups", 15)

    result = tracker.remove_workout(0)

    assert result is True
    assert len(tracker.get_workouts()) == 0


def test_remove_workout_invalid_index():
    tracker = WorkoutTracker()

    tracker.add_workout("pushups", 15)

    result = tracker.remove_workout(5)

    assert result is False
    assert len(tracker.get_workouts()) == 1
