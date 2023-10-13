from fastapi import APIRouter
from sql_base.models import accounting
import resolvers.accounting


accounting_router = APIRouter()

@accounting_router.get("/get")
def get_accounting():
    return f'Response:{{text:Страница учёта}}'

@accounting_router.post("/create")
def new_cafe(accounting: accounting,):
    new_id = resolvers.accounting.new_accounting(accounting)
    return f"{{code: 201, id: {new_id}}}"

@accounting_router.delete("/delete/{accounting_id}")
def delete_accounting(accounting_id: int):
    return f'delete accounting {accounting_id}'


