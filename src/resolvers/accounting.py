from sql_base import base_worker
from sql_base import models

def get_accounting(accounting_id: int):
    return base_worker.insert_data("SELECT id, eventid, income, costs, drugs  FROM accounting WHERE id =?",
                               (accounting_id,))
def new_accounting(accounting: models) -> int:
    new_id = base_worker.insert_data("INSERT INTO accounting (id, eventid, income, costs, drugs)"
                                 "VALUES (?, ?, ?, ?, ?)"
                                 "RETURNING id",
                                 (accounting.id, accounting.eventID, accounting.income, accounting.costs, accounting.drugs ))
    return new_id
def delete_accounting(accounting: int):
    return base_worker.execute(query="DELETE FROM accounting WHERE id=? ",
                              args=(accounting_id,))

