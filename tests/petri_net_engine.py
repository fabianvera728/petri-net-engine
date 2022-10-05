import unittest

from src.petri_net_engine_fabianvera.domain import PetriNetEngine, PetriNet
from src.petri_net_engine_fabianvera.domain.place import Place
from src.petri_net_engine_fabianvera.domain.transition import Transition


class PetriNetEngineShould(unittest.TestCase):
    petri_net = PetriNet()
    petri_net_engine = PetriNetEngine(petri_net)

    def setUp(self) -> None:
        self.petri_net = PetriNet()
        self.petri_net_engine = PetriNetEngine(self.petri_net)
        self.petri_net.add_place(Place('1', 'P1', 1))
        self.petri_net.add_place(Place('2', 'P2', 0))
        self.petri_net.add_place(Place('3', 'P3', 0))
        self.petri_net.add_place(Place('4', 'P4', 2))
        self.petri_net.add_place(Place('5', 'P5', 1))
        self.petri_net.add_transition(Transition('1', 'T1'))
        self.petri_net.add_transition(Transition('2', 'T2'))
        self.petri_net.add_transition(Transition('3', 'T3'))
        self.petri_net.add_transition(Transition('4', 'T4'))
        self.petri_net.add_input('1', '1', 1)
        self.petri_net.add_input('2', '2', 1)
        self.petri_net.add_input('3', '2', 1)
        self.petri_net.add_input('4', '2', 1)
        self.petri_net.add_input('4', '3', 2)
        self.petri_net.add_input('5', '4', 1)
        self.petri_net.add_output('1', '2', 1)
        self.petri_net.add_output('1', '3', 1)
        self.petri_net.add_output('1', '4', 2)
        self.petri_net.add_output('2', '2', 1)
        self.petri_net.add_output('3', '5', 1)
        self.petri_net.add_output('4', '4', 1)
        self.petri_net.add_output('4', '3', 1)
        self.petri_net.generate_inputs_matrix()
        self.petri_net.generate_outputs_matrix()

    def test_is_not_enabled_transition(self):
        self.assertEqual(False, self.petri_net_engine.is_enabled_transition('2'))

    def test_is_enabled_transition(self):
        self.assertEqual(True, self.petri_net_engine.is_enabled_transition('1'))

    def test_is_enabled_multiple_transitions(self):
        self.assertEqual(True, self.petri_net_engine.is_enabled_transition('4', '1', '3'))

    def test_is_not_enabled_multiple_transitions(self):
        self.assertEqual(False, self.petri_net_engine.is_enabled_transition('4', '2', '3'))

    def test_fire_transitions(self):
        new_marking = self.petri_net_engine.fire_transitions('4')
        self.assertEqual([1, 0, 1, 3, 0], new_marking.tolist())

    def test_fire_transition_disabled_raise_exception(self):
        with self.assertRaises(Exception):
            self.petri_net_engine.fire_transitions('T2')

    def test_fire_burst_transitions(self):
        new_marking = self.petri_net_engine.fire_transitions('4', '1', '3')
        self.assertEqual([0, 1, 2, 3, 1], new_marking.tolist())


if __name__ == '__main__':
    unittest.main()
