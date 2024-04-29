# customise tabulate package
# https://github.com/astanin/python-tabulate/tree/master
__package__ = 'tabulate'

from __init__ import *

# print(f'wrm::tabulater:: {tabulate_formats}')

# add custom tabulate format
# tabulate_formats.append({
    # "nospace": TableFormat(
        # lineabove=Line("", "-", "", ""),
        # linebelowheader=None,
        # linebetweenrows=None,
        # linebelow=Line("", "-", "", ""),
        # headerrow=DataRow("", "", ""),
        # datarow=DataRow("", "", ""),
        # padding=0,
        # with_header_hide=["lineabove", "linebelow"],
    # )},
# )
# multiline_formats["nospace"] = "nospace"
def set_preserve_whitespace(value):
    tabulate.PRESERVE_WHITESPACE = value

# create wrapper
def tabulater(
    tabular_data,
    headers=(),
    tablefmt="simple",
    floatfmt="g",
    colalign=None,
    preserve_whitespace=False,
):
    return tabulate(
        tabular_data,
        headers=headers,
        tablefmt=tablefmt,
        floatfmt=floatfmt,
        colalign=colalign,
        preserve_whitespace=preserve_whitespace,
    )
