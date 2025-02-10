# 📝 Table Decoders  

This project provides a framework for **decoding tables** from JSON and CSV formats into Python dictionaries.  

## 📦 Imports  
- `csv` – for handling CSV files  
- `json` – for parsing JSON data  
- `collections.defaultdict` – for structured storage  
- `io.StringIO` – for handling in-memory CSV streams  
- `pathlib.Path` – for file operations  
- `pprint.pprint` – for pretty-printing output  

## 🏗️ Classes  

### 🔹 `TableDecoder` (Base Class)  
- Maintains a **registry** of available decoders.  
- Defines a **factory method** (`create()`) to instantiate decoders dynamically.  
- Requires subclasses to implement a **`decode(text)`** method.  

### 🔹 `JsonTableEncoder` (JSON Decoder)  
- Parses **JSON arrays of dictionaries** into a column-based format.  

### 🔹 `CsvTableEncoder` (CSV Decoder)  
- Reads **CSV files** and converts them into a column-based dictionary.  

## ⚙️ Functions  

### 🔹 `load_table(filepath: str) → dict`  
- Detects file type based on **extension**.  
- Loads and **decodes** the table using the corresponding decoder.  

### 🔹 `main()`  
- Prints **available decoders**.  
- Loads a sample JSON table and **prints** the result.  

## 🚀 Usage  
Run the script:  
```bash
python table_encoders.py
```

This will print the available decoders (['json', 'csv']),
load and print the content of table.json in dictionary format,
i.e. for the table.json :
~~~python
['json', 'csv']
{'temperature': [2, 8, 12], 'time': [7, 10, 15]}
~~~

## 🌍 Made with ❤️ by  

**Piotr Lipiński**  

Contributions, issues, and feedback are welcome! 🤝  
