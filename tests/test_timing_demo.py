import unittest

from demo.timing_demo import available_events, event_ledger, synthetic_example


class TimingTests(unittest.TestCase):
    def test_historical_anchor_does_not_make_event_available(self):
        _, events = synthetic_example()
        first = events[0]
        self.assertEqual(available_events(events, first["anchor_bar"]), [])
        self.assertEqual(available_events(events, first["confirmed_bar"] - 1), [])
        self.assertEqual(available_events(events, first["confirmed_bar"]), [first])

    def test_future_event_records_do_not_change_a_confirmed_prefix(self):
        _, events = synthetic_example()
        self.assertEqual(available_events(events, 28), available_events(events[:2], 28))
        self.assertEqual(available_events(events, 28), available_events(events[:-1] + [
            {"event_id": "replacement", "anchor_bar": 65, "confirmed_bar": 77}
        ], 28))

    def test_target_touching_split_is_purged_and_next_bar_starts_target(self):
        events = [{"event_id": "edge", "anchor_bar": 2, "confirmed_bar": 7}]
        row = event_ledger(events, n_bars=20, split_bar=10, horizon=3)[0]
        self.assertEqual(row["status"], "purged_at_split")
        self.assertEqual((row["target_start_bar"], row["target_end_bar"]), (8, 10))
        self.assertEqual(event_ledger(events, n_bars=20, split_bar=11, horizon=3)[0]["status"], "development")

    def test_complete_last_window_and_incomplete_window_are_distinct(self):
        events = [{"event_id": "last", "anchor_bar": 10, "confirmed_bar": 16}]
        self.assertEqual(event_ledger(events, n_bars=20, split_bar=10, horizon=3)[0]["status"], "holdout")
        self.assertEqual(event_ledger(events, n_bars=20, split_bar=10, horizon=4)[0]["status"], "excluded_incomplete_future")

    def test_invalid_timestamps_and_duplicate_ids_are_rejected(self):
        with self.assertRaises(ValueError):
            event_ledger([{"event_id": "bad", "anchor_bar": 6, "confirmed_bar": 5}], n_bars=20, split_bar=10, horizon=3)
        e = {"event_id": "same", "anchor_bar": 2, "confirmed_bar": 4}
        with self.assertRaises(ValueError):
            event_ledger([e, e], n_bars=20, split_bar=10, horizon=3)


if __name__ == "__main__":
    unittest.main()
