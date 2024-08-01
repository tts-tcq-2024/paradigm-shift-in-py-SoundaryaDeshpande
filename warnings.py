from utils import within_range, is_below_warning, is_above_warning, evaluate_out_of_range

def evaluate_warning(value, warning_lower_limit, warning_upper_limit):
    if is_below_warning(value, warning_lower_limit):
        return 'discharge'
    if is_above_warning(value, warning_upper_limit):
        return 'peak'
    return 'in_range'

def get_warning_status(value, lower_bound, upper_bound, warning_tolerance):
    warning_lower_limit = lower_bound + warning_tolerance
    warning_upper_limit = upper_bound - warning_tolerance
    
    if evaluate_out_of_range(value, lower_bound, upper_bound):
        return 'out_of_range'
    
    return evaluate_warning(value, warning_lower_limit, warning_upper_limit)

def print_warning(category, status):
    messages = {
        'discharge': f"Warning: {category} discharge",
        'peak': f"Warning: {category} peak",
        'out_of_range': f"Warning: {category} out of range",
        'in_range': f"Warning: {category} in range"
    }
    print(messages.get(status, messages['in_range']))
