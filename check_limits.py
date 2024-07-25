
def is_temperature_out_of_range(temperature):
    return temperature < 0 or temperature > 45
def is_soc_out_of_range(soc):
    return soc < 20 or soc > 80
def is_charge_rate_out_of_range(charge_rate):
    return charge_rate > 0.8
def get_soc_warning_message(soc):
    if 20<=soc<=24:
        return "Warning: SOC approaching discharge"
    elif 76<=soc<=80:
        return "Warning : SOC approaching charge peak"
    else:
        return None
def get_temperature_warning_message(temperature):
    if 0<=temperature<=2.25:
        return "Warning: Temperature approaching to maximum limit"
    elif 42.75<=temperature<=45:
        return "Warning : Temperature approaching to minimum limit"
    else:
        return None
def get_chargerate_warning_message(charge_rate):
    if 0<=charge_rate<=0.04:
        return "Warning: Charge rate approaching to maximum limit"
    elif 0.76<=charge_rate<=0.8:
        return "Warning : Charge rate approaching to minimum limit"
    else:
        return None
def battery_is_ok(temperature, soc, charge_rate):
    warnings=[]
    if is_temperature_out_of_range(temperature):
        warning=get_temperature_warning_message(temperature)
        if warning:
            warnings.append(warning)
        print(f"Temaperature is out of range :{temperature}")

    if is_soc_out_of_range(soc):
        warning=get_soc_warning_message(soc)
        if warning:
            warnings.append(warning)
        print(f"SOC is out of range :{soc}")
    if is_charge_rate_out_of_range(charge_rate):
        warning=get_chargerate_warning_message(charge_rate)
        if warning:
            warnings.append(warning)
        print(f"Chargerate is out of range :{charge_rate}")
    if warnings:
        for warning in warnings:
            print(warning)
    return not warnings
if __name__ == '__main__':
    assert battery_is_ok(25, 70, 0.7) is True
    assert battery_is_ok(50, 85, 0) is False
