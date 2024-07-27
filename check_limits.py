def within_range(value, lower_bound, upper_bound):
    return lower_bound <= value <= upper_bound

def is_below_warning(value, lower_bound, warning_lower_limit):
    return value <= warning_lower_limit

def is_above_warning(value, upper_bound, warning_upper_limit):
    return value >= warning_upper_limit

def check_if_out_of_range(value, lower_bound, upper_bound):
    return value < lower_bound or value > upper_bound

def determine_warning_status(value, lower_bound, upper_bound, warning_tolerance):
    warning_lower_limit = lower_bound + warning_tolerance
    warning_upper_limit = upper_bound - warning_tolerance

    if check_if_out_of_range(value, lower_bound, upper_bound):
        return 'out_of_range'
    elif is_below_warning(value, lower_bound, warning_lower_limit):
        return 'discharge'
    elif is_above_warning(value, upper_bound, warning_upper_limit):
        return 'peak'
    else:
        return 'in_range'

def print_warning(category, status):
    messages = {
        'discharge': f"Warning: {category} discharge",'peak': f"Warning: {category} peak",'out_of_range': f"Warning: {category} out of range",'in_range': f"Warning: {category} in range"
    }
    print(messages.get(status, messages['in_range']))

def is_temperature_out_of_range(temperature):
    lower_bound = 0
    upper_bound = 45
    warning_tolerance = 0.05 * upper_bound
    status = determine_warning_status(temperature, lower_bound, upper_bound, warning_tolerance)
    print_warning('temperature', status)
    return status == 'out_of_range'

def is_soc_out_of_range(soc):
    lower_bound = 20
    upper_bound = 80
    warning_tolerance = 0.05 * upper_bound
    status = determine_warning_status(soc, lower_bound, upper_bound, warning_tolerance)
    print_warning('SOC', status)
    return status == 'out_of_range'

def is_charge_rate_out_of_range(charge_rate):
    lower_bound = 0
    upper_bound = 0.8
    warning_tolerance = 0.05 * upper_bound
    status = determine_warning_status(charge_rate, lower_bound, upper_bound, warning_tolerance)
    print_warning('charge rate', status)
    return status == 'out_of_range'

def battery_is_ok(temperature, soc, charge_rate):
    return not (is_temperature_out_of_range(temperature) or is_soc_out_of_range(soc) or is_charge_rate_out_of_range(charge_rate))

if __name__ == '__main__':
    assert battery_is_ok(25, 70, 0.7) is True
    assert battery_is_ok(50, 85, 0) is False
