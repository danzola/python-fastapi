from typing import Optional
from pydantic import BaseModel, Field

class CallbackRequest(BaseModel):
    url_callback: str
    tenant: str

class EmailTemplate(BaseModel):
    tenant: Optional[str] = None

class ResponseData(BaseModel):
    tenant: str = Field(..., description="Tenant identifier")
    mensaje: str = Field(..., description="Message describing the operation result")
    status_code: int = Field(..., description="HTTP status code")
    final_compound: Optional[EmailTemplate] = None