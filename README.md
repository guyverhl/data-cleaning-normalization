# data-cleaning-normalization
- [data-cleaning-normalization](#datacleaningnormalization)
    - [Usage](#usage)
        - [Requirement](#requirement)
        - [Insert File](#insert-file)
    - [Options](#options)
        - [Description](#description)
        - [Title](#title)
        - [Version](#version)
        - [Summary](#summary)
        - [File](#file)
        - [Server URL](#server-url)
        - [Directory](#directory)
        - [Output Directory](#output-directory)
        - [Endpoint Description](#endpoint-description)
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

## Description
To add the description of a mockcase Swagger file, use `-i` to add the string.
```bash
$ node wiremock2swagger3.js -i <descrption>
$ node wiremock2swagger3.js -i "This is the description of swagger 3.0 file"
```

The value of description will save in the variable `desc`.
```js
var swagger = {
    "openapi": "3.0.0",
    "info": {
      "title": title,
      "description": desc,
      "version": version
    }
 ```
 ```js
var swagger = {
    "openapi": "3.0.0",
    "info": {
      "title": title,
      "description": "This is the description of swagger 3.0 file",
      "version": version
    }
 ```

## Title
To add the title of a mockcase Swagger file, use `-t` to add the string.
```bash
$ node wiremock2swagger3.js -t <title>
$ node wiremock2swagger3.js -t "This is the title of swagger 3.0 file"
```

The value of title will save in the variable `title`.
```js
var swagger = {
    "openapi": "3.0.0",
    "info": {
      "title": title,
      "description": desc,
      "version": version
    }
 ```
 ```js
var swagger = {
    "openapi": "3.0.0",
    "info": {
      "title": "This is the title of swagger 3.0 file",
      "description": desc,
      "version": version
    }
 ```

## Version
To add the version of a mockcase Swagger file, use `-v` to add the string.
```bash
$ node wiremock2swagger3.js -v <version>
$ node wiremock2swagger3.js -v 1.0.0
```

The value of version will save in the variable `version`.
```js
var swagger = {
    "openapi": "3.0.0",
    "info": {
      "title": title,
      "description": desc,
      "version": version
    }
 ```
 ```js
var swagger = {
    "openapi": "3.0.0",
    "info": {
      "title": title,
      "description": desc,
      "version": 1.0.0
    }
 ```

## Summary
To add the summary of a specific mockcase, use `-s` to add the string.
```bash
$ node wiremock2swagger3.js -s <summary>
$ node wiremock2swagger3.js -s "This is the summary of swagger 3.0 file"
```

The value of summary will save in the variable `summary`.
```js
"paths": {
  [mockcaseURL]: {
    [method]: {
      "parameters": parameters,
      "summary": summary,
      "responses": {

      }
    }
  }
}
```
```js
"paths": {
  [mockcaseURL]: {
    [method]: {
      "parameters": parameters,
      "summary": "This is the summary of swagger 3.0 file",
      "responses": {

      }
    }
  }
}
```

## File
Use `-f` to insert wiremock json file for converting to swagger3.0.
```bash
$ node wiremock2swagger3.js -f <name-of-json>
$ node wiremock2swagger3.js -f testing.json
```

## Server URL
Input situable URL for testing. The default server URL is `http://localhost:8080`.
```bash
$ node wiremock2swagger3.js -u <server-url>
$ node wiremock2swagger3.js -u "http://localhost:8088"
```

The value of server url will save in the variable `url`.
```js
"servers": [
  {
    "url": url
  }
]
```
```js
"servers": [
  {
    "url": "http://localhost:8088"
  }
]
```

## Directory
Use `-d` to insert wiremock json folder for converting to swagger3.0.
```bash
$ node wiremock2swagger3.js -d <path-of-directory>
$ node wiremock2swagger3.js -d /Users/abc/tests/
```

## Output Directory
Use `-o` to specify the output directory
```bash
$ node wiremock2swagger3.js -o <output-directory>
$ node wiremock2swagger3.js -o tests/
```

## Endpoint Description
To add the endpoint description of a mockcase Swagger file, use `-e` to add the string.
```bash
$ node wiremock2swagger3.js -e <endpoint-description>
$ node wiremock2swagger3.js -e "This is the endpoint of the swagger"

```
The value of endpoint description will save in the variable `endpointDesc`.
```js
"paths": {
  [mockcaseURL]: {
    [method]: {
      "description": endpointDesc,
      "parameters": parameters,
      "requestBody": requestBody,
      "summary": summary,
      "responses": {

      }
    }
  }
}
```
```js
"paths": {
  [mockcaseURL]: {
    [method]: {
      "description": "This is the endpoint of the swagger",
      "parameters": parameters,
      "requestBody": requestBody,
      "summary": summary,
      "responses": {

      }
    }
  }
}
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