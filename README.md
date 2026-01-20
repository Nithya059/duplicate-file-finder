# Duplicate File Finder – Python CLI Tool

## Problem
My system had thousands of files in Downloads and Desktop with many duplicate PDFs, images and documents.
This wastes disk space and makes file management difficult.

## Solution
This tool scans a folder, detects duplicate files using SHA-256 hashing, and optionally deletes them safely.

## Features
- Recursively scans folders
- Detects duplicates using cryptographic hashing
- Safe delete mode with confirmation
- Works on Windows/Linux/Mac

## How to Run

1. Open Command Prompt  
2. Go to project folder:
   cd C:\Users\Lenovo\Desktop\duplicate_finder

3. Scan only:
   python duplicate_finder.py C:\Users\Lenovo\Downloads

4. Scan and delete:
   python duplicate_finder.py C:\Users\Lenovo\Downloads --delete

## Design Decisions
- Used SHA-256 because filenames are unreliable  
- Used argparse for clean CLI design  
- Delete mode requires human confirmation for safety

## Future Improvements
- Progress bar  
- Ignore file types  
- GUI version  
- Cloud storage support
