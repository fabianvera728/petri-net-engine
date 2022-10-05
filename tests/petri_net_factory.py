import unittest

from src.petri_net_engine_fabianvera import PetriNetFactory, PetriNetEngine


class PetriNetFactoryShould(unittest.TestCase):

    def test_build_petri_net(self):
        petri_net = PetriNetFactory.build()
        petri_net_engine = CreatePetriNetEngine().execute(petri_net)
        petri_net.add_place({'name': 'P1', 'tokens': 2})
        self.assertEqual(True, petri_net.add_place({'name': 'P1', 'tokens': 2}))

    def test_build_petri_net_from_json(self):
        petri_net = PetriNetFactory.build()
        petri_net_engine = CreatePetriNetEngine().execute(petri_net)
        petri_net.add_place({'name': 'P1', 'tokens': 2})
        self.assertEqual(True, petri_net.add_place({'name': 'P1', 'tokens': 2}))


class CreatePetriNetEngine:
    petri_net_creator = PetriNetEngine

    def execute(self, petri_net):
        return self.petri_net_creator(petri_net)


if __name__ == '__main__':
    unittest.main()
