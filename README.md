Sequence Conservation Data Converter
=

[![Build Status](https://app.travis-ci.com/mvaradi/seq-con-converter.svg?branch=main)](https://app.travis-ci.com/mvaradi/seq-con-converter)
[![codecov](https://codecov.io/gh/mvaradi/seq-con-converter/branch/main/graph/badge.svg?token=6OETPCDG6B)](https://codecov.io/gh/mvaradi/seq-con-converter)

This is a Python package for converting the current sequence conservation JSON to a proposed new format.

## Quick start

Get the code and install dependencies:
```shell
git clone https://github.com/mvaradi/seq-con-converter
cd seq-con-converter
pip install -r requirements
```

## Basic usage

Run the `main.py` sript with an argument that is a UniProt accession:
```shell
py main.py P12345
```

## Running tests

```shell
pytest
```

## Versioning
 
We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/mvaradi/seq-con-converter/tags).
 
## Authors
 
* **Mihaly Varadi** - *Initial Implementation* - [mvaradi](https://github.com/mvaradi)
 
See also the list of [contributors](https://github.com/mvaradi/seq-con-converter/contributors) who participated in this project.
 
## License
 
This project is licensed under the EMBL-EBI License - see the [LICENSE](LICENSE) file for details