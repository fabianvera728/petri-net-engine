import json
import os
import pathlib
import unittest
from ..src.petri_net_engine_fabianvera import FromJsonToPetriNet, PetriNetEngine, FromPetriNet
from ..src.petri_net_engine_fabianvera.domain.place import Place
from ..src.petri_net_engine_fabianvera.domain.transition import Transition


class PetriNetFromShould(unittest.TestCase):
    def test_build_from_json(self):
        path_tests_directory = os.path.dirname(os.path.abspath(__file__))
        with open(path_tests_directory + '/data/petri_net_as_json.json') as json_petri_net:
            petri_net_as_json = json.load(json_petri_net)
        builder_from_json = FromJsonToPetriNet()
        petri_net = builder_from_json.execute(petri_net_as_json=petri_net_as_json)
        petri_net_engine = PetriNetEngine(petri_net)
        self.assertEqual(True, petri_net_engine.is_enabled_transition('4c4e3831-9917-4d51-884b-5a7a3e64b458'))

    def test_build_from_petri_net(self):
        places = [
            Place(
                "41d4cb95-14bc-4648-84ae-8d535cdbd382",
                "P1",
                3
            ),
            Place(
                "e2bc0906-abf8-4e02-bba6-a242df1ff5ac",
                "P2",
                0
            )
        ]
        transitions = [
            Transition(
                "4c4e3831-9917-4d51-884b-5a7a3e64b458",
                "T1"
            )
        ]
        inputs = [[1, 0]]
        outputs = [[0, 1]]
        from_petri_net = FromPetriNet()
        petri_net = from_petri_net.execute(inputs=inputs, outputs=outputs, places=places, transitions=transitions)
        petri_net_engine = PetriNetEngine(petri_net)
        self.assertEqual(True, petri_net_engine.is_enabled_transition('4c4e3831-9917-4d51-884b-5a7a3e64b458'))


if __name__ == '__main__':
    unittest.main()
