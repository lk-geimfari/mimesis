# Gretel Generated Client
from dotenv import load_dotenv
load_dotenv()


from gretel_client import configure_session

configure_session(api_key="grtu****", validate=True)

# If in a Notebook or similar environment you should see...

# Using endpoint https://api.gretel.cloud
# Logged in as user@domain.com ✅