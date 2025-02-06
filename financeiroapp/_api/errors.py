class ApiConnectionError(Exception):
    """ erro de conexão com a base de dados """

class ApiValueFoundError(Exception):
    """ valores encontrados na base de dados """

class ApiValueNotFoundError(Exception):
    """ valores não encontrados na base de dados """

class ApiUserNotAuthenticatedError(Exception):
    """ usuário não autenticado """

class ApiUserNotAuthorizedError(Exception):
    """ usuário não autorizado """

class ApiParamValidationError(Exception):
    """ parâmetros inválidos """