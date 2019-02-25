from __future__ import print_function
import json
import custom_handlers
import intent_manager

def lambda_handler(event, context):
    # TODO implement
    # return {
    #     'statusCode': 200,
    #     'body': json.dumps('Hello from Lambda!')
    # }
    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to your custom alexa application!"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "I don't know if you heard me, welcome to your custom alexa application!"
    should_end_session = False
    print (">>")
    print (event['request'].get('intent', '== Blank =='))
    print ("++")
    if event['request']['type'] == "LaunchRequest":
        speech_output = "Hey Prabhakar, welcome to alexa world. How can I help you today?"
    elif event['request']['type'] == "IntentRequest":
        return intent_manager.on_intent(event['request'], event['session'])
    return custom_handlers.build_response(session_attributes, custom_handlers.build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
    # return {
    #     'version': '1.0',
    #     'sessionAttributes': session_attributes,
    #     'response': speechlet_response
    # }
