#!/usr/bin/env python3

import urwid

palette = [
        ('body', 'default', 'default'),
        ('footer', 'dark cyan', 'dark blue', 'bold'),
        ('key', 'light cyan', 'dark blue', 'underline'),
        ]

footer_text = ('foot', [
    ('key', "1"), "Play",
    ('key', "2"), "Quit",
    ])

# have a look at
# http://excess.org/urwid/browser/examples/edit.py
