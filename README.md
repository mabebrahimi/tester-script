# tester-script

This script was written to test MySQL URI connector and command tester.

## Requirements

- create venv

```
python -m venv venv
```

- and install python requirements

```
pip install requirements.txt
```

## Work with scripts

First define DWS_MYSQL_DATABASE_URI env for test mysql connection.
And run connectToDB script.
For second script just define DWS_TESTER_COMMAND and DWS_TESTER_THRESHOLD and DWS_TESTER_INTERVAL env for test command script.
And run testerCommand script.

## CI Robots

[@dwsclass](https://github.com/dwsclass) dws-dev-007-python

## How to contribute

All contributions are welcomed. If you find any bugs, please file an issue.

## License

[APACHE LICENSE, VERSION2.0](https://www.apache.org/licenses/LICENSE-2.0)
