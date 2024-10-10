import time
import requests
from app.models.callback_model import CallbackRequest,EmailTemplate,ResponseData

def invoke_callback(request: CallbackRequest):
    time.sleep(10)
    try:
        final_compound = EmailTemplate(tenant=request.tenant)
        response_data = ResponseData(
            tenant=request.tenant,
            mensaje="Method executed successfully.",
            status_code=200,
            final_compound=final_compound
            )

        json_data = response_data.model_dump_json()
        print(f"{json_data}")
        response = requests.post(request.callback_url,json=json_data)
        response.raise_for_status()

        print(f"Callback invoked, status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error invoking callback: {e}")