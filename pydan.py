from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str
student = User(
        id=1,
        name="Jie",        email="john.doe@example.com"
    )
print(student)