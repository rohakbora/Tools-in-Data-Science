from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import re
import json

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

def extract_int(param_str: str) -> int:
    try:
        return int(param_str)
    except ValueError:
        raise HTTPException(status_code=400, detail=f"Invalid integer value: {param_str}")

@app.get("/execute")
def execute(q: str = Query(..., description="Query string")):
    # Define regex patterns for each function

    # 1) get_ticket_status(ticket_id: int)
    m = re.match(r"^What is the status of ticket (\d+)\?$", q)
    if m:
        ticket_id = extract_int(m.group(1))
        return {
            "name": "get_ticket_status",
            "arguments": json.dumps({"ticket_id": ticket_id})
        }

    # 2) schedule_meeting(date: str, time: str, meeting_room: str)
    m = re.match(r"^Schedule a meeting on (\d{4}-\d{2}-\d{2}) at (\d{2}:\d{2}) in (.+)\.$", q)
    if m:
        date = m.group(1)
        time = m.group(2)
        meeting_room = m.group(3)
        return {
            "name": "schedule_meeting",
            "arguments": json.dumps({
                "date": date,
                "time": time,
                "meeting_room": meeting_room
            })
        }

    # 3) get_expense_balance(employee_id: int)
    m = re.match(r"^Show my expense balance for employee (\d+)\.$", q)
    if m:
        employee_id = extract_int(m.group(1))
        return {
            "name": "get_expense_balance",
            "arguments": json.dumps({"employee_id": employee_id})
        }

    # 4) calculate_performance_bonus(employee_id: int, current_year: int)
    m = re.match(r"^Calculate performance bonus for employee (\d+) for (\d{4})\.$", q)
    if m:
        employee_id = extract_int(m.group(1))
        current_year = extract_int(m.group(2))
        return {
            "name": "calculate_performance_bonus",
            "arguments": json.dumps({
                "employee_id": employee_id,
                "current_year": current_year
            })
        }

    # 5) report_office_issue(issue_code: int, department: str)
    m = re.match(r"^Report office issue (\d+) for the (.+) department\.$", q)
    if m:
        issue_code = extract_int(m.group(1))
        department = m.group(2)
        return {
            "name": "report_office_issue",
            "arguments": json.dumps({
                "issue_code": issue_code,
                "department": department
            })
        }

    # If no pattern matches
    raise HTTPException(status_code=400, detail="Unsupported query format")