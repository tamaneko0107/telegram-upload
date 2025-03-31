from ctypes import c_int64

import click


def get_progress_bar(action, file, length):
    if len(file) > 20:
        file = file[:10] + '...' + file[-7:]
    bar = click.progressbar(label='{} "{}"'.format(action, file), length=length)
    last_current = c_int64(0)

    def progress(current, total):
        if current < last_current.value:
            return
        bar.pos = 0
        bar.update(current)
        last_current.value = current
    return progress, bar
