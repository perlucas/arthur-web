ACCEPTED_LOCATIONS = [
    'AR',  # Argentina
    'US',  # United States
    'PE',  # Peru
    'BR',  # Brazil
    'CA',  # Canada
    'MX',  # Mexico
    'CO',  # Colombia
    'CL',  # Chile
    'EC',  # Ecuador
    'CR',  # Costa Rica
    'PA',  # Panama
    'UY',  # Uruguay
    'BO',  # Bolivia
    'PY',  # Paraguay
    'SV',  # El Salvador
    'BS',  # Bahamas
]

def is_valid_location(location: str) -> str:
    if location not in ACCEPTED_LOCATIONS:
        raise ValueError(f'{location} not valid')
    return location