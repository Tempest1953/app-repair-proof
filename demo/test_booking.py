import unittest

import booking_after
import booking_before


class BookingRegressionTest(unittest.TestCase):
    def test_before_allows_double_booking(self):
        slots = {"2026-09-25T14:00:00Z"}
        self.assertTrue(booking_before.book(slots, "2026-09-25T15:00:00+01:00"))
        self.assertEqual(len(slots), 2)  # Demonstrates the bug.

    def test_after_rejects_equivalent_instant(self):
        slots = {"2026-09-25T14:00:00Z"}
        self.assertFalse(booking_after.book(slots, "2026-09-25T15:00:00+01:00"))
        self.assertEqual(len(slots), 1)

    def test_after_accepts_distinct_time(self):
        slots = {"2026-09-25T14:00:00Z"}
        self.assertTrue(booking_after.book(slots, "2026-09-25T16:00:00+01:00"))

    def test_after_requires_timezone(self):
        with self.assertRaisesRegex(ValueError, "timezone"):
            booking_after.book(set(), "2026-09-25T14:00:00")

    def test_after_rejects_malformed_time(self):
        with self.assertRaisesRegex(ValueError, "ISO 8601"):
            booking_after.book(set(), "tomorrow afternoon")


if __name__ == "__main__":
    unittest.main()
