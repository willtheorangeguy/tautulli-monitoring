import unittest
from metrics_relay import sanitize


class PrivacyTests(unittest.TestCase):
    def test_drops_identity_and_unknown_families(self):
        raw = 'tautulli_up 1\ntautulli_session_count 2\ntautulli_session_info{user="alice",title="private",ip="1.2.3.4"} 99\nnew_metric{title="private"} 1\n'
        result = sanitize(raw)
        self.assertIn('tautulli_sessions_active 2', result)
        self.assertNotIn('alice', result)
        self.assertNotIn('private', result)
        self.assertNotIn('1.2.3.4', result)

    def test_unexpected_identity_on_inventory_fails_closed(self):
        with self.assertRaises(ValueError):
            sanitize('tautulli_up 1\ntautulli_library_items{name="Movies",type="movie",user="alice"} 10\n')

    def test_preserves_real_library_value_and_missing_optional_data(self):
        result = sanitize('tautulli_up 1\ntautulli_library_items{name="Movies",type="movie"} 42\n')
        self.assertIn(' 42', result)
        self.assertNotIn('tautulli_library_size_bytes', result)

    def test_requires_upstream_health(self):
        with self.assertRaises(ValueError):
            sanitize('tautulli_session_count 0\n')


if __name__ == '__main__':
    unittest.main()
