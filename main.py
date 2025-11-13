# pip freeze > requirements.txt
# pip install -r requirements.txt

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import caesar
import fence
app = FastAPI()

class TextCaesar(BaseModel):
    text: str
    offset: int
    mode: str

class TextFence(BaseModel):
    text: str

@app.get("/test")
def read_root():
    return {"msg": "Hi from test"}

@app.get("/test/{name}")
def save_name(name: str):
    with open("names.txt", "a") as f:
        f.write(name + "\n")

        
@app.post("/caesar")
def caesar(textCaesar : TextCaesar):
    if textCaesar.mode == "encrypt":
        return {"encrypted_text" : caesar.encrypt(textCaesar.text, textCaesar.offset)}
    elif textCaesar.mode == "decrypt":
        return {"decrypted_text" : caesar.decrypt(textCaesar.text, textCaesar.offset)}
    else:
        raise HTTPException(100,"Invalid mode")


@app.get("/fence/encrypt")
def fence_encrypt(text):
    return {"encrypted_text" : fence.encrypt(text)}


@app.post("/fence/decrypt")
def fence(textFence : TextFence):
    return {"decrypted_text" : fence.decrypt(textFence.text)}










