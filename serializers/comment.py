# serializers/comment.py

from pydantic import BaseModel

class CommentSchema(BaseModel):
  id: int
  content: str

  class Config:
    orm_mode = True

class CreateCommentSchema(BaseModel):
  content: str

  class Config:
    orm_mode = True

class UpdateCommentSchema(BaseModel):
  content: str

  class Config:
    orm_mode = True