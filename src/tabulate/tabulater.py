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

# create wrapper
def tabulater(
    tabular_data,
    headers=(),
    tablefmt="simple",
    colalign=None,
):
    return tabulate(
        tabular_data,
        headers=headers,
        tablefmt=tablefmt,
        colalign=colalign,
    )
