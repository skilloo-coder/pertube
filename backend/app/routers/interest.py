from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..models.interest import Interest
from ..schemas.interest import InterestCreate, InterestResponse
from ..dependencies import get_db

router = APIRouter(prefix="/interests", tags=["Interests"])


@router.get("/", response_model=list[InterestResponse])
def get_interests(db: Session = Depends(get_db)):
    return db.query(Interest).all()


@router.post("/", response_model=InterestResponse)
def create_interest(data: InterestCreate, db: Session = Depends(get_db)):
    existing = db.query(Interest).filter(Interest.name == data.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Interest already exists")

    interest = Interest(name=data.name, description=data.description)
    db.add(interest)
    db.commit()
    db.refresh(interest)

    return interest
