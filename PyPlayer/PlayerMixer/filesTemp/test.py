import keyboard as k

k.press_and_release('shift+s, space')

k.write('The quick brown fox jumps over the lazy dog.')

k.add_hotkey('ctrl+shift+a', print, args=('triggered', 'hotkey'))

# Press PAGE UP then PAGE DOWN to type "foobar".
k.add_hotkey('page up, page down', lambda: k.write('foobar'))

# Blocks until you press esc.
k.wait('esc')

# Record events until 'esc' is pressed.
recorded = k.record(until='esc')
# Then replay back at three times the speed.
k.play(recorded, speed_factor=3)

# Type @@ then press space to replace with abbreviation.
k.add_abbreviation('@@', 'my.long.email@example.com')

# Block forever, like `while True`.
k.wait()