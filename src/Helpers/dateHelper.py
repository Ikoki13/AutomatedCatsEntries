from datetime import datetime, timezone, date


def get_formatted_date(prompt: str, default_date: date = date.today()) -> datetime:
    """
    Prompts the user for a date and returns a datetime object.

    Args:
        prompt (str): The prompt message for the user.
        default_date (date): The default date to use if no input is provided.

    Returns:
        datetime: A datetime object parsed from user input or the default date.
    """
    user_input = input(prompt)
    if not user_input:
        return datetime.combine(default_date, datetime.min.time()).replace(tzinfo=timezone.utc)

    date_format = "%d.%m.%Y"
    try:
        return datetime.strptime(user_input, date_format)
    except ValueError:
        print(f"❌ Invalid date format '{user_input}'. Please use '{date_format}'.")
        return get_formatted_date(prompt, default_date)


def calculate_date_difference(start_dt: datetime, end_dt: datetime) -> int:
    """
    Calculates the difference in days between two datetime objects.
    Args:
        start_dt (datetime): The start datetime object.
        end_dt (datetime): The end datetime object.
    Returns:
        int: The number of days between the start and end date.
    """
    # The original logic is perfect, no need to change
    return (end_dt - start_dt).days
