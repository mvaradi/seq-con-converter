import json
from seq_con_json_converter.utils import rgb_to_hex


class Converter:
    """
    The Converter can be used to convert an input JSON file that has the old format of the
    sequence conservation PDBe-KB API endpoint into a new JSON format.

    I use this to benchmark the size of the new data format and see what level of improvement
    we can achieve if switching to the new format.
    """

    def __init__(self, path_to_input, path_to_output):
        """
        The Converter takes an input and output path to read and save JSON files to/from.
        :param path_to_input: string; path to the input JSON file
        :param path_to_output: string; path to the output JSON file
        """
        self.path_to_input = path_to_input
        self.path_to_output = path_to_output
        self.input_data = None
        self.output_data = None

    def load_json(self):
        """
        Load the input JSON data from a JSON file.
        :return: None
        """
        input_json_file = open(self.path_to_input)
        self.input_data = json.load(input_json_file)
        input_json_file.close()

    def convert(self):
        """
        Read the input JSON data and convert it to a new JSON data format. It also ensures that color coding is
        consistently done using HEX encoding.
        :return: None
        """
        accession = next(iter(self.input_data))
        new_data = {
            "identifier": accession,
            "length": self.input_data[accession]["length"],
            "main_track_color": rgb_to_hex(self.input_data[accession]["labelColor"]),
            "sub_track_color": rgb_to_hex(self.input_data[accession]["data"][0]["labelColor"]),
            "seq_id": self.input_data[accession]["seqId"],
            "data": {
                "index": [],
                "conservation_score": [],
                "residue": []
            }
        }

        for data_item in self.input_data[accession]["data"]:
            new_data["data"]["index"].append(data_item["start"])
            new_data["data"]["conservation_score"].append(data_item["conservation_score"])
            residue = {
                "one_letter_code": [],
                "probability": [],
                "color": []
            }
            for aa in data_item["amino"]:
                residue["one_letter_code"].append(aa["oneLetterCode"])
                residue["probability"].append(aa["probability"])
                residue["color"].append(rgb_to_hex(aa["color"]))
            new_data["data"]["residue"].append(residue)

        self.output_data = new_data

    def save_json(self):
        """
        Save the new JSON data to a JSON file.
        :return: None
        """
        output_json_file = open(self.path_to_output, "w")
        json.dump(self.output_data, output_json_file)
        output_json_file.close()

