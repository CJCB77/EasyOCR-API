from fastapi import FastAPI, UploadFile
import easyocr

app = FastAPI()

reader = easyocr.Reader(['en'], gpu=False)

@app.get("/")
def read_root():
    return {"Message": "API EasyOCR"}


@app.post("/read")
async def read_image(
    image:UploadFile = UploadFile(...)
):
    image_bytes = await image.read()
    text = reader.readtext(image_bytes,detail = 0, allowlist ='0123456789')
    print(text)
    # Get number with the most characters
    lectura = max(text, key=lambda x: len(x))
    print(lectura)
    return int(lectura)

    
  
    

