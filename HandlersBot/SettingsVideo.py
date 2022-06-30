import time
import re


def conversion_duration_video(duration):
    transform_duration = time.strftime("%M:%S", time.gmtime(duration))
    return transform_duration


def conversion_title_video(file_title):
    remove_resolution = file_title.split('.')[0]
    remove_symbols = re.sub(r'[^ a-zA-Z]', ' ', remove_resolution)
    double_gap = '  '.join(remove_symbols.split())
    title = double_gap.replace('  ', ' ')
    return title





