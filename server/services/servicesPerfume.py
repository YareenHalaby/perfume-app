
from sqlalchemy.orm import Session 
from models.perfumeModels import Perfume
from schemas.schemasPerfume import PerfumeSchema
from sqlalchemy import DateTime
from sqlalchemy import desc

async def get_perfume_from_db(db: Session):
    return db.query(Perfume).filter(Perfume.deleted == False).order_by(Perfume.id.asc()).all()


async def add_perfume(db:Session,perfume:PerfumeSchema):
    db_perfume =Perfume(
        name = perfume.name,
        scentIds=perfume.scentIds,
        brand=perfume.brand,
        fragrance_notes=perfume.fragrance_notes,
        price=perfume.price,
        volume=perfume.volume,
        image_url=perfume.image_url,
        buy_url=perfume.buy_url,
    )
    db.add(db_perfume)
    db.commit()
    db.refresh(db_perfume)
    return db_perfume
    
async def deleted_perfumes(db: Session, perfume_id: int):
    # חיפוש הבושם שצריך להיות מסומן כמחוק
    perfume_item = db.query(Perfume).filter(Perfume.id == perfume_id, Perfume.deleted == False).first()  # שינוי

    if not perfume_item:
        return None  # אם לא נמצא או כבר נמחק, מחזירים None

    # סימון הבושם כמחוק
    perfume_item.deleted = True  # שינוי
    perfume_item.deleted_on = datetime.utcnow()  # שינוי

    db.commit()  # שמירה בבסיס הנתונים
    db.refresh(perfume_item)  # רענון הנתונים של הבושם
    return perfume_item  # החזרת הבושם עם השדות המעודכנים