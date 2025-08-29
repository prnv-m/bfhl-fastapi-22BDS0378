from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import re
from mangum import Mangum   # adapter for serverless

app = FastAPI()

# ---------- CONFIG ----------
FULL_NAME = "Pranav_Madhu"
DOB = "26092004"
EMAIL = "pranavm2323@gmail.com"
ROLL_NUMBER = "22BDS0378"

class DataRequest(BaseModel):
    data: List[str]

def is_integer(value: str) -> bool:
    return re.fullmatch(r"-?\d+", value) is not None

def alternating_caps(s: str) -> str:
    result = []
    upper = True
    for ch in s[::-1]:
        if ch.isalpha():
            result.append(ch.upper() if upper else ch.lower())
            upper = not upper
    return "".join(result)

@app.post("/bfhl")
async def process_data(req: DataRequest):
    try:
        data = req.data
        odd_numbers, even_numbers, alphabets, specials = [], [], [], []
        sum_numbers = 0
        concat_src = []

        for item in data:
            if is_integer(item):
                num = int(item)
                (even_numbers if num % 2 == 0 else odd_numbers).append(item)
                sum_numbers += num
            elif item.isalpha():
                alphabets.append(item.upper())
                concat_src.append(item)
            else:
                specials.append(item)

        return {
            "is_success": True,
            "user_id": f"{FULL_NAME}_{DOB}",
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": specials,
            "sum": str(sum_numbers),
            "concat_string": alternating_caps("".join(concat_src))
        }
    except Exception as e:
        return {"is_success": False, "user_id": f"{FULL_NAME}_{DOB}", "error": str(e)}

# Mangum adapter for Vercel serverless
handler = Mangum(app)
