# Excel_Parser
CLI tool to parse CSV and Excel files for x-value associated with given y-value, using interpolation when necessary. Supported filetypes are .csv, .xls, .xlsx, .xlsm, .xlsb. 

## Usage
```
$ python excelparser.py --help
Usage: excelparser.py [OPTIONS] FILENAME

  CLI to parse .csv or .xls* files for x value associated with given y-value

Options:
  --sort TEXT  Whether x-column should be sorted (True/False)
  --help       Show this message and exit.
```

## Example
This is an example program interaction where the client uses a .csv file and sorts the input before parsing.

```
$ python excelparser.py --sort=True example.csv
Enter x-column: xcol
Enter y-column: invalid input
Invalid y-column name.
Columns names: xcol, fake, ycol
Enter y-column: ycol
Enter desired y-value: 4
x-value(s): 3.0
```
