import os
import dialogflow
json_path = os.path.dirname(os.path.abspath("dialogflowHandler.py"))+'/env/chatbot-292417-08259f9f0019.json'
json_path = json_path.replace('\\','/')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = json_path
project_id = "chatbot-292417"
session_id = "18021999"
language_code = "vi"
session_client = dialogflow.SessionsClient()
session = session_client.session_path(project_id, session_id)

def process(inputText):
    text_input = dialogflow.types.TextInput(text=inputText, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response_dialogflow = session_client.detect_intent(session=session, query_input=query_input)
    text = response_dialogflow.query_result.fulfillment_text
    return text