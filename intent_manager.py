import json
import custom_handlers

def get_custom_intents():
    intents_object = [
        ("welcome_intent", custom_handlers.get_welcome_msg),
        ("search_intent", custom_handlers.get_search_msg),
        ("architecture", custom_handlers.get_architecture_msg),
        ("saybye", custom_handlers.get_saybye_response)
        # ("AMAZON.HelpIntent", custom_handlers.get_welcome_msg),
        # ("AMAZON.CancelIntent", )
    ]
    return intents_object

        
def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']
    # intents_object = get_custom_intents()
    print ("************")
    print (intent_request)
    # fall_back = True
    # final_function = ''
    # for temp_intent in intents_object:
    #     if temp_intent == intent_name:
    #         fall_back = False
    #         final_function = temp_intent[1]
    #         break
    # if(fall_back):
    #     return custom_handlers.get_fallback_msg()
    # else:
    #     return final_function(intent, session)
        
    # Dispatch to your skill's intent handlers
    if intent_name == "welcome_intent":
        return custom_handlers.get_welcome_msg(intent, session)
    elif intent_name == "search_intent":
        return custom_handlers.get_search_msg(intent, session)
    elif intent_name == "architecture":
        return custom_handlers.get_architecture_msg(intent, session)
    elif intent_name == "saybye":
        return custom_handlers.get_saybye_response(intent, session)
    elif intent_name == "myname":
        return custom_handlers.get_myname_response(intent, session)
    elif intent_name == "ask":
        return custom_handlers.get_ask_response(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return custom_handlers.get_welcome_response(intent, session)
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return custom_handlers.handle_session_end_request(intent, session)
    else:
        return custom_handlers.get_fallback_msg(intent, session)