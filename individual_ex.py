import pandas as pd
import re

raw_data = None

def input_csv(raw_data):
    try:
        csv_file = input("Input CSV file (staff_dir.csv): ")
        if csv_file == '\q': exit()
        raw_data = pd.read_csv(csv_file)
    except Exception as e:
        print(e)
        return input_csv(raw_data)
    else:
        return raw_data

def check_columns_with_empty_cell(df):

    df.columns = [' '.join(i.split()) for i in df.columns]
    empty_cols_name = [value for value in df.columns if "Unnamed" in value]
    empty_cols = [col for col in df.columns if df[col].isnull().any()]
    print("You have", len(empty_cols_name), "columns without naming")
    print("You have", len(empty_cols), "columns with empty cells")

    return main()

# -M
def modify_column_name():
    global df

    print(df.columns.values)
    col = input("Name of column that you want to rename: ")
    if col == '\q': return main()
    elif col not in df.columns.values: return modify_column_name()
    i = input("Updated name: ")
    df = df.rename(columns={col: i})
    print(f'"{col}" is changed to "{i}".')

    return main()

# -m
def modify_cell():
    global df

    print("Input row, column and value to a cell that you want to change")
    print("Length of dataframe is", len(df) - 1, '\n', df.columns.values)
    row = input("Number of Row: ")
    col = input("Name of Column: ")
    if (col == '\q' or row == '\q'): return main()
    elif col not in df.columns.values or not row.isnumeric(): return modify_cell()
    row = int(row)
    if row > len(df) - 1: return modify_cell()
    value = input("Value: ")

    df.iloc[row, df.columns.get_loc(col)] = value
    print(f'The value of row {row} in "{col}" is changed to "{value}".')

    return main()

# -D
def remove_selected_column():
    global df

    print(df.columns.values)
    i = input("Type the name of column to delete: ")
    if i == '\q': return main()
    elif i not in df.columns.values: return remove_selected_column()
    else: del df[i]

    print(f'"{i}" is removed.')

    return main()

# -C
def counting_with_a_column():
    global df

    print(df.columns.values)
    col = input("Select a column to count: ")
    if col == '\q': return main()
    elif col not in df.columns.values: return counting_with_a_column()
    selected_column = [i for i in df[col]]
    selected_column = {i: selected_column.count(i) for i in selected_column}
    for key, value in selected_column.items():
        print(key, value)

    return main()

# -d
def remove_selected_row():
    global df

    print(len(df))
    row = input("Number of row to remove: ")
    if row == '\q': return main()
    elif not row.isnumeric(): return remove_selected_row()
    row = int(row)
    if row > len(df) - 1: return remove_selected_row()
    df.drop([row], axis=0, inplace=True)
    print(f'Row {row} is removed.')
    
    return main()

# -r
def normalization():
    global df
    column_with_multi_values = []
    
    for col in list(df.columns):
        df[col] = ['('.join(i.split("\r\n(")) for i in df[col]]
        for row in range(0, len(df)):
            cell_value = df[col][row]
            cell_value_list = list(map(str, cell_value.split("\r\n")))
            if (len(cell_value_list) > 1 and not col in column_with_multi_values): column_with_multi_values.append(col)

    for i in range(0, len(column_with_multi_values)):
        selected_column = list(column_with_multi_values[i].split(" "))
        set_index_list = [i for i in df.columns if i not in selected_column]
        df = df.set_index(set_index_list)
        df = df.apply(lambda x: df[column_with_multi_values[i]].str.split('\r\n').explode())
        df = df.reset_index()

    print("Normalization is complete")
    return tidy_dataframe()

def tidy_dataframe():
    global df

    for i in list(df.columns):
        if 'E-mail' in i: continue
        elif 'Location' in i: df[i] = [''.join(i.split()).upper() for i in df[i]]
        elif 'Phone' in i: df[i] = [re.sub(r"[^A-Za-z0-9]+", "", i) for i in df[i]]
        elif 'Position' in i:
            df[i] = ['('.join(i.split(' (')).title() for i in df[i]]
            df[i] = [i.replace("Assoc.", "Associate") for i in df[i]]
            df[i] = [re.sub(r"\bProf\b", "Professor", i) for i in df[i]]
        else: df[i] = [' '.join(i.split()).title() for i in df[i]]

    duplicateDFRow = df[df.duplicated()]
    print('Duplicated Rows: \n', duplicateDFRow)
    df = df.drop_duplicates()
    df.reset_index(inplace=True)
    del df['index']
    print("Dataframe is cleaned")

    return main()

