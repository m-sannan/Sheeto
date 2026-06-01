import os
import sys
import webbrowser
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = ['https://www.googleapis.com/auth/drive.file']

# --- CONFIGURATION ---
PRIMARY_EMAIL = "your.email@gmail.com" 
# ---------------------

def get_resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def authenticate_google_drive():
    creds = None
    # Use a user-specific folder for the token so it doesn't crash in Read-Only App folders
    token_path = os.path.expanduser('~/.quicksheets_token.json')
    credentials_path = get_resource_path('credentials.json')

    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(token_path, 'w') as token:
            token.write(creds.to_json())
    try:
        return build('drive', 'v3', credentials=creds)
    except Exception as error:
        print(f"Authentication error: {error}")
        return None

def upload_and_convert(service, file_path):
    if not os.path.exists(file_path):
        return None

    filename = os.path.basename(file_path)
    file_metadata = {
        'name': filename,
        'mimeType': 'application/vnd.google-apps.spreadsheet'
    }
    media = MediaFileUpload(
        file_path, 
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        resumable=True
    )

    try:
        file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        sheet_id = file.get('id')
        return f"https://docs.google.com/spreadsheets/d/{sheet_id}/edit?authuser={PRIMARY_EMAIL}"
    except Exception:
        return None

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(1)
        
    target_file = sys.argv[1]
    drive_service = authenticate_google_drive()
    
    if drive_service:
        sheet_url = upload_and_convert(drive_service, target_file)
        if sheet_url:
            webbrowser.open(sheet_url)