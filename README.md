# Duplicate File Detector Using Python

## 1. Project Title
Duplicate File Detector Using SHA-256 Hashing

---

## 2. Problem Statement

In modern computer systems, users often store the same files multiple times without realizing it. This happens due to repeated downloads, file sharing, backups, or copying files into different folders. These duplicate files consume unnecessary disk space and make file organization difficult.

Manually identifying duplicate files is inefficient and error-prone, especially when files have different names but identical content. Therefore, an automated solution is required to accurately detect duplicate files.

---

## 3. Objective

The objectives of this project are:

- To identify duplicate files based on file content
- To scan directories and subdirectories automatically
- To use a secure hashing algorithm for accuracy
- To display duplicate files safely without modifying or deleting them
- To help users manage storage efficiently

---

## 4. Technology Used

- Programming Language: Python
- Hashing Algorithm: SHA-256
- Operating System: Windows
- Execution Method: Command Line Interface

---

## 5. System Requirements

### Hardware Requirements
- Minimum 4 GB RAM
- Any modern processor
- Adequate storage space

### Software Requirements
- Python 3.x
- Windows Operating System
- Command Prompt

---

## 6. Project Description

The Duplicate File Detector scans a specified directory and all its subdirectories. Each file is read in chunks to handle large files efficiently. A SHA-256 hash is generated for each file.

Files producing the same hash value are grouped together and identified as duplicate files. This method ensures accuracy because identical content always results in the same hash, regardless of file name.

---

## 7. How the Project Works

1. User provides a directory path
2. Program scans all files recursively
3. Each file is hashed using SHA-256
4. Hash values are stored and compared
5. Files with matching hashes are marked as duplicates
6. Duplicate files are displayed in the terminal

---

## 8. Execution Steps

1. Open Command Prompt
2. Navigate to the project directory
3. Run the Python file with target folder path as argument

Example:
python duplicate_finder.py C:\Users\Lenovo\Downloads

---

## 9. Sample Output

DUPLICATE FILES FOUND:

Hash: 617fc84710b30ffe2d1c5ae07253d2272cca2c0ae3c27e0de47a4791723f9ab5
   C:\Users\Lenovo\Downloads\DocScanner 26-Dec-2025 (1).pdf
   C:\Users\Lenovo\Downloads\DocScanner 26-Dec-2025.pdf

Hash: f163ca541160a8751776c14a1775ab679b900a1b2ac0568cd9eb20409ba6fc19
   C:\Users\Lenovo\Downloads\WhatsApp Image (1).jpeg
   C:\Users\Lenovo\Downloads\WhatsApp Image.jpeg

---

## 10. Execution Proof

The program was executed successfully on a local Windows system.

Screenshots of the following are stored in the screenshots/ folder:
- Program execution
- Duplicate detection output
- Terminal results

---

## 11. Assumptions

- Files with identical content produce identical hash values
- User has permission to read target directory
- Hash collisions are extremely rare
- Files are accessible during scanning
- No files are modified or deleted automatically

---

## 12. Edge Cases Handled

- Nested directories
- Large files processed in chunks
- Files with same name but different content
- Files with different names but same content

---

## 13. Limitations

- Cannot detect similar files with small content differences
- No graphical user interface
- Performance decreases with very large directories
- Cannot preview file contents

---

## 14. Security Considerations

- Uses SHA-256 cryptographic hashing
- Does not modify or delete files
- Safe read-only operations
- No external data transmission

---

## 15. Future Enhancements

- Add graphical user interface (GUI)
- Export duplicate report to Word or PDF
- Add optional file deletion feature
- Improve performance using multithreading
- Cloud storage integration

---

## 16. Applications

- Disk cleanup utilities
- Backup optimization
- File system maintenance
- Digital forensics
- Storage management tools

---

## 17. Conclusion

This project successfully identifies duplicate files using cryptographic hashing techniques. It provides a reliable and efficient solution for managing duplicate data and optimizing storage space. The project demonstrates strong understanding of file handling, recursion, and hashing in Python.

---

## 18. Author Details

Name: Nithya H S  
Project Type: Mini Project  
Technology: Python
