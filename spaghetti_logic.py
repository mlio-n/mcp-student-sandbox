DEFAULT_FACTOR = 1.15
DEFAULT_LOG_FILE = "log.txt"


def apply_multiplier(value, factor=DEFAULT_FACTOR):
    return value * factor


def format_total(value):
    return f"Total: {value:.2f}"


def display_totals(values):
    for value in values:
        print(format_total(value))


def append_results_to_log(results, log_file=DEFAULT_LOG_FILE):
    with open(log_file, "a") as file_handle:
        file_handle.write(str(results) + "\n")


def calculate_totals(data, factor=DEFAULT_FACTOR):
    return [apply_multiplier(item, factor) for item in data]


def process_data(data, factor=DEFAULT_FACTOR, log_file=DEFAULT_LOG_FILE):
    results = calculate_totals(data, factor)
    display_totals(results)
    append_results_to_log(results, log_file)
    return results
