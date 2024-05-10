def validate_pin(pin: str) -> bool:
    return True if len(pin) == 4 and pin.isdigit() else False
