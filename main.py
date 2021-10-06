import sys
from seq_con_json_converter.converter import Converter


# TODO - Get the JSON data from the API instead of manually downloaded JSON files
# TODO - Get the JSON paths from sys.argv instead of having it hard-coded
# TODO - Add logging
# TODO - Add license
# TODO - Push to a repository

# import requests
# API_URL = "https://www.ebi.ac.uk/pdbe/graph-api/uniprot/sequence_conservation/"
# ACCESSION = "P0DTD1"
# response = requests.get(API_URL + ACCESSION)


if __name__ == '__main__':
    converter = Converter("./data/old.json", "./data/new.json")
    converter.load_json()
    converter.convert()
    converter.save_json()
