
def within_range(value, lower_bound, upper_bound):
    return not is_below_warning(value,lower_bound) and not is_above_warning(value,upper_bound)

def is_below_warning(value, warning_lower_limit):
    return value <= warning_lower_limit

def is_above_warning(value, warning_upper_limit):
    return value >= warning_upper_limit

def evaluate_out_of_range(value, lower_bound, upper_bound):
    return not within_range(value, lower_bound, upper_bound)
