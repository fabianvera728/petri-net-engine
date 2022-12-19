import pandas as pd
import numpy as np
from ..domain.petri_net import PetriNet
from ..domain.place import Place
from ..domain.transition import Transition


class FromEventLogToPetriNet:

    def __init__(self):
        pass

    def execute(self, url_dataframe):
        # event_log_dataframe = pd.read_csv(url_dataframe, sep=';')
        event_log_dataframe, event_log_dataframe_copy = self.load_dataframe(url_dataframe)
        event_log_dataframe, dic_places = self.convert_place_name(event_log_dataframe_copy)
        event_log_dataframe = self.create_transition_id(event_log_dataframe, dic_places.copy())
        event_log_dataframe = self.create_places_id(event_log_dataframe, dic_places)
        event_log_dataframe = self.create_tokens(event_log_dataframe)
        cases = event_log_dataframe.sort_values(['timestamp'], ascending=True).groupby('case_id')
        print('\n')
        petri_nets_variants = []
        for key, item in cases:
            petri_net = PetriNet()
            case = cases.get_group(key)
            for i in range(len(case)):
                petri_net.name = str(case.iloc[i]['case_id'])
                place = Place(
                    str(case.iloc[i]['place_id']),
                    case.iloc[i]['place_name'],
                    int(case.iloc[i]['tokens'])
                )
                transition = Transition(
                    str(case.iloc[i]['transition_id']),
                    case.iloc[i]['activity'].replace(' ', '_'),
                )
                petri_net.add_place(place)
                petri_net.add_transition(transition)
                is_input_valid = True
                for entry in petri_net.entries:
                    is_input_valid = is_input_valid and (
                            entry['place'] != str(case.iloc[i]['place_id']) or
                            entry['transition'] != str(case.iloc[i]['transition_id']))
                if is_input_valid:
                    petri_net.add_input(str(case.iloc[i]['place_id']), str(case.iloc[i]['transition_id']), 1)
                is_output_valid = True
                if i + 2 > len(case):
                    break
                for output in petri_net.outputs:
                    is_output_valid = is_output_valid and (
                            output['place'] != str(case.iloc[i + 1]['place_id']) or
                            output['transition'] != str(case.iloc[i]['transition_id']))
                if is_output_valid:
                    petri_net.add_output(str(case.iloc[i]['transition_id']), str(case.iloc[i + 1]['place_id']), 1)
            petri_nets_variants.append(petri_net)
        return petri_nets_variants

    def convert_place_name(self, df: pd.DataFrame):
        # returns place name
        activities = df.activity.unique()  # lista of activities
        id_activities = [f'P{x + 1}' for x in range(len(activities))]
        dic_places = dict(zip(activities, id_activities))
        df['place_name'] = df['activity']
        df.replace({"place_name": dic_places}, inplace=True)
        return df, dic_places

    def load_dataframe(self, filename: str, sep=';'):
        log = pd.read_csv(filename, sep=sep)
        copy_log = log.copy()
        return log, copy_log

    def create_transition_id(self, df: pd.DataFrame, dic_transition_id: dict):
        # create transition_id
        df['transition_id'] = df['activity']
        i = 1
        for k, v in dic_transition_id.items():
            dic_transition_id[k] = i
            i = i + 1
        df.replace({"transition_id": dic_transition_id}, inplace=True)
        return df

    def create_places_id(self, df: pd.DataFrame, dic_activities: dict):
        # create places_id
        df['place_id'] = df['place_name']
        id_places = []
        places_name = []
        for k, v in dic_activities.items():
            id_places.append(int(v[1]))
            places_name.append(v)
        dic_places = dict(zip(places_name, id_places))
        df.replace({"place_id": dic_places}, inplace=True)
        return df

    def create_tokens(self, df: pd.DataFrame):
        # create tokens
        df['tokens'] = 0
        df['tokens'] = np.where(df['place_name'] == 'P1', 1, 0)
        return df

    def create_inputs(self, df: pd.DataFrame):
        # create inputs
        df['inputs'] = 0
        size = df.shape[0]
        shortlist = []
        for i in range(size):
            shortlist.append((df['place_id'][i], df['transition_id'][i], df['tokens'][i]))
        df['inputs'] = shortlist
        return df

    def get_cost_total(self, df: pd.DataFrame):
        dic_costos = {}
        df = df.groupby('case_id').sum()
        dic_costos = dict(df['costs'])
        return dic_costos
