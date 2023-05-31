"""
Small test programm to check distribution of test rates for Belarusian Exams.
Uses:
* tabula-py
* pandas

! Ensure Java is installed & acessible via PATH.java
"""

import pandas as pd
import numpy as np
import tabula
# import PyPDF2

import seaborn as sns

if __name__ == "__main__":
    print("Test Run done well.")
    
    pdf_file_path = "./pdf/01-02.pdf"
    dfs = tabula.read_pdf(pdf_file_path,pages="all")
    
    print(len(dfs))
    print(dfs)
    
    dfs[1] = (dfs[1].T.reset_index().T.reset_index(drop=True).set_axis(
        [
            "Первичный\rбалл",
            "Тестовый\rбалл"
        ],
        axis=1
    ))
    
    df = pd.concat(dfs, ignore_index=True)
    
    df.to_csv("./test_rate.csv")
    
    print("Saved to CSV!")