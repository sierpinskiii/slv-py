#!/usr/bin/python

import PySimpleGUI as sg
import time, argparse
from sys import stdin, stderr

parser = argparse.ArgumentParser(description='slv')
parser. add_argument('--channels', type=str,
                     nargs='+',
                     help='channels')

args = parser.parse_args()
channels = args.channels
print(channels)

# replace this part with some good ol' DB
temp_db = {} 
for ch in channels:
    temp_db[ch] = []

sg.theme('Black')
FONT = ('Terminus', 13)

layout = [[]]

for ch in channels:
    layout[0].append(sg.Column(
        [
            [
                # sg.Text(ch),
                sg.Combo(channels, key=ch+'combo')
            ],

            [
                sg.Listbox(
                    values=[], enable_events=True, size=(40, 20), key=ch
                )
            ]
        ]
    ))

    layout[0].append(sg.VSeperator())


window = sg.Window('slv', layout, finalize=True)

while True:

    event, values = window.read(timeout=100)

    if event in (None, sg.WIN_CLOSED):
        break

    if event == sg.TIMEOUT_EVENT:
        line = input()
        try:
            temp_db[line.split()[0]].append(line)
        except:
            stderr.write(f"Couldn't identify the channel of the string: {line} \n")
            continue
        for ch in channels:
            window[ch].update(temp_db[ch])

window.close()
