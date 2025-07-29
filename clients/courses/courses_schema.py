from pydantic import BaseModel, Field, EmailStr, ConfigDict
from clients.files.files_client import File
from pydantic_create_user import UserSchema


# Добавили описание структуры курса
class CourseSchema(BaseModel):
    """
    Описание структуры курса.
    """
    id: str
    title: str
    maxScore: int
    minScore: int
    description: str
    previewFile: File  # Вложенная структура файла
    estimatedTime: str
    createdByUser: UserSchema  # Вложенная структура пользователя


class GetCoursesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка курсов.
    """
    userId: str


class CreateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание курса.
    """
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str
    previewFileId: str
    createdByUserId: str


# Добавили описание структуры запроса на создание курса
class CreateCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания курса.
    """
    course: CourseSchema


class UpdateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление курса.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    description: str | None
    estimatedTime: str | None