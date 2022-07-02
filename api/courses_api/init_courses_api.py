import fastapi
from sqlalchemy.orm import session
from db.db_setup import getdb
from db.models.courses import Courses
from db.models.career import Interests

router = fastapi.APIRouter(
    tags=['Courses']
)


@router.get("/Courses/{career}")
async def get_init_courses(career: str, db: session = fastapi.Depends(getdb), skip: int = 0, limit: int = 100):
    cluster = db.query(Interests).filter(Interests.title == career).first().sector
    courses = db.query(Courses).filter(Courses.field == cluster).offset(skip).limit(limit).all()
    return courses
