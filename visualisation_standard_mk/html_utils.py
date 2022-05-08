from IPython.core.display import display, HTML


def html(html_string: str):
    display(HTML(html_string))


def print_header(header: str, size_level: str = '1'):
    html(f'<h{size_level} style="text-align:center">{header}<h{size_level}>')


def print_paragraph(string: str, fontsize: int):
    html(f'<p style="font-size:{fontsize}px; text-align:center">{string}</p>')


def print_blank_line():
    html('<br><br>')


def print_horizontal_line():
    html('<hr style="border:2px solid gray">')