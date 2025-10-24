from fastapi import APIRouter, HTTPException
from ..models.course import CourseIdResponse
from ..utilities.helpers import validate_and_normalize_course_id

router = APIRouter(tags=["courses"])

@router.get("/courses/{course_id}", response_model=CourseIdResponse, summary="Get course by ID")
def get_course_by_id(course_id: str) -> CourseIdResponse:
    """
    Returns ONLY the `course_id` in the response structure, as required.
    No other fields should be included.
    """
    try:
        normalized = validate_and_normalize_course_id(course_id)
        return CourseIdResponse(course_id=normalized)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
