#!/usr/bin/env python

import numpy as np
import pandas as pd
import sys
import os.path
import click


# Handles excel file, prompting for sheet
def handle_excel(filename):
    # Prompt for sheet number
    sheet = input('Enter sheet number (0 default): ')
    if sheet == '':
        return pd.read_excel(filename)
    return pd.read_excel(filename, int(sheet))


# Prompts user for columns
def prompt_col(columns, axis):
    col = input(axis + '-column: ')
    while col not in columns:
        print('Invalid ' + axis + '-column name.')
        print('Columns names: ', end='')
        print(*columns, sep=', ')
        col = input('Enter ' + axis + '-column: ')
    return col


# Finds x-value in xcol corresponding to yval
def find_val(xcol, ycol, yval):
    xvals = []

    # Check first value
    if ycol[1] == yval:
        xvals.push_end(xcol[1])

    # Check others, interpolate as necessary
    for i in range(2, len(ycol)):
        if ycol[i] == yval:
            xvals.append(xcol[i])
        elif ycol[i] > yval > ycol[i - 1]:
            xvals.append(np.interp(yval, [ycol[i - 1], ycol[i]], [xcol[i - 1], xcol[i]]))
        elif ycol[i] < yval < ycol[i - 1]:
            xvals.append(np.interp(yval, [ycol[i], ycol[i - 1]], [xcol[i], xcol[i - 1]]))
    return xvals


@click.command()
@click.option('--sort', default='false', help='Whether x-column should be sorted (True/False)')
@click.argument('filename')
def main(sort, filename):
    """
    CLI to parse .csv or .xls* files for x value associated with given y-value
    """
    # Check file name
    if not os.path.isfile(filename):
        sys.exit('Invalid filepath')

    # Check and handle file extension
    if filename.lower().endswith('.csv'):
        dframe = pd.read_csv(filename)
    elif filename.lower().endswith(('.xls', '.xlsx', '.xlsm', '.xlsb')):
        dframe = handle_excel(filename)
    else:
        sys.exit('Invalid extension')

    # Get columns
    xname = prompt_col(dframe.columns.values, 'x')
    yname = prompt_col(dframe.columns.values, 'y')

    # Sort if necessary
    if sort.lower() == 'true' or sort.lower() == 't':
        dframe.sort_values(by=xname)

    # Prompt for y-value
    yval = int(input('Enter desired y-value: '))

    # Search for corresponding x-value and print
    xvals = find_val(dframe[xname], dframe[yname], yval)
    if len(xvals) == 0:
        print('y-value not encountered')
    else:
        print('x-value(s): ', end='')
        print(*xvals, sep=', ')


if __name__ == '__main__':
    main()