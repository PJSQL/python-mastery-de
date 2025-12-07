# python-mastery-de

# Python Mastery for Data Engineers  
A complete 10-week curriculum designed to take you from “I can hack together Python scripts” to having a deep, confident understanding of Python — with a strong focus on data engineering workflows, performance, reliability, and production-grade patterns.

This repository contains:
- A structured 10-week learning plan  
- Daily exercises  
- Hands-on projects  
- A full mini-library (`etl_utils`) that you’ll build step-by-step  
- Capstone projects to demonstrate mastery

Python becomes *much* more powerful once you understand its mental models — iterators, generators, object references, error handling, and modular design. This repo is built to give you that foundation.

---

# 📚 Curriculum Overview

This curriculum is divided into **10 modules**, each representing one week of focused learning and practice.  
Every module includes:
- Concept explanations  
- Example scripts  
- Exercises  
- A small project to apply the concepts  
- A directory in this repo with starter or completed code  

## **Module List**
1. **Python Basics & Core Mental Model**  
2. **Control Flow & Pythonic Logic**  
3. **Functions, Type Hints & Clean Code**  
4. **Iterables, Iterators & Generators**  
5. **Exceptions, Logging & Context Managers**  
6. **Modules, Packages & Virtual Environments**  
7. **File I/O, JSON, CSV & Data Normalization**  
8. **APIs, SQL, and ETL Patterns**  
9. **Polars, Pandas & Arrow for High-Performance Data Processing**  
10. **Capstone Project (ETL Framework, Polars Pipeline, or API CLI Tool)**

You can complete this program in **10 weeks**, working 30–60 minutes per weekday — or go at your own pace.

---

# 🗂 Repository Structure

python-mastery-de/
│
├── README.md
├── .gitignore
├── requirements.txt
│
├── module_01_basics/
│ ├── variables_and_types.py
│ ├── collections.py
│ ├── mutability_demo.py
│ ├── word_counter.py
│ └── exercises/
│ └── practice_problems.md
│
├── module_02_control_flow/
│ ├── conditionals.py
│ ├── loops.py
│ ├── comprehensions.py
│ ├── json_filtering.py
│ └── exercises/
│ └── practice_problems.md
│
├── module_03_functions/
│ ├── functions_basics.py
│ ├── type_hints.py
│ ├── closures_scope.py
│ ├── data_cleaner.py
│ └── exercises/
│ └── practice_problems.md
│
├── module_04_iterators_generators/
│ ├── iterables_vs_iterators.py
│ ├── generators.py
│ ├── generator_csv_reader.py
│ ├── chunk_processing_example.py
│ └── exercises/
│ └── practice_problems.md
│
├── module_05_exceptions_logging/
│ ├── try_except_examples.py
│ ├── custom_exceptions.py
│ ├── logging_setup.py
│ ├── db_connection_manager.py
│ └── exercises/
│ └── practice_problems.md
│
├── module_06_modules_packages/
│ ├── etl_utils/
│ │ ├── init.py
│ │ ├── cleaner.py
│ │ ├── validator.py
│ │ ├── logger.py
│ │ ├── db.py
│ │ └── config.py
│ ├── example_project/
│ │ └── main.py
│ └── exercises/
│ └── practice_problems.md
│
├── module_07_file_io_data/
│ ├── json_normalizer.py
│ ├── csv_reader_writer.py
│ ├── pathlib_examples.py
│ ├── file_processing_pipeline.py
│ └── exercises/
│ └── practice_problems.md
│
├── module_08_api_sql_etl/
│ ├── api_pagination.py
│ ├── api_retry_handler.py
│ ├── sql_loader_pyodbc.py
│ ├── sql_loader_sqlalchemy.py
│ ├── full_etl_pipeline.py
│ └── exercises/
│ └── practice_problems.md
│
├── module_09_polars_arrow/
│ ├── pandas_vs_polars_benchmark.py
│ ├── parquet_reader_arrow.py
│ ├── transformations_polars.py
│ ├── memory_benchmarking.py
│ └── exercises/
│ └── practice_problems.md
│
└── module_10_capstone/
├── capstone_etl_framework/
│ ├── config.yaml
│ ├── extract.py
│ ├── transform.py
│ ├── load.py
│ ├── log.py
│ └── run.py
├── capstone_polars_project/
│ ├── data/
│ ├── benchmark.py
│ ├── transform.py
│ └── report.md
└── capstone_api_cli/
├── cli.py
├── api.py
├── config.py
└── readme.md



Each directory contains code, examples, and exercises for that topic.

---

# 🗓 10-Week Daily Learning Schedule

The full schedule is included in the `/schedule/` section (or you can follow it from this README). Each day takes roughly 30–60 minutes.  
The schedule balances:
- Learning new concepts  
- Doing targeted exercises  
- Building real projects  
- Checking your understanding  

You’ll push each week’s work to the repository so you can track progression over time.

---

# 🏗 Capstone Projects

By Week 10, you’ll choose one of three full-scale data engineering projects:

### **🔹 Capstone A — ETL Framework**
A configurable extract → transform → load system using:
- Logging  
- Error handling  
- Config files  
- SQL loading  
- Modular architecture  

### **🔹 Capstone B — High-Performance Polars Pipeline**
Process large data efficiently using:
- Polars  
- PyArrow  
- Parquet  
- Benchmarks vs Pandas  

### **🔹 Capstone C — API CLI Tool**
A command-line application that:
- Accepts an API endpoint + config  
- Handles pagination  
- Implements retries  
- Saves data to disk or SQL  

Each option demonstrates real professional Python skills.

---

# 🧰 Requirements

Install dependencies with:

```bash
pip install -r requirements.txt

