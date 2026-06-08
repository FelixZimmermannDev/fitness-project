from backend.workout_tracker import WorkoutTracker
from frontend.terminal_ui import TerminalUI


def create_ui():
    return TerminalUI(WorkoutTracker())


def test_input_menu_choice_returns_valid_choice(monkeypatch):
    ui = create_ui()
    monkeypatch.setattr("builtins.input", lambda _: "8")

    assert ui.input_menu_choice() == 8


def test_input_menu_choice_returns_none_for_invalid_choice(monkeypatch):
    ui = create_ui()
    monkeypatch.setattr("builtins.input", lambda _: "9")

    assert ui.input_menu_choice() is None


def test_input_workout_name_returns_parsed_name(monkeypatch):
    ui = create_ui()
    monkeypatch.setattr("builtins.input", lambda _: " pushups ")

    assert ui.input_workout_name() == "Pushups"


def test_input_workout_reps_returns_parsed_list(monkeypatch):
    ui = create_ui()
    monkeypatch.setattr("builtins.input", lambda _: "15 12 10")

    assert ui.input_workout_reps() == [15, 12, 10]


def test_show_workouts_prints_empty_message(capsys):
    ui = create_ui()

    ui.show_workouts()

    assert capsys.readouterr().out == (
        "Current workouts:\n"
        "No current workouts\n"
    )


def test_show_workouts_prints_numbered_workouts(capsys):
    tracker = WorkoutTracker()
    tracker.add_workout("Pushups", [15, 12, 10])
    ui = TerminalUI(tracker)

    ui.show_workouts()

    assert capsys.readouterr().out == (
        "Current workouts:\n"
        "1. Pushups - 15, 12, 10 reps\n"
    )


def test_show_menu_includes_search_and_filter_options(capsys):
    ui = create_ui()

    ui.show_menu()

    assert capsys.readouterr().out == (
        "Welcome to the Terminal UI!\n\n"
        "1. Add workout\n"
        "2. Remove workout\n"
        "3. Show workouts\n"
        "4. Change workouts\n"
        "5. Show summary\n"
        "6. Exit\n"
        "7. Search workout\n"
        "8. Filter by reps\n"
    )


def test_show_summary_prints_totals_and_grouped_reps(capsys):
    tracker = WorkoutTracker()
    tracker.add_workout("Pushups", [15, 12])
    tracker.add_workout("Pushups", [10])
    tracker.add_workout("Squats", [20])
    ui = TerminalUI(tracker)

    ui.show_summary()

    assert capsys.readouterr().out == (
        "Total workouts: 3\n"
        "Total reps: 57\n"
        "Highest total reps in one workout: 27\n"
        "Lowest total reps in one workout: 10\n"
        "Highest total reps by name: 37\n"
        "Lowest total reps by name: 20\n"
        "\n"
        "Pushups: 37 reps\n"
        "Squats: 20 reps\n"
    )


def test_show_summary_prints_no_workouts_message(capsys):
    ui = create_ui()

    ui.show_summary()

    assert capsys.readouterr().out == "No workouts available\n"


def test_input_search_workout_formats_valid_name(monkeypatch):
    ui = create_ui()
    monkeypatch.setattr("builtins.input", lambda _: " pushups ")

    assert ui.input_search_workout() == "Pushups"


def test_input_search_workout_rejects_multiple_words(monkeypatch, capsys):
    ui = create_ui()
    monkeypatch.setattr("builtins.input", lambda _: "push ups")

    assert ui.input_search_workout() is None
    assert capsys.readouterr().out == "Invalid workout name\n"


def test_handle_search_workout_prints_matching_workouts(monkeypatch, capsys):
    tracker = WorkoutTracker()
    tracker.add_workout("Pushups", [15, 12])
    tracker.add_workout("Pushups", [10])
    tracker.add_workout("Squats", [20])
    ui = TerminalUI(tracker)
    monkeypatch.setattr("builtins.input", lambda _: "pushups")

    ui.handle_search_workout()

    assert capsys.readouterr().out == (
        "Pushups - 15, 12 reps\n"
        "Pushups - 10 reps\n"
    )


def test_handle_search_workout_prints_not_found(monkeypatch, capsys):
    tracker = WorkoutTracker()
    tracker.add_workout("Pushups", [15])
    ui = TerminalUI(tracker)
    monkeypatch.setattr("builtins.input", lambda _: "squats")

    ui.handle_search_workout()

    assert capsys.readouterr().out == "Workout not found\n"


def test_show_filter_menu_prints_filter_options(capsys):
    ui = create_ui()

    ui.show_filter_menu()

    assert capsys.readouterr().out == (
        "1. Filter for minimum total reps\n"
        "2. Filter for maximum total reps\n"
    )


def test_handle_filter_workouts_by_reps_prints_min_results(monkeypatch, capsys):
    tracker = WorkoutTracker()
    tracker.add_workout("Pushups", [15, 12])
    tracker.add_workout("Squats", [20, 20])
    tracker.add_workout("Pullups", [5, 5])
    ui = TerminalUI(tracker)
    inputs = iter(["1", "20"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    ui.handle_filter_workouts_by_reps()

    assert capsys.readouterr().out == (
        "1. Filter for minimum total reps\n"
        "2. Filter for maximum total reps\n"
        "Pushups - 15, 12 reps\n"
        "Squats - 20, 20 reps\n"
    )


def test_handle_filter_workouts_by_reps_prints_max_results(monkeypatch, capsys):
    tracker = WorkoutTracker()
    tracker.add_workout("Pushups", [15, 12])
    tracker.add_workout("Squats", [20, 20])
    tracker.add_workout("Pullups", [5, 5])
    ui = TerminalUI(tracker)
    inputs = iter(["2", "27"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    ui.handle_filter_workouts_by_reps()

    assert capsys.readouterr().out == (
        "1. Filter for minimum total reps\n"
        "2. Filter for maximum total reps\n"
        "Pushups - 15, 12 reps\n"
        "Pullups - 5, 5 reps\n"
    )


def test_handle_filter_workouts_by_reps_prints_not_found(monkeypatch, capsys):
    tracker = WorkoutTracker()
    tracker.add_workout("Pushups", [15, 12])
    ui = TerminalUI(tracker)
    inputs = iter(["1", "50"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    ui.handle_filter_workouts_by_reps()

    assert capsys.readouterr().out == (
        "1. Filter for minimum total reps\n"
        "2. Filter for maximum total reps\n"
        "No workouts found\n"
    )


def test_handle_filter_workouts_by_reps_rejects_invalid_choice(monkeypatch, capsys):
    ui = create_ui()
    monkeypatch.setattr("builtins.input", lambda _: "3")

    ui.handle_filter_workouts_by_reps()

    assert capsys.readouterr().out == (
        "1. Filter for minimum total reps\n"
        "2. Filter for maximum total reps\n"
        "Invalid choice\n"
    )


def test_handle_filter_workouts_by_reps_rejects_invalid_reps(monkeypatch, capsys):
    ui = create_ui()
    inputs = iter(["1", "abc"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    ui.handle_filter_workouts_by_reps()

    assert capsys.readouterr().out == (
        "1. Filter for minimum total reps\n"
        "2. Filter for maximum total reps\n"
        "Invalid Reps\n"
    )
