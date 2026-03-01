from fastapi import FastAPI

from models import PhoneRecord, UpdatePhoneRecord
from typing import Dict
from fastapi import HTTPException

app = FastAPI()

records : Dict[int, dict] = {}

next_id = 1

@app.post("/records")
def create_record(record: PhoneRecord):
    global next_id
    records[next_id] = record.model_dump()
    records[next_id]["id"] = next_id
    next_id += 1
    return {"message": "Record created", "record": records[next_id - 1]}

@app.get("/records/{record_id}")
def read_record(record_id: int):
    if record_id not in records:
        raise HTTPException(status_code=404, detail="Record not found")
    return records[record_id]

@app.put("/records/{record_id}")
def update_record(record_id: int, record: UpdatePhoneRecord):
    if record_id not in records:
        raise HTTPException(status_code=404, detail="Record not found")
    
    existing_record = records[record_id]
    
    updated_record = record.model_dump(exclude_unset=True)
    
    existing_record.update(updated_record)
    
    return {"message": "Record updated", "record": existing_record}

@app.delete("/records/{record_id}")
def delete_record(record_id: int):
    if record_id not in records:
        raise HTTPException(status_code=404, detail="Record not found")
    
    del records[record_id]
    
    return {"message": "Record deleted"}

@app.get("/records")
def list_records():
    return list(records.values())