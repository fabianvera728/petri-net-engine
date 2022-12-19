from ..domain import PetriNet
from ..domain.place import Place
from ..domain.transition import Transition


class FromJsonToPetriNet:

    def __init__(self):
        pass

    def execute(self, petri_net_as_json) -> PetriNet:
        petri_net = PetriNet()
        try:
            for place in petri_net_as_json['places']:
                petri_net.add_place(Place(place['id'], place['name'], place['tokens']))
            for transition in petri_net_as_json['transitions']:
                petri_net.add_transition(Transition(transition['id'], transition['name']))
            for input in petri_net_as_json['inputs']:
                petri_net.add_input(input['place_id'], input['transition_id'], input['number'])
            for output in petri_net_as_json['outputs']:
                petri_net.add_output(output['transition_id'], output['place_id'], output['number'])
            petri_net.generate_inputs_matrix()
            petri_net.generate_outputs_matrix()
        except:
            raise Exception("Error in load data from json")
        return petri_net


