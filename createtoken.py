import datetime
from datetime import timedelta

import pytz
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

service_account_email = "yudizchatbot@yudizbot-abfjvm.iam.gserviceaccount.com"
SCOPES = ["https://www.googleapis.com/auth/calendar"]
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    filename="yudizbot-abfjvm-cf29736bf66c.json", scopes=SCOPES
)