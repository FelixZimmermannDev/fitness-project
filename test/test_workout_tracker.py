from backend.workout_tracker import WorkoutTracker


def test_add_workout():
    tracker = WorkoutTracker()

    result = tracker.add_workout("Pushups", [15, 12, 10])

    assert result is True
    assert len(tracker.get_workouts()) == 1
    assert tracker.get_workouts()[0].name == "Pushups"
    assert tracker.get_workouts()[0].reps == [15, 12, 10]


def test_has_workouts_returns_false_when_empty():
    tracker = WorkoutTracker()

    assert tracker.has_workouts() is False


def test_has_workouts_returns_true_when_not_empty():
    tracker = WorkoutTracker()

    tracker.add_workout("Pushups", [15])

    assert tracker.has_workouts() is True


def test_has_valid_index_with_valid_index():
    tracker = WorkoutTracker()

    tracker.add_workout("Pushups", [15])

    assert tracker.has_valid_index(0) is True


def test_has_valid_index_returns_false_for_too_large_index():
    tracker = WorkoutTracker()

    tracker.add_workout("Pushups", [15])

    assert tracker.has_valid_index(5) is False


def test_has_valid_index_returns_false_for_negative_index():
    tracker = WorkoutTracker()

    tracker.add_workout("Pushups", [15])

    assert tracker.has_valid_index(-1) is False


def test_remove_workout():
    tracker = WorkoutTracker()

    tracker.add_workout("Pushups", [15])

    result = tracker.remove_workout(0)

    assert result is True
    assert tracker.get_workouts() == []


def test_remove_workout_invalid_index():
    tracker = WorkoutTracker()

    tracker.add_workout("Pushups", [15])

    result = tracker.remove_workout(5)

    assert result is False
    assert len(tracker.get_workouts()) == 1


def test_update_workout():
    tracker = WorkoutTracker()

    tracker.add_workout("Pushups", [15])

    result = tracker.update_workout(0, [25, 20])

    assert result is True
    assert tracker.get_workouts()[0].reps == [25, 20]


def test_update_workout_invalid_index():
    tracker = WorkoutTracker()

    tracker.add_workout("Pushups", [15])

    result = tracker.update_workout(99, [25])

    assert result is False
    assert tracker.get_workouts()[0].reps == [15]


def test_rename_workout():
    tracker = WorkoutTracker()
    tracker.add_workout("Pushups", [15])

    result = tracker.rename_workout(0, "Pressups")

    assert result is True
    assert tracker.get_workouts()[0].name == "Pressups"


def test_rename_workout_invalid_index():
    tracker = WorkoutTracker()
    tracker.add_workout("Pushups", [15])

    result = tracker.rename_workout(5, "Pressups")

    assert result is False
    assert tracker.get_workouts()[0].name == "Pushups"


def test_get_workouts_by_name_returns_matching_workouts():
    tracker = WorkoutTracker()

    tracker.add_workout("Pushups", [15, 12])
    tracker.add_workout("Squats", [20])
    tracker.add_workout("Pushups", [10])

    results = tracker.get_workouts_by_name("Pushups")

    assert len(results) == 2
    assert results[0].name == "Pushups"
    assert results[0].reps == [15, 12]
    assert results[1].name == "Pushups"
    assert results[1].reps == [10]


def test_get_workouts_by_name_returns_empty_list_when_missing():
    tracker = WorkoutTracker()

    tracker.add_workout("Pushups", [15])

    assert tracker.get_workouts_by_name("Squats") == []


def test_has_workouts_by_name_returns_true_when_match_exists():
    tracker = WorkoutTracker()

    tracker.add_workout("Pushups", [15])

    assert tracker.has_workouts_by_name("Pushups") is True


def test_has_workouts_by_name_returns_false_when_missing():
    tracker = WorkoutTracker()

    tracker.add_workout("Pushups", [15])

    assert tracker.has_workouts_by_name("Squats") is False


def test_get_workouts_with_min_total_reps_returns_matching_workouts():
    tracker = WorkoutTracker()

    tracker.add_workout("Pushups", [15, 12])
    tracker.add_workout("Squats", [20, 20])
    tracker.add_workout("Pullups", [5, 5])

    results = tracker.get_workouts_with_min_total_reps(20)

    assert len(results) == 2
    assert results[0].name == "Pushups"
    assert results[1].name == "Squats"


def test_get_workouts_with_min_total_reps_returns_empty_list_when_missing():
    tracker = WorkoutTracker()

    tracker.add_workout("Pushups", [15, 12])
    tracker.add_workout("Pullups", [5, 5])

    assert tracker.get_workouts_with_min_total_reps(50) == []


def test_get_workouts_with_max_total_reps_returns_matching_workouts():
    tracker = WorkoutTracker()

    tracker.add_workout("Pushups", [15, 12])
    tracker.add_workout("Squats", [20, 20])
    tracker.add_workout("Pullups", [5, 5])

    results = tracker.get_workouts_with_max_total_reps(27)

    assert len(results) == 2
    assert results[0].name == "Pushups"
    assert results[1].name == "Pullups"


def test_get_workouts_with_max_total_reps_returns_empty_list_when_missing():
    tracker = WorkoutTracker()

    tracker.add_workout("Pushups", [15, 12])
    tracker.add_workout("Squats", [20, 20])

    assert tracker.get_workouts_with_max_total_reps(5) == []


def test_has_workouts_with_min_total_reps():
    tracker = WorkoutTracker()

    tracker.add_workout("Push", [10, 10, 5])
    tracker.add_workout("Pull", [8, 8])

    assert tracker.has_workouts_with_min_total_reps(20) is True
    assert tracker.has_workouts_with_min_total_reps(40) is False


def test_has_workouts_with_max_total_reps():
    tracker = WorkoutTracker()

    tracker.add_workout("Push", [10, 10, 5])
    tracker.add_workout("Pull", [8, 8])

    assert tracker.has_workouts_with_max_total_reps(20) is True
    assert tracker.has_workouts_with_max_total_reps(10) is False
