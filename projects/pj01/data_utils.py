"""Utility functions."""

__author__ = "730407726"

# Define your functions below

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result 


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str]."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Read the rows of a csv into a 'table'."""
    result: dict[str, list[str]] = {}
    for columns in table:
        new: list[str] = []
        i: int = 0
        while i < n:
            new.append(table[columns][i])
            i += 1
        result[columns] = new
    return result


def select(tables: dict[str, list[str]], column: list[str]) -> dict[str, list[str]]:
    """Produce a list[str] of all values in a single column."""
    empty: dict[str, list[str]] = {}
    for row in column:
        empty[row] = tables[row]
    return empty


def concat(one: dict[str, list[str]], two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    build: dict[str, list[str]] = {}
    for colum in one:
        build[colum] = one[colum]
    for c in two:
        if build in two:
            build
        else:
            build[c] = two[c]
    return build