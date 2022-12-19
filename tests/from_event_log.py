import os
import unittest
from ..src.petri_net_engine_fabianvera.application.from_event_log_to_petri_net import FromEventLogToPetriNet


class FromEventLogToPetriNetShould(unittest.TestCase):
    def test_build_petri_net_from_event_log(self):
        path_tests_directory = os.path.dirname(os.path.abspath(__file__))
        event_log = FromEventLogToPetriNet()
        petri_net = event_log.execute(path_tests_directory + '/data/event_log.csv')
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
