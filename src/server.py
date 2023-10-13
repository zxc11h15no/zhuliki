from fastapi import FastAPI
from sql_base import base_worker
from settings import BASE_PATH
from routers.accounting import accounting_router
from routers.drugs import drugs_router
from routers.users import user_router


base_worker.set_base_path(BASE_PATH)

if not base_worker.check_base():
    base_worker.create_base('../sql/base.sql')

app = FastAPI()


app.include_router(accounting_router, prefix='/accounting')
app.include_router(drugs_router, prefix='/drugs')
app.include_router(user_router, prefix='/users')

