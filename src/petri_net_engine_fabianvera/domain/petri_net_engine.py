from .petri_net import PetriNet

import numpy as np


class PetriNetEngine:

    def __init__(self, petri_net: PetriNet):
        self.petri_net = petri_net
        pass

    def is_enabled_transition(self, *args):
        markings = self.petri_net.get_markings()
        transition_markings = np.array([0] * len(self.petri_net.places))
        for transition in args:
            transition_markings += self.petri_net.get_inputs_matrix_for_transition(transition)
        result_diff = markings - transition_markings
        return np.min(result_diff) >= 0

    def fire_transitions(self, *args):

        markings = self.petri_net.get_markings()
        if not self.is_enabled_transition(*args):
            raise Exception

        inputs_transitions = np.array([0] * len(self.petri_net.places))
        for transition in args:
            inputs_transitions += self.petri_net.get_inputs_matrix_for_transition(transition)

        outputs_transitions = np.array([0] * len(self.petri_net.places))
        for transition in args:
            outputs_transitions += self.petri_net.get_outputs_matrix_for_transition(transition)

        self.petri_net.markings = markings - inputs_transitions + outputs_transitions
        return self.petri_net.markings
