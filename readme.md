# 📘 DSBDA Practicals Repository

This repository contains all practical assignments for **Data Science and Big Data Analytics (DSBDA)** subject.

The practicals are implemented using:

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Hadoop MapReduce (Some Practicals)

---

# 📂 Repository Structure

```text
Practical1/
Practical2/
Practical3/
...
Practical13/
```

Each folder contains:
- Jupyter Notebook (`.ipynb`)
- Dataset files (`.csv`, `.txt`)
- Python programs
- Output screenshots (if available)

---

# ⚙️ Software Requirements

Install the following software before running the practicals.

## 1️⃣ Install Python

Download Python from:

[Python Official Website](https://www.python.org/downloads/?utm_source=chatgpt.com)

### ✅ Important:
During installation check:

```text
✔ Add Python to PATH
```

---

# 🧪 Verify Python Installation

Open Command Prompt and run:

```bash
python --version
```

Example:

```text
Python 3.12.0
```

---

# 📓 Install Jupyter Notebook

Run this command in Command Prompt or Terminal:

```bash
pip install notebook
```

---

# 📦 Install Required Python Libraries

Run:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn nltk
```

---

# 🚀 Start Jupyter Notebook

Open terminal in project folder and run:

```bash
jupyter notebook
```

Jupyter Notebook will open automatically in your browser.

---

# ▶️ How to Run Practicals

## Step 1:
Open the required practical folder.

Example:

```text
Practical5/
```

---

## Step 2:
Open the `.ipynb` notebook file.

Example:

```text
practical5.ipynb
```

---

## Step 3:
Run each cell using:

```text
Shift + Enter
```

---

# 📊 Common Libraries Used

| Library | Purpose |
|---|---|
| Pandas | Data Handling |
| NumPy | Numerical Operations |
| Matplotlib | Data Visualization |
| Scikit-learn | Machine Learning |
| NLTK | Natural Language Processing |

---

# 📁 Dataset Information

Datasets used in this repository include:

- Student Performance Dataset
- Iris Dataset
- Titanic Dataset
- Weather Dataset
- Social Network Ads Dataset
- Academic Performance Dataset

Datasets are available inside corresponding practical folders.

---

# 🖥️ Hadoop MapReduce Practicals

Some practicals use Hadoop Streaming with Python Mapper and Reducer files.

### Hadoop Streaming Command Example

```bash
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-input sample.txt \
-output output \
-mapper mapper.py \
-reducer reducer.py
```

---

# 🔧 Useful Commands

## Install all dependencies

```bash
pip install -r requirements.txt
```

---

## Create virtual environment

```bash
python -m venv venv
```

---

## Activate virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

# ❗ Common Errors & Solutions

## Error:
```text
ModuleNotFoundError
```

### Solution:
Install missing library using:

```bash
pip install library_name
```

---

## Error:
```text
jupyter is not recognized
```

### Solution:

```bash
pip install notebook
```

---

## Error:
```text
FileNotFoundError
```

### Solution:
Check:
- Correct dataset path
- Dataset exists in project folder

---

# 📚 Subjects Covered

- Data Wrangling
- Data Visualization
- Machine Learning
- NLP
- Hadoop MapReduce
- Regression
- Classification
- Clustering

---

# 👨‍💻 Author

## Vishal Bankar

Computer Engineering Student  
DSBDA Practicals Repository

---

# ⭐ If this repository helped you

Give it a ⭐ on GitHub.