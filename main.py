# pip freeze > requirements.txt
# pip install -r requirements.txt

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from caesar import caesar_encrypt, caesar_decrypt
from fence import fence_encrypt_text, fence_decrypt_text

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
    return {"msg": "saved user"}


@app.post("/caesar")
def caesar(textCaesar : TextCaesar):
    if textCaesar.mode == "encrypt":
        return {"encrypted_text" : caesar_encrypt(textCaesar.text, textCaesar.offset)}
    elif textCaesar.mode == "decrypt":
        return {"decrypted_text" : caesar_decrypt(textCaesar.text, textCaesar.offset)}
    else:
        raise HTTPException(100,"Invalid mode")


@app.get("/fence/encrypt")
def fence_encrypt(text : str):
    return {"encrypted_text" : fence_encrypt_text(text)}


@app.post("/fence/decrypt")
def fence_decrypt(textFence : TextFence):
    return {"decrypted_text" : fence_decrypt_text(textFence.text)}










