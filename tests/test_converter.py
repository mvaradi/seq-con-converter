from unittest import TestCase
from seq_con_json_converter.converter import Converter

MOCK_INPUT = {
    "FOO": {
        "length": 42,
        "labelColor": "rgb(211,211,211)",
        "seqId": "ABCD1234",
        "data": [
            {
                "labelColor": "#FFF",
                "start": 1,
                "end": 1,
                "conservation_score": 0,
                "tooltipContent": "Lorem ipsum...",
                "amino": [
                    {
                        "start": 1,
                        "end": 1,
                        "oneLetterCode": "A",
                        "threeLetterCode": "ALA",
                        "probability": 0.3,
                        "color": "rgb(211, 211, 211)",
                        "tooltipContent": "Lorem ipsum..."
                    },
{
                        "start": 1,
                        "end": 1,
                        "oneLetterCode": "P",
                        "threeLetterCode": "PRO",
                        "probability": 0.5,
                        "color": "#FFF",
                        "tooltipContent": "Lorem ipsum..."
                    }
                ]
            },
            {
                "labelColor": "#FFF",
                "start": 2,
                "end": 2,
                "conservation_score": 0.2,
                "tooltipContent": "Lorem ipsum...",
                "amino": [
                    {
                        "start": 2,
                        "end": 2,
                        "oneLetterCode": "C",
                        "threeLetterCode": "CYS",
                        "probability": 0.1,
                        "color": "#FFF",
                        "tooltipContent": "Lorem ipsum..."
                    },
{
                        "start": 2,
                        "end": 2,
                        "oneLetterCode": "S",
                        "threeLetterCode": "SER",
                        "probability": 0.4,
                        "color": "#000",
                        "tooltipContent": "Lorem ipsum..."
                    }
                ]
            }
        ]
    }
}

MOCK_EXPECTED = {
    "identifier": "FOO",
    "length": 42,
    "seq_id": "ABCD1234",
    "data": {
        "index": [1, 2],
        "conservation_score": [0, 0.2],
        "probability_A": [0.3],
        "probability_C": [0.1],
        "probability_D": [],
        "probability_E": [],
        "probability_F": [],
        "probability_G": [],
        "probability_H": [],
        "probability_I": [],
        "probability_K": [],
        "probability_L": [],
        "probability_M": [],
        "probability_N": [],
        "probability_P": [0.5],
        "probability_Q": [],
        "probability_R": [],
        "probability_S": [0.4],
        "probability_T": [],
        "probability_V": [],
        "probability_W": [],
        "probability_Y": []
    }
}


class TestConverter(TestCase):

    def test_convert(self):
        converter = Converter("", "")
        converter.input_data = MOCK_INPUT
        converter.convert()
        self.assertEqual(converter.output_data, MOCK_EXPECTED)