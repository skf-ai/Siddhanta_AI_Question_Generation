from pydantic import BaseModel, Field, ConfigDict

class CourseIdResponse(BaseModel):
    course_id: str = Field(..., description="Unique identifier of the course")

    model_config = ConfigDict(json_schema_extra={"example": {"course_id": "COURSE-123"}})
