from sql_base import base_worker
from sql_base import models

def get_drugs(drugs_id: int):
    return base_worker.insert_data("SELECT id, quantity, for_sale, for_personal_use  FROM drugs WHERE id =?",
                               (drugs_id,))

def new_drugs(drugs: models) -> int:
    new_id = base_worker.insert_data("INSERT INTO drugs (id, quantity, for_sale, for_personal_use)"
                                 "VALUES (?, ?, ?, ?)"
                                 "RETURNING id",
                                 (drugs.id, drugs.quantity, drugs.for_sale, drugs.for_personal_use))
    return new_id

def delete_drugs(drugs_id: int):
    return base_worker.execute(query="DELETE FROM drugs WHERE id=? ",
                              args=(drugs_id,))