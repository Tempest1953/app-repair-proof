"""Synthetic booking app after the repair. In-memory demonstration only."""

from datetime import datetime, timezone


def normalize_slot(slot):
    if not isinstance(slot, str):
        raise ValueError("A timestamp with a timezone is required")
    try:
        parsed = datetime.fromisoformat(slot.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError("Use an ISO 8601 timestamp") from exc
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ValueError("A timezone is required")
    return parsed.astimezone(timezone.utc)


def book(existing_slots, requested_slot):
    requested = normalize_slot(requested_slot)
    if any(normalize_slot(slot) == requested for slot in existing_slots):
        return False
    existing_slots.add(requested_slot)
    return True
