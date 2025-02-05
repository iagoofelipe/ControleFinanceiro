# REG_TYPE_*
REG_TYPE_OUT = 0
REG_TYPE_IN = 1

# DB_COLS_TABLE_*
DB_COLS_TABLE_USER = ('id', 'username', 'password', 'first_name', 'last_name')
DB_COLS_TABLE_BANK = ('id', 'name', 'description', 'user_id')
DB_COLS_TABLE_CARD = ('id', 'num', 'dia_fechamento', 'dia_vencimento', 'limite', 'bank_id')
DB_COLS_TABLE_REGISTRY = ('id', 'type', 'title', 'value', 'datetime', 'description', 'user_id', 'bank_id', 'card_id')
