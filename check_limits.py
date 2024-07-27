def is_temperature_within_warning_range(temperature):
    lower_bound = 0
    upper_bound = 45
    warning_tolerance = 0.05 * upper_bound
    warning_lower_limit = lower_bound + warning_tolerance
    warning_upper_limit = upper_bound - warning_tolerance
    
    if temperature < lower_bound or temperature > upper_bound:
        return False
    elif temperature <= warning_lower_limit:
        return 'discharge'
    elif temperature >= warning_upper_limit:
        return 'peak'
    else:
        return 'in_range'

def is_soc_within_warning_range(soc):
    lower_bound = 20
    upper_bound = 80
    warning_tolerance = 0.05 * upper_bound
    warning_lower_limit = lower_bound + warning_tolerance
    warning_upper_limit = upper_bound - warning_tolerance
    
    if soc < lower_bound or soc > upper_bound:
        return False
    elif soc <= warning_lower_limit:
        return 'discharge'
    elif soc >= warning_upper_limit:
        return 'peak'
    else:
        return 'in_range'

def is_charge_rate_within_warning_range(charge_rate):
    lower_bound = 0
    upper_bound = 0.8
    warning_tolerance = 0.05 * upper_bound
    warning_lower_limit = lower_bound + warning_tolerance
    warning_upper_limit = upper_bound - warning_tolerance
    
    if charge_rate < lower_bound or charge_rate > upper_bound:
        return False
    elif charge_rate <= warning_lower_limit:
        return 'discharge'
    elif charge_rate >= warning_upper_limit:
        return 'peak'
    else:
        return 'in_range'

def print_warning(category, status):
    warnings = {
        'discharge': f"Warning: {category} discharge",
        'peak': f"Warning: {category} peak",
        'out_of_range': f"Warning: {category} out of range",
        'in_range': f"Warning: {category} in range"
    }
    print(warnings.get(status, warnings['in_range']))

def battery_is_ok(temperature, soc, charge_rate):
    temperature_status = is_temperature_within_warning_range(temperature)
    soc_status = is_soc_within_warning_range(soc)
    charge_rate_status = is_charge_rate_within_warning_range(charge_rate)

    # Print warnings for temperature
    if temperature_status is False:
        print_warning('temperature', 'out_of_range')
    else:
        print_warning('temperature', temperature_status)

    # Print warnings for SOC
    if soc_status is False:
        print_warning('SOC', 'out_of_range')
    else:
        print_warning('SOC', soc_status)

    # Print warnings for charge rate
    if charge_rate_status is False:
        print_warning('charge rate', 'out_of_range')
    else:
        print_warning('charge rate', charge_rate_status)

    return not (temperature_status is False or soc_status is False or charge_rate_status is False)

if __name__ == '__main__':
    # Testing the functions
    assert battery_is_ok(25, 70, 0.7) is True
    assert battery_is_ok(50, 85, 0) is False  # Expected to print warnings and fail the assertion if the function is not working as intended
