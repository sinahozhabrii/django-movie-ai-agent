from permit import Permit
from decouple import config
def get_permit_client():
    token= config('PERMIT_API_KEY',default='')
    pdp_url = config("PDP_URL",default="https://cloudpdp.api.permit.io")
    permit = Permit(
        pdp=pdp_url,  
        token=token,
    )
    return permit



permit = get_permit_client()