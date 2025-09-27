import sqlite3
import json
from datetime import datetime
from uuid import UUID, uuid4
from typing import List, Optional
from models import Report, ReportCreate

class DatabaseManager:
    def __init__(self, db_path: str = "reports.db"):
        self.db_path = db_path
        self._init_database()
    
    def _init_database(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS reports (
                    id TEXT PRIMARY KEY,
                    title TEXT NOT NULL,
                    content TEXT NOT NULL,
                    tags TEXT NOT NULL,
                    date TEXT NOT NULL
                )
            """)
            conn.execute("CREATE INDEX IF NOT EXISTS idx_tags ON reports(tags)")
            conn.commit()
    
    def create_report(self, report_data: ReportCreate) -> Report:
        report_id = str(uuid4())
        report = Report(
            id=report_id,
            title=report_data.title,
            content=report_data.content,
            tags=report_data.tags,
            date=datetime.now()
        )
        
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "INSERT INTO reports (id, title, content, tags, date) VALUES (?, ?, ?, ?, ?)",
                (report_id, report.title, report.content, json.dumps(report.tags), report.date.isoformat())
            )
            conn.commit()
        
        return report
    
    def get_report(self, report_id: str) -> Optional[Report]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                "SELECT id, title, content, tags, date FROM reports WHERE id = ?",
                (report_id,)
            )
            row = cursor.fetchone()
            
            if not row:
                return None
            
            return Report(
                id=row[0],
                title=row[1],
                content=row[2],
                tags=json.loads(row[3]),
                date=datetime.fromisoformat(row[4])
            )
    
    def get_reports(self, tag: Optional[str] = None, search: Optional[str] = None) -> List[Report]:
        query = "SELECT id, title, content, tags, date FROM reports"
        params = []
        conditions = []
        
        if tag:
            conditions.append("tags LIKE ?")
            params.append(f'%"{tag}"%')
        
        if search:
            conditions.append("(title LIKE ? OR content LIKE ?)")
            search_param = f"%{search}%"
            params.extend([search_param, search_param])
        
        if conditions:
            query += " WHERE " + " AND ".join(conditions)
        
        query += " ORDER BY date DESC"
        
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(query, params)
            rows = cursor.fetchall()
            
            return [
                Report(
                    id=row[0],
                    title=row[1],
                    content=row[2],
                    tags=json.loads(row[3]),
                    date=datetime.fromisoformat(row[4])
                )
                for row in rows
            ]

db_manager = DatabaseManager()
