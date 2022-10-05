import unittest

from src.petri_net_engine_fabianvera.domain import PetriNet
from src.petri_net_engine_fabianvera.domain.place import Place
from src.petri_net_engine_fabianvera.domain.transition import Transition


class PetriNetShould(unittest.TestCase):
    petri_net = PetriNet()

    def setUp(self) -> None:
        self.petri_net = PetriNet()
        self.petri_net.add_place(Place('1', 'P2', 4))
        self.petri_net.add_place(Place('2', 'P3', 5))
        self.petri_net.add_transition(Transition('1', 'T1'))
        self.petri_net.add_input('1', '1', 5)
        self.petri_net.add_input('2', '1', 1)
        self.petri_net.generate_inputs_matrix()
        self.petri_net.generate_outputs_matrix()

    def test_add_place(self):
        self.assertEqual(True, self.petri_net.add_place(Place('3', 'P1', 4)))

    def test_add_transition(self):
        self.assertEqual(True, self.petri_net.add_transition(Transition('2', 'T2')))

    def test_calculate_vector_of_markings(self):
        self.assertEqual([4, 5], self.petri_net.get_markings().tolist())

    def test_calculate_vector_of_places_by_transitions(self):
        self.assertEqual([5, 1], self.petri_net.get_inputs_matrix_for_transition('1'))


if __name__ == '__main__':
    unittest.main()
