from .. import  models, database, schemas
from fastapi import Depends, APIRouter, Response, HTTPException, status
from sqlalchemy.orm import Session


def get_all(db):
    allvaccines = db.query(models.Vaccine).all()
    return allvaccines

def create_vaccine(request: schemas.Vaccine,db):
      # db: Session = Depends(get_db) convert session into pydantic thing
   new_vac = models.Vaccine(startTime= request.startTime, endTime = request.endTime) #vaccineId = request.vaccineId, 
   db.add(new_vac)
   db.commit()
   db.refresh(new_vac)
   return new_vac

def delete_vaccine(vaccineId:int, db: Session):
     # db.query(models.Vaccine).filter(models.Vaccine.vaccineId == vaccineId).delete(synchronize_session= False)
    # db.commit()
    # return 'done'

    delbyid = db.query(models.Vaccine).filter(models.Vaccine.vaccineId == vaccineId)

    if not delbyid.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Vaacine id  {vaccineId} not found")

    delbyid.delete(synchronize_session= False)
    db.commit()
    return 'done'

def update_vaccine(vaccineId:int, request: schemas.Vaccine, db:Session):
      #preparing the query 
    vacbyid = db.query(models.Vaccine).filter(models.Vaccine.vaccineId == vaccineId)
    # if there is id give me the first one 
    if not vacbyid.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Vaacine id  {vaccineId} not found")

    vacbyid.update(request.dict()) 
    # vacbyid.update({'startTime':request.startTime,'endTime' :request.endTime})
    db.commit()
    return 'updated'
    # First approach
    # db.query(models.Vaccine).filter(models.Vaccine.vaccineId == vaccineId).update({'startTime': 'start Time updated'})
    # db.commit()
    # return 'updated'
    #2nd app
    # print(schemas.Vaccine)
    # db.query(models.Vaccine).filter(models.Vaccine.vaccineId == vaccineId).update(request)
    # db.commit()
    # return 'updated'

def vaccine_byId(vaccineId:int,response, db:Session):
    vaccinesbyid = db.query(models.Vaccine).filter(models.Vaccine.vaccineId ==vaccineId).first()
    if not vaccinesbyid:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
         detail=f"user with the vaccineId {vaccineId} not available")
        # response.status_code =status.HTTP_404_NOT_FOUND
        # return {'detail' : f"user with the vaccineId{vaccineId} not found"}
    return vaccinesbyid