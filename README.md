# Duplicate File Detector (Command Line Tool)

## Overview
Duplicate files accumulate over time due to repeated downloads, backups, or file copies.
These duplicates waste storage space and make file management difficult.

This project is a Python-based command-line tool that scans a directory,
detects duplicate files using cryptographic hashing, and optionally removes them
after user confirmation.

---

## Problem Statement
Manually identifying duplicate files in large folders such as Downloads or Documents
is time-consuming and error-prone. Operating systems do not provide a reliable built-in
solution to detect duplicates based on file content.

---

## Solution
This tool automatically:
- Scans all files inside a given directory (recursively)
- Generates a SHA-256 hash for each file
- Groups files with identical hashes as duplicates
- Displays duplicate files clearly
- Optionally deletes duplicate copies safely

---

## How the System Works
1. The program walks through all subfolders using `os.walk`
2. Each file is read in binary mode in chunks
3. A SHA-256 hash is generated for file content
4. Files with the same hash are grouped
5. Duplicate groups are printed
6. If delete mode is enabled, user confirmation is requested
7. Only duplicate copies are removed (original file remains)

---

## Requirements
- Python 3.x
- No external libraries required

---

## How to Run the Program

### Basic Scan (No Deletion)
```bash
python duplicate_finder.py <folder_path>
