from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any
import sqlite3
import json
from datetime import datetime

app = FastAPI(title="SonicAnalytics Lab API")

# 開放跨域存取 (CORS)，讓受試者在任何網頁都能 POST 資料進來
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 初始化 SQLite 資料庫
def init_db():
    conn = sqlite3.connect("experiment_data.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS experiment_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject_id TEXT,
            condition TEXT,
            trial_id INTEGER,
            reaction_time REAL,
            t_stimulus REAL,
            t_response REAL,
            lang TEXT,
            tlx_mental INTEGER,
            tlx_physical INTEGER,
            tlx_temporal INTEGER,
            tlx_performance INTEGER,
            tlx_effort INTEGER,
            tlx_frustration INTEGER,
            created_at TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

init_db()

# 資料結構驗證模型
class TrialItem(BaseModel):
    subject_id: str
    trial_id: int
    condition: str
    rt: float
    t_stimulus: str
    t_response: str
    lang: str

class ExperimentPayload(BaseModel):
    subject_id: str
    created_at: str
    trials: List[TrialItem]
    tlx: Dict[str, Any]

@app.post("/api/v1/submit")
async def submit_experiment(payload: ExperimentPayload):
    try:
        conn = sqlite3.connect("experiment_data.db")
        cursor = conn.cursor()
        
        for t in payload.trials:
            tlx_item = payload.tlx.get(t.condition, {}) or {}
            cursor.execute("""
                INSERT INTO experiment_records (
                    subject_id, condition, trial_id, reaction_time,
                    t_stimulus, t_response, lang,
                    tlx_mental, tlx_physical, tlx_temporal,
                    tlx_performance, tlx_effort, tlx_frustration,
                    created_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                t.subject_id, t.condition, t.trial_id, t.rt,
                float(t.t_stimulus), float(t.t_response), t.lang,
                tlx_item.get("mental"), tlx_item.get("physical"), tlx_item.get("temporal"),
                tlx_item.get("perf"), tlx_item.get("effort"), tlx_item.get("frust"),
                datetime.utcnow()
            ))
            
        conn.commit()
        conn.close()
        return {"status": "success", "message": f"Successfully recorded {len(payload.trials)} trials."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/health")
def health_check():
    return {"status": "online", "server": "Asustor Private Node"}