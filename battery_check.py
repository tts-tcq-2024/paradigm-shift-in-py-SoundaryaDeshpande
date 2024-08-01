from warning_handler import get_warning_status, print_warning

def is_temperature_out_of_range(temperature):
    lower_bound = 0
    upper_bound = 45
    warning_tolerance = 0.05 * upper_bound
    status = get_warning_status(temperature, lower_bound, upper_bound, warning_tolerance)
    print_warning('temperature', status)
    return status == 'out_of_range'

def is_soc_out_of_range(soc):
    lower_bound = 20
    upper_bound = 80
    warning_tolerance = 0.05 * upper_bound
    status = get_warning_status(soc, lower_bound, upper_bound, warning_tolerance)
    print_warning('SOC', status)
    return status == 'out_of_range'

def is_charge_rate_out_of_range(charge_rate):
    lower_bound = 0
    upper_bound = 0.8
    warning_tolerance = 0.05 * upper_bound
    status = get_warning_status(charge_rate, lower_bound, upper_bound, warning_tolerance)
    print_warning('charge rate', status)
    return status == 'out_of_range'

def battery_is_ok(temperature, soc, charge_rate):
    return not (is_temperature_out_of_range(temperature) or is_soc_out_of_range(soc) or is_charge_rate_out_of_range(charge_rate))
