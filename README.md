# FastAPI + Vercel Deployment

This project is a simple **FastAPI** backend deployed on **Vercel**. It demonstrates how to serve APIs in a serverless environment with minimal configuration.

## 🚀 Deployment URL
Production Deployment:  
[https://bfhl-fastapi-22bds0378.vercel.app](https://bfhl-fastapi-22bds0378.vercel.app)

## Example cURL Requests
```
curl -X POST https://bfhl-fastapi-22bds0378.vercel.app/bfhl \
  -H "Content-Type: application/json" \
  -d '{"data":["a","1","334","4","R","$"]}'
```

## Expected output 
``
{ "is_success": true, "user_id": "Pranav_Madhu_26092004", "email": "pranavm2323@gmail.com", "roll_number": "22BDS0378", "odd_numbers": ["1"], "even_numbers": ["334", "4"], "alphabets": ["A", "R"], "special_characters": ["$"], "sum": "339", "concat_string": "Ra" }
``
