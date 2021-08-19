# DomainsTool

DomainsTool is a Python script for mapping different domains [usually of an organization] to their respective IP Address and vice versa. Useful in the Information-gathering stages of a PenTest process.


## Usage
To use this tool, you have to provide a list of desired domains in a file, same as the output of [Sublist3r](https://github.com/aboul3la/Sublist3r) tool. the format of the addresses and domains (protocol, www, strips) isn't important, just pass the file to the script.

```bash
python domainstool.py [-h] [-i INPUT_FILE] [-r [REPORT]] [-t SPECIAL_HOST] [-v [VERBOSE]]

```

```
optional arguments:
  -i INPUT_FILE, --input-file INPUT_FILE
                        path to file containing domains
  -h, --help            show this help message and exit
  -r [REPORT], --report [REPORT]
                        full report needed or not
  -t SPECIAL_HOST, --target SPECIAL_HOST
                        specify the host you want to find all domains pointing to it [A Record]
  -v [VERBOSE], --verbose [VERBOSE]
                        choose to generate a complete report showing which domain is on which host
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
