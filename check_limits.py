def is_temperature_out_of_range(temperature):
    lower_bound = 0
    upper_bound = 45 
    warning_tolerance = 0.05 * upper_bound # 2.25
    warning_lower_limit = lower_bound + warning_tolerance # 2.25
    warning_upper_limit = upper_bound - warning_tolerance # 42.75
    
    if lower_bound <= temperature <= warning_lower_limit:
        print("Warning: temperature discharge")
        return True
    elif warning_upper_limit <= temperature <= upper_bound:
        print("Warning: temperature peak")
        return True
    elif temperature < lower_bound or temperature > upper_bound:
        print("Warning: temperature out of range")
        return True
    else:
        print("Warning: temperature in range")
        return False
def is_soc_out_of_range(soc):
    lower_bound = 20
    upper_bound = 80 
    warning_tolerance = 0.05 * upper_bound # 4
    warning_lower_limit = lower_bound + warning_tolerance # 24
    warning_upper_limit = upper_bound - warning_tolerance # 76
    
    if lower_bound <= soc <= warning_lower_limit:
        print("Warning: SOC discharge")
        return True
    elif warning_upper_limit <= soc <= upper_bound:
        print("Warning: SOC peak")
        return True
    elif soc < lower_bound or soc > upper_bound:
        print("Warning: SOC out of range")
        return True
    else:
        print("Warning: SOC in range")
        return False
def is_charge_rate_out_of_range(charge_rate):
    lower_bound = 0
    upper_bound = 0.8
    warning_tolerance = 0.05 * upper_bound # 0.04
    warning_lower_limit = lower_bound + warning_tolerance # 0.04
    warning_upper_limit = upper_bound - warning_tolerance # 0.76
    
    if lower_bound <= charge_rate <= warning_lower_limit:
        print("Warning: charge rate discharge")
        return True
    elif warning_upper_limit <= charge_rate <= upper_bound:
        print("Warning: charge rate peak")
        return True
    elif charge_rate < lower_bound or charge_rate > upper_bound:
        print("Warning: charge rate out of range")
        return True
    else:
        print("Warning: charge rate in range")
        return False
def battery_is_ok(temperature, soc, charge_rate):
    return not (is_temperature_out_of_range(temperature) or is_soc_out_of_range(soc) or is_charge_rate_out_of_range(charge_rate))
if __name__ == '__main__':
    assert battery_is_ok(25, 70, 0.7) is True
    assert battery_is_ok(50, 85, 0) is False
