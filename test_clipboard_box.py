def test_set_clipboard_text(home):
    clipboard = home.nav_to_clipboard_box()

    clipboard_text = 'Hubert test#!@'
    clipboard.set_clipboard_text(clipboard_text)


def test_check_clipboard_text(home):
    clipboard = home.nav_to_clipboard_box()

    clipboard_text = 'Hubert test#!@'
    clipboard.set_clipboard_text(clipboard_text)
    clipboard.nav_back()
    clipboard = home.nav_to_clipboard_box()
    assert clipboard.read_clipboard_text() == 'Hubert test#!@'
