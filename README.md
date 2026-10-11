# CLI Tool to monitor system resources

Compatible with Linux and Windows.

## Usage

```bash
python3 -m venv venv
```
On Windows:

```bash
venv/Scripts/activate

python3 ts-pmo.py
```

On Linux:

```bash
source venv/bin/activate

python3 ts-pmo.py
```

Options:

-v = Verbose Output Network information (Linux & Windows) and Temperature information (Linux Only)
-i = Set Update interval

Example Usage:

```bash
python3 ts-pmo.py -v -i 3

(Verbose output with updates after 3 seconds)
```

Not the final version. Improvements soon.
