import urwid

def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()

palette = [
    ('entry_text', 'black', 'dark cyan'),
    ('entry_button', 'white, bold', 'black'),
    ('streak', 'black', 'dark cyan'),
    ('bg', 'default', 'default'),]

placeholder = urwid.SolidFill()
loop = urwid.MainLoop(placeholder, palette, unhandled_input=exit_on_q)
loop.widget = urwid.AttrMap(placeholder, 'bg')
loop.widget.original_widget = urwid.Filler(urwid.Columns([]),valign='bottom')

# menu entries
txt_play  = urwid.Text(('entry_text', u"Play "), align='left')
txt_pause = urwid.Text(('entry_text', u"Pause "), align='left')
txt_open  = urwid.Text(('entry_text', u"Open "), align='left')
txt_quit  = urwid.Text(('entry_text', u"Quit "), align='left')
txt_f1 = urwid.Text(('entry_button', u" F1"), align='left')
txt_f2 = urwid.Text(('entry_button', u" F2"), align='left')
txt_f3 = urwid.Text(('entry_button', u" F3"), align='left')
txt_f4 = urwid.Text(('entry_button', u" F4"), align='left')
entry1 = urwid.Columns([txt_f1, txt_play])
entry1 = urwid.AttrMap(entry1, 'streak')
entry2 = urwid.Columns([txt_f2, txt_pause])
entry2 = urwid.AttrMap(entry2, 'streak')
entry3 = urwid.Columns([txt_f3, txt_open])
entry3 = urwid.AttrMap(entry3, 'streak')
entry4 = urwid.Columns([txt_f4, txt_quit])
entry4 = urwid.AttrMap(entry4, 'streak')

columns = loop.widget.base_widget # .base_widget skips the decorations
for item in [entry1, entry2, entry3, entry4]:
    columns.contents.append((item, columns.options()))

loop.run()
