from datetime import date as __date

__id = 0
def generateId():
    global __id
    __id += 1
    return __id

# Ui Pages
PAGE_ID_LOADING = generateId()
PAGE_ID_LOGIN = generateId()
PAGE_ID_HOME = generateId()
PAGE_ID_REG = generateId()

WINDOW_PAGES = (PAGE_ID_HOME, PAGE_ID_REG)
WINDOW_TITLE = 'Controle Financeiro'

# General
CRYPTO_KEY = "42333823303233455347532322493093"
CONFIG_FILE = 'config.ini'
CURRENT_DATE = __date.today()

# Ui Components - Table
TABLE_HEADER_TITLE = generateId()
TABLE_HEADER_EDIT = generateId()
TABLE_HEADER_CONFIRM = generateId()
TABLE_HEADER_DELETE = generateId()

# Database
DATABASE_HOST = 'localhost'
DATABASE_USER = 'test'
DATABASE_PASSWORD = '1234'
DATABASE_SCHEMA = 'financeiro'
DATABASE_PARAMS = {
    'host': DATABASE_HOST,
    'user': DATABASE_USER,
    'password': DATABASE_PASSWORD,
    'database': DATABASE_SCHEMA,
}