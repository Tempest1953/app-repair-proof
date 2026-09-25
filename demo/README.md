# App Repair Proof: before and after

**Synthetic example, built for this demonstration.** It is not a client project, proof of bookings in a live system, or a security guarantee.

A booking app stored time slots as text. The same appointment could be written as `2026-09-25T14:00:00Z` and `2026-09-25T15:00:00+01:00`, so the prototype accepted two reservations for one instant. The repaired version parses timezone-aware timestamps and compares the actual instants. It rejects missing timezones and malformed timestamps.

Run from this directory with `python3 -m unittest -v test_booking.py`. The test named `test_before_allows_double_booking` intentionally confirms the original bug; the remaining tests exercise the repair.

**Limit:** This is an in-memory example. A real booking service also needs a database uniqueness rule or transactional lock to prevent simultaneous requests from taking one slot. We would inspect the real repository, reproduce its fault, and agree one fix before quoting.
