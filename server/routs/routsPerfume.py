from fastapi import APIRouter ,Depends , HTTPException
router = APIRouter()
from pydantic import BaseModel
from typing import Optional, List
from services.servicesPerfume import get_perfume_from_db,add_perfume
from sqlalchemy.orm import Session 
from dataBase import get_db 
from schemas.schemasPerfume import PerfumeSchema
from datetime import datetime
from models.perfumeModels import Perfume

@router.get("/")
async def get_perfumes_route(db:Session = Depends(get_db)):
    return await get_perfume_from_db(db)

@router.post("/")
async def add_entity(new_perfume:PerfumeSchema,db:Session =Depends(get_db)): 
    return await add_perfume(db,new_perfume)
    
@router.put("/delete/{perfume_id}")
async def soft_delete_perfume(perfume_id: int, db: Session = Depends(get_db)):
    perfume = db.query(Perfume).filter(Perfume.id == perfume_id).first()
    
    if not perfume:
        raise HTTPException(status_code=404, detail="perfume not found")
    
    if perfume.deleted:
        raise HTTPException(status_code=400, detail="perfume already deleted")
    
    perfume.deleted = True
    perfume.deleted_on = datetime.utcnow()
    db.commit()
    return {"message": "perfume deleted successfully"}


@router.put("/restore/{perfume_id}")
async def restore_perfume(perfume_id: int, db: Session = Depends(get_db)):
    perfume = db.query(Perfume).filter(Perfume.id == perfume_id).first()
    
    # Debugging log to check if perfume is found
    print(f"Found perfume: {perfume}")
    
    if not perfume:
        raise HTTPException(status_code=404, detail="perfume not found")
    
    if not perfume.deleted:
        # perfume is not deleted, so no restoration is necessary
        raise HTTPException(status_code=400, detail="perfume not deleted")
    
    perfume.deleted = False  # Restore the perfume
    perfume.deleted_on = None  # Optional: Remove deleted timestamp
    db.commit()
    
    # Debugging log to check restored perfume
    print(f"perfume restored: {perfume}")
    
    return {"message": f"perfume with id {perfume_id} restored successfully"}