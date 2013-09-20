#!/usr/bin/env python3
import urwid

def get_key(key):
    if key in ('q','Q'):
        raise urwid.ExitMainLoop()
    
txt1 = urwid.Text(u"Hello World")
txt2 = urwid.Text(u"Play")
fill = urwid.Columns(txt1)
fill.contents.append(txt2)
loop = urwid.MainLoop(fill, unhandled_input=get_key)
loop.run()
