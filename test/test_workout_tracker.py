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


def test_get_total_workouts():
    tracker = WorkoutTracker()

    tracker.add_workout("Pushups", [15])
    tracker.add_workout("Squats", [20])

    assert tracker.get_total_workouts() == 2


def test_get_total_reps_returns_zero_when_empty():
    tracker = WorkoutTracker()

    assert tracker.get_total_reps() == 0


def test_get_total_reps_sums_all_sets():
    tracker = WorkoutTracker()

    tracker.add_workout("Pushups", [15, 12, 10])
    tracker.add_workout("Squats", [20, 18])

    assert tracker.get_total_reps() == 75


def test_get_total_reps_by_name_groups_duplicate_names():
    tracker = WorkoutTracker()

    tracker.add_workout("Pushups", [15, 12])
    tracker.add_workout("Squats", [20])
    tracker.add_workout("Pushups", [10, 8])

    assert tracker.get_total_reps_by_name() == {
        "Pushups": 45,
        "Squats": 20,
    }


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


def test_get_highest_total_reps_returns_none_when_empty():
    tracker = WorkoutTracker()

    assert tracker.get_highest_total_reps() is None


def test_get_lowest_total_reps_returns_none_when_empty():
    tracker = WorkoutTracker()

    assert tracker.get_lowest_total_reps() is None


def test_get_highest_total_reps_by_name_returns_none_when_empty():
    tracker = WorkoutTracker()

    assert tracker.get_highest_total_reps_by_name() is None


def test_get_lowest_total_reps_by_name_returns_none_when_empty():
    tracker = WorkoutTracker()

    assert tracker.get_lowest_total_reps_by_name() is None


def test_get_workout_with_highest_total_reps_returns_none_when_empty():
    tracker = WorkoutTracker()

    assert tracker.get_workout_with_highest_total_reps() is None


def test_highest_and_lowest_total_reps():
    tracker = WorkoutTracker()

    tracker.add_workout("Push", [10, 10, 5])   # 25
    tracker.add_workout("Pull", [8, 8])        # 16
    tracker.add_workout("Legs", [12, 12, 12])  # 36

    assert tracker.get_highest_total_reps() == 36
    assert tracker.get_lowest_total_reps() == 16

def test_highest_and_lowest_total_reps_by_name():
    tracker = WorkoutTracker()

    tracker.add_workout("Push", [10, 10])  # Push = 20
    tracker.add_workout("Push", [5])       # Push = 25
    tracker.add_workout("Pull", [8, 8])    # Pull = 16
    tracker.add_workout("Legs", [12])      # Legs = 12

    assert tracker.get_highest_total_reps_by_name() == 25
    assert tracker.get_lowest_total_reps_by_name() == 12


def test_get_workout_with_highest_total_reps_returns_workout():
    tracker = WorkoutTracker()

    tracker.add_workout("Push", [10, 10, 5])
    tracker.add_workout("Pull", [8, 8])
    tracker.add_workout("Legs", [12, 12, 12])

    workout = tracker.get_workout_with_highest_total_reps()

    assert workout is not None
    assert workout.name == "Legs"
    assert workout.reps == [12, 12, 12]

def test_get_workout_with_lowest_total_reps_when_first_is_lowest():
    tracker = WorkoutTracker()

    tracker.add_workout("Push", [5])
    tracker.add_workout("Pull", [10])
    tracker.add_workout("Legs", [12])

    workout = tracker.get_workout_with_lowest_total_reps()

    assert workout.name == "Push"
    assert workout.reps == [5]

def test_get_workout_with_lowest_total_reps():
    tracker = WorkoutTracker()

    tracker.add_workout("Push", [10, 10])
    tracker.add_workout("Pull", [5])
    tracker.add_workout("Legs", [12, 12])

    workout = tracker.get_workout_with_lowest_total_reps()

    assert workout.name == "Pull"
    assert workout.reps == [5]
