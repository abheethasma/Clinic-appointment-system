from fastapi import FastAPI, HTTPException, Body
from fastapi.responses import JSONResponse, Response
import httpx
from typing import Any

app = FastAPI(title="API Gateway", version="1.0.0")

SERVICES = {
    "patient": "http://localhost:8001",
    "doctor": "http://localhost:8002",
    "appointment": "http://localhost:8003",
    "feedback": "http://localhost:8004"
}


async def forward_request(service: str, path: str, method: str, **kwargs) -> Any:
    if service not in SERVICES:
        raise HTTPException(status_code=404, detail="Service not found")

    url = f"{SERVICES[service]}{path}"

    async with httpx.AsyncClient() as client:
        try:
            if method == "GET":
                response = await client.get(url, **kwargs)
            elif method == "POST":
                response = await client.post(url, **kwargs)
            elif method == "PUT":
                response = await client.put(url, **kwargs)
            elif method == "DELETE":
                response = await client.delete(url, **kwargs)
            else:
                raise HTTPException(status_code=405, detail="Method not allowed")

            if response.status_code == 204:
                return Response(status_code=204)

            content_type = response.headers.get("content-type", "")

            if "application/json" in content_type:
                return JSONResponse(
                    content=response.json(),
                    status_code=response.status_code
                )

            return Response(
                content=response.text,
                status_code=response.status_code,
                media_type=content_type or "text/plain"
            )

        except httpx.RequestError as e:
            raise HTTPException(status_code=503, detail=f"Service unavailable: {str(e)}")


@app.get("/")
def read_root():
    return {
        "message": "API Gateway is running",
        "available_services": list(SERVICES.keys())
    }


# Patient routes
@app.get("/gateway/patients")
async def get_all_patients():
    return await forward_request("patient", "/api/patients", "GET")


@app.get("/gateway/patients/{patient_id}")
async def get_patient(patient_id: int):
    return await forward_request("patient", f"/api/patients/{patient_id}", "GET")


@app.post("/gateway/patients")
async def create_patient(payload: dict = Body(...)):
    return await forward_request("patient", "/api/patients", "POST", json=payload)


@app.put("/gateway/patients/{patient_id}")
async def update_patient(patient_id: int, payload: dict = Body(...)):
    return await forward_request("patient", f"/api/patients/{patient_id}", "PUT", json=payload)


@app.delete("/gateway/patients/{patient_id}")
async def delete_patient(patient_id: int):
    return await forward_request("patient", f"/api/patients/{patient_id}", "DELETE")


# Doctor routes
@app.get("/gateway/doctors")
async def get_all_doctors():
    return await forward_request("doctor", "/api/doctors", "GET")


@app.get("/gateway/doctors/{doctor_id}")
async def get_doctor(doctor_id: int):
    return await forward_request("doctor", f"/api/doctors/{doctor_id}", "GET")


@app.post("/gateway/doctors")
async def create_doctor(payload: dict = Body(...)):
    return await forward_request("doctor", "/api/doctors", "POST", json=payload)


@app.put("/gateway/doctors/{doctor_id}")
async def update_doctor(doctor_id: int, payload: dict = Body(...)):
    return await forward_request("doctor", f"/api/doctors/{doctor_id}", "PUT", json=payload)


@app.delete("/gateway/doctors/{doctor_id}")
async def delete_doctor(doctor_id: int):
    return await forward_request("doctor", f"/api/doctors/{doctor_id}", "DELETE")


# Appointment routes
@app.get("/gateway/appointments")
async def get_all_appointments():
    return await forward_request("appointment", "/api/appointments", "GET")


@app.get("/gateway/appointments/{appointment_id}")
async def get_appointment(appointment_id: int):
    return await forward_request("appointment", f"/api/appointments/{appointment_id}", "GET")


@app.post("/gateway/appointments")
async def create_appointment(payload: dict = Body(...)):
    return await forward_request("appointment", "/api/appointments", "POST", json=payload)


@app.put("/gateway/appointments/{appointment_id}")
async def update_appointment(appointment_id: int, payload: dict = Body(...)):
    return await forward_request("appointment", f"/api/appointments/{appointment_id}", "PUT", json=payload)


@app.delete("/gateway/appointments/{appointment_id}")
async def delete_appointment(appointment_id: int):
    return await forward_request("appointment", f"/api/appointments/{appointment_id}", "DELETE")


# Feedback routes
@app.get("/gateway/feedbacks")
async def get_all_feedbacks():
    return await forward_request("feedback", "/api/feedbacks", "GET")


@app.get("/gateway/feedbacks/{feedback_id}")
async def get_feedback(feedback_id: int):
    return await forward_request("feedback", f"/api/feedbacks/{feedback_id}", "GET")


@app.post("/gateway/feedbacks")
async def create_feedback(payload: dict = Body(...)):
    return await forward_request("feedback", "/api/feedbacks", "POST", json=payload)


@app.put("/gateway/feedbacks/{feedback_id}")
async def update_feedback(feedback_id: int, payload: dict = Body(...)):
    return await forward_request("feedback", f"/api/feedbacks/{feedback_id}", "PUT", json=payload)


@app.delete("/gateway/feedbacks/{feedback_id}")
async def delete_feedback(feedback_id: int):
    return await forward_request("feedback", f"/api/feedbacks/{feedback_id}", "DELETE")