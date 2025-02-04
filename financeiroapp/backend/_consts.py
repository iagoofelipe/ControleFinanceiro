__id = 0
def generateId():
    global __id
    __id += 1
    return __id

# Pages
PAGE_ID_LOADING = generateId()
PAGE_ID_HOME = generateId()
PAGE_ID_REG = generateId()

MAINWINDOW_PAGES = (PAGE_ID_HOME, PAGE_ID_REG)

# Table
TABLE_HEADER_TITLE = generateId()
TABLE_HEADER_EDIT = generateId()
TABLE_HEADER_CONFIRM = generateId()
TABLE_HEADER_DELETE = generateId()