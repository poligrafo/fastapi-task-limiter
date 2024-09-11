from pydantic import BaseModel


# The class name was changed from TestResponse to ResponseModel
# Reason: To avoid PytestCollectionWarning, as pytest was interpreting TestResponse as a test class
class ResponseModel(BaseModel):
    elapsed: float
