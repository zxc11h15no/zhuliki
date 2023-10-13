from fastapi import APIRouter
from sql_base.models import drugs
import resolvers.drugs


drugs_router = APIRouter()

@drugs_router.get("/get")
def get_drugs():
    return f'Response:{{text:Страница с информацией о drugs}}'

@drugs_router.post("/create")
def new_drugs(drugs: drugs,):
    new_id = resolvers.drugs.new_drugs(drugs)
    return f"{{code: 201, id: {new_id}}}"

@drugs_router.delete("/delete/{drugs_id}")
def delete_drugs(drugs_id: int):
    return f'delete drugs {drugs_id}'
