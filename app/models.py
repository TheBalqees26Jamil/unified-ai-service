# هنا يمكن تعريف أي موديلات لاحقًا باستخدام Pydantic
from pydantic import BaseModel

class ExampleModel(BaseModel):
    name: str
    age: int
