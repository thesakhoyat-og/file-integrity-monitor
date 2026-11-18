# 🔐 File Integrity Monitor

A Python-based File Integrity Monitoring (FIM) tool that uses SHA-256 hashing to detect changes in files.

## 📌 Project Overview

The File Integrity Monitor is a beginner-friendly cybersecurity project developed using Python.

It monitors files by generating SHA-256 fingerprints and comparing them against previously stored fingerprints in a baseline JSON file.

The program identifies whether files have been modified, deleted, newly added, or remain unchanged.

## ✨ Features

- **SHA-256 Hashing:** Generates unique fingerprints for files using Python's `hashlib` library.
- **Baseline Creation:** Stores original file fingerprints in a JSON file.
- **Modified File Detection:** Detects changes in file contents.
- **Deleted File Detection:** Identifies files removed after baseline creation.
- **New File Detection:** Identifies files added after baseline creation.
- **Unchanged File Detection:** Confirms files that have not been modified.
- **Interactive Menu:** Allows users to create a baseline or monitor files.

## 🛠️ Technologies Used

- Python 3
- hashlib
- pathlib
- json

## 📂 Project Structure

```text
file-integrity-monitor/
│
├── files/
│   ├── document.txt
│   ├── config.txt
│   └── notes.txt
│
├── main.py
├── baseline.json
└── README.md
```

## ⚙️ How It Works

1. The user creates an initial baseline of the files.
2. The program calculates SHA-256 hashes for each file.
3. The original filenames and hashes are stored in `baseline.json`.
4. During monitoring, the program generates new hashes.
5. The new hashes are compared against the original baseline.
6. The program reports detected changes.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
```

### 2. Navigate to the project directory

```bash
cd file-integrity-monitor
```

### 3. Run the program

```bash
python main.py
```

### 4. Choose an option

```text
===== FILE INTEGRITY MONITOR =====

1. Create baseline
2. Monitor files
```

- Select `1` to create or reset the original baseline.
- Select `2` to monitor files against the existing baseline.

**Important:** Create the baseline before starting normal monitoring. Creating a new baseline replaces the previous one.

## 🧪 Example Output

```text
document.txt Unchanged
config.txt Modified
notes.txt DELETED
extra.txt NEW FILE DETECTED
```

## 🎯 Learning Objectives

Through this project, I practised:

- Python file handling
- Dictionaries and loops
- Functions and function calls
- SHA-256 hashing
- JSON data storage
- File system operations
- Basic cybersecurity and file integrity monitoring concepts

## 🔮 Future Improvements

- Add logging and error handling.
- Support monitoring subdirectories.
- Generate detailed monitoring reports.
- Add command-line arguments.
- Improve baseline protection.

## 👨‍💻 Author

Developed as a Python and cybersecurity learning project.