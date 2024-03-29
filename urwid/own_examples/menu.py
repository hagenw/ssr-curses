import urwid

# define menu entries
entries = [
        ('1', 'Play'),
        ('2', 'Stop'),
        ('3', 'Open'),
        ('4', 'Quit'),]
    
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

def add_menu_entries(entries):
    entry_list = []
    for entry in entries:
        button_txt = urwid.Text(('entry_text', entry[1]), align='left')
        button_key = urwid.Text(('entry_button', u" F" + entry[0]), align='left')
        # 'pack' calculates the needed size of the column with F1 etc.
        button = urwid.Columns([('pack', button_key), button_txt])
        entry_list.append(urwid.AttrMap(button, 'streak'))
    return entry_list
    
columns = loop.widget.base_widget # .base_widget skips the decorations
for item in add_menu_entries(entries):
    columns.contents.append((item, columns.options()))

loop.run()
