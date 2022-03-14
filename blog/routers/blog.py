from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, database, models
from typing import List
from sqlalchemy.orm import Session
from ..repository import blog

router = APIRouter(
    prefix="/blog",
    tags=['blogs']
)

@router.get('/', response_model=List[schemas.showBlog])
def all(  db: Session = Depends(database.get_db)  ):
    return blog.get_all(db)

@router.post('/')
def create(request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.create(request,db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db: Session= Depends(database.get_db)):
   return blog.destroy(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.update(id,request,db)

@router.get('/{id}', status_code=status.HTTP_201_CREATED, response_model=schemas.showBlog)
def show(id:int,db: Session = Depends(database.get_db)):
    return blog.show(id,db)