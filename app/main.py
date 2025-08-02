import logging
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.models import Base, Patient
from datetime import datetime

app = FastAPI()
templates = Jinja2Templates(directory="templates")
Base.metadata.create_all(bind=engine)


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request, keyword: str = ""):
    db: Session = SessionLocal()
    if keyword:
        patients = db.query(Patient).filter(
            Patient.name.contains(keyword)).all()
    else:
        patients = db.query(Patient).all()
    return templates.TemplateResponse("home.html", {"request": request, "patients": patients, "keyword": keyword})


@app.post("/add")
def add_patient(
    name: str = Form(...),
    gender: str = Form(...),
    birth_date: str = Form(...),
    phone: str = Form(...),
    address: str = Form(...),
    day_in: str = Form(...),
    hos_fee: int = Form(...)
):
    db: Session = SessionLocal()
    new_patient = Patient(
        name=name,
        gender=gender,
        birth_date=datetime.strptime(birth_date, "%Y-%m-%d").date(),
        phone=phone,
        address=address,
        day_in=datetime.strptime(day_in, "%Y-%m-%d").date(),
        hos_fee=hos_fee
    )
    db.add(new_patient)
    db.commit()
    return RedirectResponse("/", status_code=303)


# Trang sửa bệnh nhân
@app.get("/edit/{patient_id}", response_class=HTMLResponse)
def edit_patient(request: Request, patient_id: int):
    db: Session = SessionLocal()
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if not patient:
        return RedirectResponse("/", status_code=302)
    return templates.TemplateResponse("edit.html", {"request": request, "patient": patient})


# Xử lý cập nhật
@app.post("/edit/{patient_id}")
def update_patient(
    patient_id: int,
    name: str = Form(...),
    gender: str = Form(...),
    birth_date: str = Form(...),
    phone: str = Form(...),
    address: str = Form(...),
    day_in: str = Form(...),
    hos_fee: int = Form(...)
):
    db: Session = SessionLocal()
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if patient:
        patient.name = name
        patient.gender = gender
        patient.birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()
        patient.phone = phone
        patient.address = address
        patient.day_in = datetime.strptime(day_in, "%Y-%m-%d").date()
        patient.hos_fee = hos_fee
        db.commit()
    return RedirectResponse("/", status_code=303)


# Xử lý xoá
@app.post("/delete/{patient_id}")
def delete_patient(patient_id: int):
    db: Session = SessionLocal()
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if patient:
        db.delete(patient)
        db.commit()
    return RedirectResponse("/", status_code=303)


logging.basicConfig(level=logging.INFO)
logging.info("Truy cập tại: http://localhost:8000")
