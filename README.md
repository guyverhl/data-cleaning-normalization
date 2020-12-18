# data-cleaning-normalization
- [data-cleaning-normalization](#datacleaningnormalization)
    - [Usage](#usage)
        - [Requirement](#requirement)
        - [Insert File](#insert-file)
    - [Options](#options)
        - [Description](#description)
        - [Modify Column Title](#modify-column-title)
        - [Modify cell](#modify-cell)
        - [Count Values in Selected Column](#count-values-in-selected-column)
        - [Delete Selected Column](#delete-selected-column)
        - [Delete Selected Row](#delete-selected-row)
        - [Call a Cell Value](#call-a-cell-value)
        - [Output CSV](#output-csv)
        - [Change Text Case](#change-text-case)
        - [Sorting](#sorting)
        - [Quit](#quit)
    - [Help List](#helplist)

# Usage
How to use the script

## Requirement
This script requires `commander.js` package to run, you need to install the library using `package.json`.
```bash
npm install
```

## Insert File
A json file is needed to convert to swagger file. Since the script run at your current location, you only need to input the name of that json file by adding `-f`.
```bash
$ node wiremock2swagger3.js -f <name-of-json>
$ node wiremock2swagger3.js -f testing.json
```
or use `-d` to insert wiremock json folder for converting to swagger3.0. You should put `all and only` wiremock json files into the folder.
```bash
$ node wiremock2swagger3.js -d <path-of-directory>
$ node wiremock2swagger3.js -d /Users/abc/tests/
```
And the output should be located at your current folder. Result with the file name will prompt.
```bash
swagger-testing-001.json is created.
```

# Options
Usage of options

## Modify Column Title
To modify a title in a selected column, use `-M` to change the string.
```py
def modify_column_name():
    global df

    print(df.columns.values)
    col = input("Name of col that you want to rename: ")
    if col not in df.columns.values: return modify_column_name()
    i = input("Updated name: ")
    df = df.rename(columns={col: i})

    return main()
 ```

## Modify cell
To modify a value in a selected cell, use `-m` to change the string.
```py
def modify_cell():
    global df
    print("Input row, column and value to the cell that you want to change")
    print(df.head(5))
    row = input("Number of Row: ")
    col = input("Name of Column: ")
    if col not in df.columns.values or not row.isnumeric(): return modify_cell()
    value = input("Value: ")
    row = int(row)
    if row > len(df) - 1: return modify_cell()

    df.iloc[row, df.columns.get_loc(col)] = value
    return main()
 ```

## Count Values in Selected Column
To count the number of values in a specific column, use `-C`.
```py
def counting_with_a_column():
    global df
    print(df.columns.values)
    col = input("What columns you want to count? ")
    if col not in df.columns.values: return counting_with_a_column()
    selected_column = [i for i in df[col]]
    selected_column = {i: selected_column.count(i) for i in selected_column}
    for key, value in selected_column.items():
        print(key, value)
    return main()
```

## Delete Selected Column
Use `-D` to delete a selected column.
```py
def remove_selected_column():
    global df

    print(df.head(5))
    i = input("Type order number to select column you want to delete(-a for all): ")
    if i not in df.columns.values:
        return remove_selected_column()
    else:
        del df[i]

    return main()
```

## Delete Selected Row
Use `-d` to delete a selected row.
```py
def remove_selected_row():
    global df
    print(df.head(5))
    row = input("Which rows you want to remove? ")
    if not row.isnumeric(): return remove_selected_row()
    row = int(row)
    if row > len(df) - 1: return remove_selected_row()
    df.drop([row], axis=0, inplace=True)
    return main()
```

## Call a Cell Value
Use `-v` to view the value with a selected cell.
```py
def receive_cell_value():
    row = input("Number of Row: ")
    if not row.isnumeric(): return receive_cell_value()
    row = int(row)
    if row > len(df) - 1: return receive_cell_value()
    col = input("Name of Column: ")
    if col not in df.columns.values: return receive_cell_value()
    print(df.loc[row, col])
    return main()
```

## Output CSV
Use `-o` to specify the name of CSV with directory.
```py
def to_csv():
    global df
    output = input("Name of the new csv file: ")
    df.to_csv(f'{output}.csv', index=0)
    print(f'{output}.csv is generated.')
    main()
```

## Change Text Case
To change the the value to selected textcase within a particular column, use `-t`.
```py
def change_text_case():
    global df

    print(df.columns.values)
    col = input("What columns you want to change? ") 
    if col not in df.columns.values: return change_text_case()
    
    val = input("\'u\' for upper, \'l\' for lower or \'t\' for title: ")    
    if val == 'u': df[col] = [' '.join(i.split()).upper() for i in df[col]]
    elif val == 'l': df[col] = [' '.join(i.split()).lower() for i in df[col]]
    elif val == 't': df[col] = [' '.join(i.split()).title() for i in df[col]]
    else: 
        print('Invalid input!')
        return change_text_case()

    return main()
```

## Sorting
Use `-s` to sort the dataframe by selected column.
```py
def sort_by_column():
    global df

    print(df.columns.values)
    col = input("What columns you want to sort? ") 
    if col not in df.columns.values: return sort_by_column()
    val = input("\'a\' for ascending or \'d\' for descending: ")
    if val == 'd': df = df.sort_values(by=[col], ascending = False)
    elif val == 'a': df = df.sort_values(by=[col], ascending = True)
    else: 
        print('Invalid input!')
        return sort_by_column()
    
    df.reset_index(inplace=True)
    del df['index']

    return main()
```

## Quit
Use `\q` to exit the program.
```py
def quit_prog():
    print("Thank and GoodBye")
    exit()
```

# Help List
The help information is generated based on the information commander already knows about the program. The default help option is `-h,--help`.
```bash
-p,   --print              Print all dataframe           
-C,   --count_column       Count the number of the cell values of a selected column
-m,   --modify_cell        Modify the selected cell value
-M,   --modify_col_name    Modify the selected column name
-D,   --del_col            Remove the selected column    
-d,   --del_row            Remove the selected row       
-v,   --view_value         View the selected cell value  
-o,   --gen_csv            Generate CSV file for database
-s,   --sort               Sort the dataframe by selected column
-t,   --textcase           Change values textcase        
\q,   --quit               Quit the program              
-h,   --help               Show command list
```