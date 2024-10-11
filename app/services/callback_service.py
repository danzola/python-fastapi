import time
import requests
from app.models.callback_model import CallbackRequest,EmailTemplate,ResponseData

def invoke_callback(request: CallbackRequest, status_code: int):
    time.sleep(5)
    try:
        final_compound = EmailTemplate(tenant=request.tenant)
        response_data = ResponseData(
            tenant=request.tenant,
            mensaje="Message: Element not found:id-btnActualizar_input - Clickable\n",
            status_code=status_code,
            final_compound=final_compound
            )

        json_data = response_data.model_dump_json()
        print(f"{json_data}")
        response = requests.post(request.url_callback,json=json_data)
        response.raise_for_status()

        print(f"Callback invoked, status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error invoking callback: {e}")