import numpy as np
# import project libraries
from constants import *

# Collection of utility functions

def get_datatype_color(datatype):
	color = COLOR_RESET
	if datatype == 'float64':
		color = COLOR_GREEN
	elif datatype == 'object':
		color = COLOR_PURPLE
	else:
		color = COLOR_BLACK
	return color

def format_elapse_time(elapse_time):
    format_time = ''
    if elapse_time is not None:
        _parts = str(elapse_time).split('.')
        _millisecs = _parts[len(_parts)-1][:4]
        format_time = f'{_parts[0]}.{_millisecs}'
    return format_time

def print_format_dataset(dataset, nrow, ncol, **kwargs):
    def _column_attribute(column, key, **kwargs):
        value = None
        if ('columns' in kwargs and
            column in kwargs['columns'] and
            key in kwargs['columns'][column]):
            value = kwargs['columns'][column][key]
        return value
        
    def _add_column_value_attribute(column, col_value, formatter=None, **kwargs):
        value = col_value
        if formatter is not None:
            value = f'{value:{formatter}}'
        if ('columns' in kwargs and
            column in kwargs['columns']):
            col_attributes = kwargs['columns'][column]
            if value == DEFAULT_SETTINGS:
                value = f'{COLOR_GRAY}{value}{COLOR_RESET}'
            else:
                # check for color attribute
                if 'color' in col_attributes:
                    value = f'{col_attributes["color"]}{value}{COLOR_RESET}'
        return value
        
    # store list of steps needed to print all dataset columns
    steps = np.arange(0, len(dataset.columns), ncol)
    index_spacer = f'{TAB_SPACE * 2}'
    index_max_length = 0
    if 'print_index' in kwargs:
        size = len(max(dataset.index, key=len))
        index_spacer = f'{TAB_SPACE}{" " * size}'
    index_formatter = len(index_spacer)
    for step in steps:
        # get column names to print for this step
        cols = dataset.columns[range(step, min(step+ncol, len(dataset.columns)))]
        cols_size = [] # store each column size for alignment
        output = ''
        if 'print_index' in kwargs:
            output = f'{TAB_SPACE * 3}'
        # catenate column names to output (print)
        for index, col in enumerate(cols):
            # set column size if specified
            value = _column_attribute(col, 'size', **kwargs)
            if value is None:
                value = len(col)
                cols_size.append(value)
            else:
                cols_size.append(value)
            if DEBUG_LEVEL > 4:
                print(f'::print_format_dataset_0:: {col} size = {value} {cols_size}')
            # set column size if specified
            alignment = _column_attribute(col, 'alignment', **kwargs)
            if alignment is None:
                output += f'{TAB_SPACE}{col:<{value}}'
            else:
                output += f'{TAB_SPACE}{col:{alignment}{value}}'
        # print column names
        print(f'{TAB_SPACE * 2}{index_spacer}{COLOR_BLUE}{output}{COLOR_RESET}')
        # for each row, print column values
        for row in range(0, nrow):
            output = ''
            if 'print_index' in kwargs:
                output = f'{TAB_SPACE}'
            # catenate column values to output (print)
            for index, col in enumerate(cols):
                # ensure correct alignment for column
                # set column size if specified
                alignment = _column_attribute(col, 'alignment', **kwargs)
                if alignment is None:
                    alignment = '<'
                formatter = cols_size[index]
                if 'print_index' in kwargs:
                    # print("::print_format_dataset::",row, col, dataset.index[row])
                    column_value = dataset.loc[dataset.index[row], col]
                    if DEBUG_LEVEL > 3:
                        print(f'::print_format_dataset_1:: {index} {col} {type(column_value)} {column_value} {alignment} {formatter}')
                    if col == COLUMN_NAME_PERCENTAGE:
                        column_value = f'{column_value:>{formatter-1}}%'
                    else:
                        if column_value is None:
                            column_value = ''
                        elif (isinstance(column_value, np.int64) or
                              isinstance(column_value, np.float64)):
                            formatter = str(formatter) + ','
                        elif str(column_value).isnumeric():
                            # format number with the thousand separator
                            formatter = str(formatter) + ','
                    column_value = _add_column_value_attribute(col, column_value, f'{alignment}{formatter}', **kwargs)
                    if DEBUG_LEVEL > 3:
                        print(f'::print_format_dataset_2:: {index} {col} {type(column_value)} {column_value} {len(column_value)}')
                    output += f'{column_value}{TAB_SPACE}'
                else:
                    if DEBUG_LEVEL > 3:
                        print(f'::print_format_dataset_3:: {index} {col} {type(dataset.loc[row, col])} {dataset.loc[row, col]} {alignment} {formatter}')
                    column_value = _add_column_value_attribute(col, dataset.loc[row, col], f'{alignment}{formatter}', **kwargs)
                    output += f'{column_value}{TAB_SPACE}'
                    if DEBUG_LEVEL > 3:
                        print(f'::print_format_dataset_4:: {index} {col} {type(column_value)} {column_value} {len(column_value)}')
            # print column values
            row_value = f'{dataset.index[row]:<{index_formatter}}'
            if 'print_index' in kwargs:
                color = COLOR_BLACK
                if 'highlight_index' in kwargs:
                    color = COLOR_BLUE
                row_value = f'{row+1}.{TAB_SPACE}{COLOR_BOLD}{color}{dataset.index[row]:<{index_formatter}}{COLOR_RESET}'
            print(f'{TAB_SPACE * 2}{row_value}{COLOR_BOLD}{COLOR_GREEN}  {output}{COLOR_RESET}')
