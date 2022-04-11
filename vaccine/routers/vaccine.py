from fastapi import Depends, APIRouter, Response, HTTPException, status
from sqlalchemy.orm import Session
from .. import  models, database, schemas

from ..repository import vaccine

router = APIRouter(

    prefix="/devsecops",
    tags =['vaccine']
)

get_db = database.get_db

@router.post('/vaccine' , status_code=status.HTTP_201_CREATED)
def create(request: schemas.Vaccine, db: Session = Depends(get_db)): 
   return vaccine.create_vaccine(request, db)


@router.delete('/vaccine/{vaccineId}', status_code= status.HTTP_204_NO_CONTENT)
def deletevaccine(vaccineId, db: Session = Depends(get_db)):
    return vaccine.delete_vaccine(vaccineId,db)
   

@router.put('/vaccine/{vaccineId}', status_code= status.HTTP_202_ACCEPTED)
def update(vaccineId, request: schemas.Vaccine, db: Session = Depends(get_db)):
  return vaccine.update_vaccine(vaccineId,request,db)

@router.get('/vaccine' )
def all(db: Session = Depends(get_db)):
    return vaccine.get_all(db)


@router.get('/vaccine/{vaccineId}', status_code= 200)
def show(vaccineId, response: Response, db: Session = Depends(get_db)):
    return vaccine.vaccine_byId(vaccineId, response, db)
    