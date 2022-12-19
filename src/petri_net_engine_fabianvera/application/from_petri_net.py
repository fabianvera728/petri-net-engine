from ..domain import PetriNet


class FromPetriNet:

    def __init__(self):
        pass

    def execute(self, inputs, outputs, places, transitions) -> PetriNet:
        petri_net = PetriNet()
        petri_net.inputs_matrix = inputs
        petri_net.outputs_matrix = outputs
        petri_net.places = places
        petri_net.transitions = transitions
        petri_net.generate_places_as_dict()
        petri_net.generate_transitions_as_dict()
        petri_net.generate_markings()
        return petri_net
