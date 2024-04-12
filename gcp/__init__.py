from gcp_auth import authenticate_implicit_with_adc
from gcp_upload import upload_blob

def main():
    authenticate_implicit_with_adc(project_id=os.getenv("GCP_PROJECT_ID"))
    upload_blob()

if __name__ == "__main__":
    main()

