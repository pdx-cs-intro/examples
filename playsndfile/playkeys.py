import curses, playsound, threading, sys

keys = {
    ';': "g",
    'l': "e",
    'k': "d",
    'j': "c",
}

def playkey(scr, note):
    playsound.playsound("keys/" + note + ".wav")
    scr.addstr(0, 0, ' ')
    scr.refresh()

def main(stdscr):
    stdscr.clear()
    while True:
        ch = stdscr.getkey()
        if ch == 'q':
            break
        if ch not in keys:
            continue
        note = keys[ch]
        stdscr.addstr(0, 0, note.upper())
        stdscr.refresh()
        t = threading.Thread(target=playkey, args=(stdscr, note))
        t.start()

curses.wrapper(main)
