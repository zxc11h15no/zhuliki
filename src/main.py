from sql_base import check_base, create_base
from settings import BASE_PATH

if __name__ == '__main__':
    if not check_base(BASE_PATH):
        create_base(BASE_PATH,'../SQL/base.sql')