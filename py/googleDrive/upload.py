
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
import auth

def upload_basic():
   
    SCOPES = 'https://www.googleapis.com/auth/drive'
    # your google drive API OAuth
    CLIENT_SECRET_FILE = 'client_secret.json'
    APPLICATION_NAME = 'Drive API'
    authInst = auth.auth(SCOPES,CLIENT_SECRET_FILE,APPLICATION_NAME)
    creds = authInst.getCredentials()

    try:
        # create drive api client
        service = build('drive', 'v3', credentials=creds)

        # save file name
        # folder
        file_metadata = {'name': 'googledd.jpg',
                         'parents': ['1alAFW3FNHh2NY1fFFMLNHIWg5P83ubdh']}
        # local file name and type
        media = MediaFileUpload('google.jpg',
                                mimetype='image/jpeg')
        # pylint: disable=maybe-no-member
        file = service.files().create(body=file_metadata, media_body=media,
                                      fields='id').execute()
        print(F'File ID: {file.get("id")}')

    except HttpError as error:
        print(F'An error occurred: {error}')
        file = None

    return file.get('id')


if __name__ == '__main__':
    upload_basic()