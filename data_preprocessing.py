
from fastapi import  FastAPI, UploadFile, File, HTTPException
import pandas as pd
 
app=FastAPI()
def preprocessing_data(df: pd.DataFrame):
    df.columns=df.columns.str.lower().str.strip()
    df=df.apply(
        lambda col: col.str.strip() if col.dtype== "object" else col
        
    )
    
    for col in df.columns:
        if df[col].dtype in ["int64" , "float64"]:
                df[col]=df[col].fillna(df[col].mean())
        elif df[col].dtype ==object:
                df[col]=df[col].fillna(df[col].mode()[0])


    df=df.drop_duplicates()
    df=df.convert_dtypes()
    return df

@app.post("/upload-file")
async def data_(file: UploadFile=File(...)):
    df=pd.read_excel(file.file)
    df=preprocessing_data(df)
    return {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "previews": df.to_dict(orient="records")
    
    }
