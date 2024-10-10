from fastapi import APIRouter,BackgroundTasks
from app.models.callback_model import CallbackRequest
from app.services.callback_service import invoke_callback

router = APIRouter(
    prefix="/process",
    tags=["process"],
)

@router.post("/")
async def process(
    request: CallbackRequest, 
    background_tasks: BackgroundTasks):
    print(f"Tenant: {request.tenant}")
    background_tasks.add_task(invoke_callback, request)
    return {"message": "Callback will be invoked after n minutes"}