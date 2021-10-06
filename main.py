import sys
import requests
import json
import logging
from seq_con_json_converter.converter import Converter

logging.basicConfig(filename='example.log', level=logging.DEBUG)
API_URL = "https://www.ebi.ac.uk/pdbe/graph-api/uniprot/sequence_conservation/"
ACCESSION = sys.argv[1]

logging.info("Fetching JSON for " + ACCESSION)
response = requests.get(url=API_URL + ACCESSION).json()
with open("data/" + ACCESSION + "-old.json", "w") as old_json:
    logging.info("Saving old JSON for " + ACCESSION)
    json.dump(response, old_json)


if __name__ == '__main__':
    converter = Converter("data/" + ACCESSION + "-old.json", "data/" + ACCESSION + "-new.json")
    converter.load_json()
    logging.info("Converting JSON for " + ACCESSION)
    converter.convert()
    converter.save_json()
    logging.info("Saving new JSON for " + ACCESSION)
