from google_task_service import Create_Service
from convert_text_to_speech import text_to_wav



# Constants
CLIENT_SECRET_FILE = 'credentials.json'
API_NAME = 'tasks'
API_VERSION = 'v1'
SCOPES = ['https://www.googleapis.com/auth/tasks.readonly']

service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)
# Call the Tasks API
results = service.tasklists().list().execute()
items = results.get('items', [])
#print(service.tasklists().list().execute())

final_string =""
if not items:
    print('No task lists found.')
else:
    print('Task lists:')
    for item in items:
        #print(item)
        print(u'{0} ({1})'.format(item['title'], item['id']))
        responses = service.tasks().list(tasklist=u'{}'.format(item['id'])).execute()
        all_tasks = responses.get('items', [])
        for single_task in all_tasks:
            try:
                #print(u'{}'.format(single_task['notes']))
                final_string+=u'{}'.format(single_task['notes'])
            except:
                pass
            
text_to_wav("en-AU-Wavenet-A", final_string)          

