from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import tensorflow as tf
import numpy as np
from PIL import Image
import uvicorn

model = tf.keras.models.load_model("models/best-23-10-2024.keras")

# Função para pré-processar a imagem
def preprocess_image(image):
    # Converte para RGB caso a imagem esteja em escala de cinza
    if image.mode != "RGB":
        image = image.convert("RGB")
    
    image = image.resize((256, 256))
    
    image = np.array(image) / 255.0

    image = image.reshape(1, 256, 256, 3)
    
    return image

# Função para converter a previsão em porcentagens
def format_prediction(prediction):
    cancer_prob = prediction[0][0] * 100  # Probabilidade de "Câncer"
    normal_prob = prediction[0][1] * 100  # Probabilidade de "Normal"
    return {
        "prediction": {
            "cancer": f"{cancer_prob:.2f}%",
            "normal": f"{normal_prob:.2f}%"
        }
    }

# Função de previsão
def predict(image: Image.Image):
    processed_image = preprocess_image(image)

    raw_prediction = model.predict(processed_image).tolist()

    return format_prediction(raw_prediction)

app = FastAPI(title="Previsão de Câncer de Mama")

@app.post("/predict/")
async def predict_image(file: UploadFile = File(...)):
    try:
        image = Image.open(file.file)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao processar a imagem: {e}")

    prediction = predict(image)
    return JSONResponse(content=prediction)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
