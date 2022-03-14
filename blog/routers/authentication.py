from fastapi import APIRouter, HTTPException, status, Depends
from .. import schemas, database, models
from sqlalchemy.orm import Session
from ..hashing import Hash
# from token import create_access_token

router = APIRouter(
    tags=['authentication']
)

@router.post('/login')
def login(request: schemas.Login, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Invalid Credentials"
            )
    if not Hash.verify(user.password,request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Invalid Password"
            )
    #generate jwt-token and return it
    # access_token = create_access_token(
    #     data={"sub": user.username}
    # )
    return "done"