from datetime import date


def strval(data: dict, name: str) -> str | None:
    value = data.get(name, None)
    return str(value) if value is not None else None


def intval(data: dict, name: str) -> int | None:
    value = data.get(name, None)
    return int(value) if value is not None else None


def floatval(data: dict, name: str) -> float | None:
    value = data.get(name, None)
    return float(value) if value is not None else None


def boolval(data: dict, name: str) -> bool | None:
    value = intval(data, name)
    return bool(value) if value is not None else None


def dateval(data: dict, name: str) -> date | None:
    value = data.get(name, None)
    return date.fromisoformat(value) if value is not None else None
