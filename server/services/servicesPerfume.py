
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



def update_perfume_data(
    perfume_id: int, 
    updated_perfume: PerfumeSchema, 
    db: Session
) -> Perfume:
    # Fetch the perfume by ID
    perfume = db.query(Perfume).filter(Perfume.id == perfume_id).first()

    # If perfume does not exist, raise 404 error
    if not perfume:
        raise HTTPException(status_code=404, detail="Perfume not found")

    # Update the perfume data with the new values
    perfume.name = updated_perfume.name
    perfume.brand = updated_perfume.brand
    perfume.fragrance_notes = updated_perfume.fragrance_notes
    perfume.price = updated_perfume.price
    perfume.volume = updated_perfume.volume
    perfume.image_url = updated_perfume.image_url
    perfume.buy_url = updated_perfume.buy_url

    # Update scentId as an array (even if it's a single scentId)
    print("scent id from backend",updated_perfume.scentId)
    if updated_perfume.scentId:
        perfume.scentId = [int(updated_perfume.scentId)]  # Convert to integer and wrap in an array

    # Commit the changes to the database
    db.commit()

    # Refresh the instance to reflect the updated data
    db.refresh(perfume)

    return perfume





# Function to fetch a single perfume by id
def get_perfume_by_id(db: Session, perfume_id: int):
    perfume = db.query(Perfume).filter(Perfume.id == perfume_id).first()
    if not perfume:
        return None
    return perfume