# -v
def receive_cell_value():
    print('Length of the row is', len(df) - 1)
    row = input("Number of Row: ")
    if row == '\q': return main()
    elif not row.isnumeric(): return receive_cell_value()
    row = int(row)
    if row > len(df) - 1: return receive_cell_value()
    
    print(df.columns.values)
    col = input("Name of Column: ")
    if col == '\q': return main()
    elif col not in df.columns.values: return receive_cell_value()
    print('The value is', df.loc[row, col])

    return main()

# -o
def to_csv():
    global df

    output = input("Name of the new csv file: ")
    if output == '\q': return main()
    df.to_csv(f'{output}.csv', index=0)
    print(f'{output}.csv is generated.')
    
    return main()

# -s
def sort_by_column():
    global df

    print(df.columns.values)
    col = input("Name of column to sort: ")
    if col == '\q': return main()
    elif col not in df.columns.values: return sort_by_column()
    val = input("\'as\' for ascending or \'de\' for descending: ")
    if val == '\q': return main()
    elif val == 'de': df = df.sort_values(by=[col], ascending = False)
    elif val == 'as': df = df.sort_values(by=[col], ascending = True)
    else: 
        print('Invalid input!')
        return sort_by_column()
    
    df.reset_index(inplace=True)
    del df['index']
    print(f'The order of "{col}" is changed.')

    return main()

# -t
def change_text_case():
    global df

    print(df.columns.values)
    col = input("Name of column to change: ") 
    if col == '\q': return main()
    elif col not in df.columns.values: return change_text_case()
    
    val = input("\'up\' for upper, \'lo\' for lower or \'ti\' for title: ")
    if val == '\q': return main()    
    elif val == 'up': df[col] = [' '.join(i.split()).upper() for i in df[col]]
    elif val == 'lo': df[col] = [' '.join(i.split()).lower() for i in df[col]]
    elif val == 'ti': df[col] = [' '.join(i.split()).title() for i in df[col]]
    else: 
        print('Invalid input!')
        return change_text_case()

    print(f'The textcase of "{col}" is changed.')
    return main()

# \q
def quit_prog():
    print("Thank you and Goodbye")
    exit()

# -h
def help_list():
    print("\n%-5s %-20s %-30s" % ("-p,", "--print", "Print all dataframe"))
    print("%-5s %-20s %-30s" % ("-C,", "--count_column", "Count the number of the cell values of a selected column"))
    print("%-5s %-20s %-30s" % ("-m,", "--modify_cell", "Modify the selected cell value"))
    print("%-5s %-20s %-30s" % ("-M,", "--modify_col_name", "Modify the selected column name"))
    print("%-5s %-20s %-30s" % ("-D,", "--del_col", "Remove the selected column"))
    print("%-5s %-20s %-30s" % ("-d,", "--del_row", "Remove the selected row"))
    print("%-5s %-20s %-30s" % ("-v,", "--view_value", "View the selected cell value"))
    print("%-5s %-20s %-30s" % ("-o,", "--gen_csv", "Generate CSV file for database"))
    print("%-5s %-20s %-30s" % ("-s,", "--sort", "Sort the dataframe by selected column"))
    print("%-5s %-20s %-30s" % ("-t,", "--textcase", "Change values textcase"))
    print("%-5s %-20s %-30s" % ("\q,", "--quit", "Quit the program"))
    print("%-5s %-20s %-30s" % ("-h,", "--help", "Show command list\n"))

    return main()

def main():
    global df

    usr_input = input('prog ')
    if usr_input == '-p' or usr_input == '--print':
        print(df)
        main()
    elif usr_input == '-C' or usr_input == '--count_column': counting_with_a_column()
    elif usr_input == '-m' or usr_input == '--modify_cell': modify_cell()
    elif usr_input == '-M' or usr_input == '--modify_col_name': modify_column_name()
    elif usr_input == '-D' or usr_input == '--remove_col': remove_selected_column()
    elif usr_input == '-d' or usr_input == '--remove_row': remove_selected_row()
    elif usr_input == '-v' or usr_input == '--view_value': receive_cell_value()
    elif usr_input == '-o' or usr_input == '--gen_csv': to_csv()
    elif usr_input == '-r' or usr_input == '--run': normalization()
    elif usr_input == '-s' or usr_input == '--sort': sort_by_column()
    elif usr_input == '-t' or usr_input == '--text_case': change_text_case()
    elif usr_input == '\q' or usr_input == '--quit': quit_prog()
    elif usr_input == '-h' or usr_input == '--help': help_list()
    else:
        print("Invalid input. Please type again.")
        main()

# Start
print("Welcome to the data cleaning program! Type '-h' or '--help' to know the command of the program.")
raw_data = input_csv(raw_data)
df = pd.DataFrame(raw_data)
check_columns_with_empty_cell(df)
