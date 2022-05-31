import itertools
import fastapi
from sqlalchemy.orm import session
from db.db_setup import getdb
from db.models.career import Interests

router = fastapi.APIRouter()


@router.get("/career")
async def get_career(db: session = fastapi.Depends(getdb)):
    return db.query(Interests).all()


def get_all_codes(code: str):
    all_codes = [char for char in itertools.product(list(code), repeat=3)]
    clean_codes = ["".join(code) for code in all_codes if len(set(code)) == 3]
    return clean_codes


@router.get("/career/{code},{area}")
async def get_career(code: str, area: int, db: session = fastapi.Depends(getdb)):
    generated_codes = get_all_codes(code)

    careers = [db.query(Interests).filter(Interests.interest_code == code).filter(Interests.job_zone == area).all()
               for code in generated_codes]

    return [career for career in careers if len(career) > 0]


