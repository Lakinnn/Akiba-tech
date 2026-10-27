print("====== Electricity Calculator ======")
def validate_units(units):
    if not isinstance(units, (int, float)) or isinstance(units, bool):
        raise ValueError("Units consumed must be a number.")

    if units < 0:
        raise ValueError("Units consumed cannot be negative.")

    return units


def calculate_tier_charges(units):
    units = validate_units(units)

    first_tier_units = min(units, 50)
    second_tier_units = min(max(units - 50, 0), 100)
    third_tier_units = max(units - 150, 0)

    return {
        "first_50": first_tier_units * 0.50,
        "next_100": second_tier_units * 0.75,
        "above_150": third_tier_units * 1.20
    }


def calculate_total_bill(units, service_fee=0):
    units = validate_units(units)

    if service_fee < 0:
        raise ValueError("Service fee cannot be negative.")

    tier_charges = calculate_tier_charges(units)
    usage_charge = sum(tier_charges.values())

    return usage_charge + service_fee


def generate_billing_summary(units, service_fee=0):
    units = validate_units(units)
    tier_charges = calculate_tier_charges(units)
    total_bill = calculate_total_bill(units, service_fee)

    return {
        "units_consumed": units,
        "first_50_charge": tier_charges["first_50"],
        "next_100_charge": tier_charges["next_100"],
        "above_150_charge": tier_charges["above_150"],
        "service_fee": service_fee,
        "total_bill": total_bill
    }


# Example
summary = generate_billing_summary(
    units=180,
    service_fee=10
)

for item, value in summary.items():
    if isinstance(value, (int, float)):
        print(f"{item}: {value:.2f} Birr")
    else:
        print(f"{item}: {value}")
