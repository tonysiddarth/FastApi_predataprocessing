

📊 Data Preprocessing API using FastAPI

A FastAPI-based REST API that accepts Excel files, performs automatic data cleaning and preprocessing using Pandas, and returns a cleaned dataset summary and preview.



🚀 Features

Features

1.Upload Excel files (.xlsx)

2.Standardizes column names (lowercase & trimmed)

3.Trims extra spaces in string columns

4.Handles missing values:

    Numerical columns → filled with mean

    Categorical columns → filled with mode

5.Removes duplicate rows

6.Automatically converts data types

7.Returns:

    1.Number of rows

    2.Number of columns

    3.Cleaned data preview

    4.Number of rows

    5.Number of columns

    6.Cleaned data preview


    
🛠️ Tech Stack

Python

FastAPI

Pandas

Uvicorn
