#!/usr/bin/env python3

"""Organizes journal entries and notes for retrospection"""

import os
import sys
import json
import datetime
import click
from pprint import pprint
import traceback
import logging

"""Kind of a proto-consructor here"""
def init():
    journal_path = os.path.join(os.path.expanduser('~'), '.journal')
    journal_date = datetime.datetime.today()
    journal_dir = os.path.join(journal_path, str(journal_date.year), str(journal_date.month))
    return({'journal_path': journal_path, 'journal_date': journal_date, 'journal_dir': journal_dir})

def read_journal_entries(days, state):
    output = []
    for day in range(0, (1 + days)):
        if os.path.isfile(os.path.join(state['journal_path'], state['journal_dir'], str((state['journal_date'].day - day)))):
            try:
                with open(os.path.join(state['journal_path'], state['journal_dir'], str((state['journal_date'].day - day)))) as file:
                    entries = json.loads(file.read())
                    for ent in entries:
                        thisday = str(state['journal_date'].day - day)
                        output.append("{}/{} -- {}".format(state['journal_dir'], thisday, ent['content'].strip('\n')))
            except Exception as e:
                logging.error(traceback.format_exc())
    if output:
        for out in output:
            print(out)
    else:
        print("No journal entries found.")

@click.command()
@click.argument('days', default = 0)
@click.option('-v', '--verbose', 'verbose', default = False, help = "More info", is_flag = True)
@click.option('-d', '--debug', 'debug', default = False, help = "Lot's of info", is_flag = True)
def main(days, verbose, debug):
    """For outputing past journal entries.  The argument is a numeric value of how many days you wish to view in the past"""
    state = init()
    journal_entries = read_journal_entries(days, state)
    
if __name__ == '__main__':
    main()
