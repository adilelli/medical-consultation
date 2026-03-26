from fastapi import HTTPException

class UnauthorizedError(HTTPException):
    def __init__(self, detail: str = "Invalid credentials"):
        super().__init__(status_code=401, detail=detail)

class ForbiddenError(HTTPException):
    def __init__(self, detail: str = "Not allowed to login"):
        super().__init__(status_code=403, detail=detail)

class UnprocessableEntityError(HTTPException):
    def __init__(self, detail: str = "Unprocessable entity"):
        super().__init__(status_code=422, detail=detail)

class NotFoundError(HTTPException):
    def __init__(self, detail: str = "Resource not found"):
        super().__init__(status_code=404, detail=detail)

class ConflictError(HTTPException):
    def __init__(self, detail: str = "Conflict"):
        super().__init__(status_code=409, detail=detail)
    
class BusinessLogicError(HTTPException):
    def __init__(self, detail: str = "Business logic error"):
        super().__init__(status_code=400, detail=detail)