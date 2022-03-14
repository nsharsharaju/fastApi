from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import models

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request,db: Session):
    new_blog = models.Blog(title=request.title, body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(id:int, db: Session):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(id:int,request,db):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not found')
    blog.update(request,synchronize_session=False)
    db.commit()
    return 'done'

def show(id,db):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        return {'detail': f'Blog with the id {id} is not avaliable'}
    return blog
