# file_handling_-_Exception_Handling
#  File Handling & Error Management Tool

##  Overview

This Python-based utility script is designed to read a text file, apply a chosen transformation to its contents, and write the modified output to a new file — all while handling file-related errors gracefully.

> **Use Case:** Ideal for beginners and intermediates learning about file I/O and exception handling in Python. 

---

##  Features

✅ Reads a user-specified file line by line  
✅ Applies one of three text transformations:
- `UPPERCASE`
- `lowercase`
- `Title Case`

✅ Writes the transformed content to a new file  
✅ Prompts user before overwriting existing output  
✅ Exception handling for:
- File not found
- Permission errors
- Unexpected read/write failures

✅ Line counter + user-friendly CLI messages  
✅ Memory-efficient: line-by-line processing

---

##  How It Works

1. **Run the script:**
   ```bash
   python3 file_processor.py
