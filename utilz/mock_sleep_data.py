def get_mock_sleep_data():
    current_data = {
        "Monday": 7.5,
        "Tuesday": 6.0,
        "Wednesday": 8.0,
        "Thursday": 7.0,
        "Friday": 5.5,
        "Saturday": 8.5,
        "Sunday": 9.0
    }

    improvement_factor = 1.1

    projected_data = {day: round(hours * improvement_factor, 1) for day, hours in current_data.items()}

    return current_data, projected_data

def get_last_night_sleep_duration():
    return 7.5  # hours

def get_last_night_sleep_phases():
    return {
        "REM": 1.5,
        "Light Sleep": 3.0,
        "Deep Sleep": 2.0,
        "Awake": 1.0
    }

def get_last_night_sleep_distribution():
    return {
        "12 AM": "Awake",
        "1 AM": "Light Sleep",
        "2 AM": "Light Sleep",
        "3 AM": "Deep Sleep",
        "4 AM": "Deep Sleep",
        "5 AM": "REM",
        "6 AM": "REM",
        "7 AM": "Awake"
    }

def get_last_week_sleep_data():
    return {
        "Monday": 6.5,
        "Tuesday": 6.0,
        "Wednesday": 7.0,
        "Thursday": 5.5,
        "Friday": 6.5,
        "Saturday": 8.0,
        "Sunday": 7.5
    }

def simulate_improved_sleep_data():
    last_week_data = get_last_week_sleep_data()
    improvement_factor = 1.1

    improved_data = {day: round(hours * improvement_factor, 1) for day, hours in last_week_data.items()}
    return improved_data