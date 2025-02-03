import uvicorn
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse

from src.lib.Features.Features import Features
from src.services.model_service import predict, upload_data

app = FastAPI()

@app.post("/upload")
async def upload_data_handler(file: UploadFile = File(...)):
    try:
        upload_data(file)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.post("/predict")
async def predict_handler(features: Features):
    prediction = predict(features)
    return {"predicted_price": prediction}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)