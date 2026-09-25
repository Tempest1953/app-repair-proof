"""Synthetic booking app before the repair."""


def book(existing_slots, requested_slot):
    # A common prototype shortcut: compare timestamp text instead of instants.
    if requested_slot in existing_slots:
        return False
    existing_slots.add(requested_slot)
    return True
