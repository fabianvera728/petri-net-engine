from .petri_net import PetriNet


class PetriNetJson:
    pass


class PetriNetMatrix:
    pass


class PetriNetFactory:

    @staticmethod
    def from_json(json: PetriNetJson) -> PetriNet:
        pass

    @staticmethod
    def from_matrix(json: PetriNetMatrix) -> PetriNet:
        pass

    @staticmethod
    def build() -> PetriNet:
        return PetriNet()
