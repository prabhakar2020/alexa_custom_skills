import json

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }
    
def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }
    
def handle_session_end_request(intent, session):
    card_title = "Session Ended"
    speech_output = "Thank you for Talking with me. " \
                    "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))
        
def get_fallback_msg(intent, session):
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """
    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Fallback function called"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "I don't know if you heard me, welcome to your custom alexa application!"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_welcome_msg(intent, session):
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """
    session_attributes = {}
    card_title = "Welcome"
    speech_output = "This is welcome intent"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "I don't know if you heard me, welcome to your custom alexa application!"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
def get_saybye_response(intent, session):
    """ An example of a custom intent. Same structure as welcome message, just make sure to add this intent
    in your alexa skill in order for it to work.
    """
    session_attributes = {}
    card_title = "SayBye"
    responses = ["You're welcome", "It's my pleasure to serve you", "I am happy to work with you", "Nice talking with you"]
    import random
    speech_output = responses[random.randint(0,len(responses)-1)]
    reprompt_text = "It's my pleasure to serve you"
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
    # return build_response({}, build_speechlet_response(
    #     card_title, speech_output, None, should_end_session))
        
def get_architecture_msg(intent, session):
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """
    session_attributes = {}
    card_title = "Search"
    speech_output = "Hello all, My team has designed. and trained me. for automatic workflow to simplify. Top management queries. I will help you on this. Let me walk you through my architecture here. \
    Team has designed. to use alexa advanced custom skills. \
    Also I am using Lambda functions. to process user free flow conversation. \
    I am using EC2 web server. for hosting the web API. for handling advanced queries using. machine learning.\
    I am also using S3 storage. for maintaining business data, user context and logs. Let me walk you through the demo." 
    
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "I don't know if you heard me, welcome to your custom alexa application!"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def fetch_data_from_heroku_api(search_query):
    # from urllib.request import urlopen
    # link = "http://prabhakar.pythonanywhere.com/alexa/"+search_query
    try:
        # import urllib.request
        link = "https://alexa-web-robot.herokuapp.com/alexa/"+search_query
        # request = urllib.request.Request(link)
        # res = urllib.request.urlopen(request)
        # return res.read()
        
        
        # f = urlopen(link)
        # myfile = f.read()
        # return myfile.decode("utf-8")
        from urllib.request import urlopen
        response = urlopen(link)
        html = response.read()
        return html
    except Exception as err:
        print ("########## ERROR ")
        print (err)
        return "error"


def fetch_data_from_api(search_query):
    from urllib.request import urlopen
    link = "http://prabhakar.pythonanywhere.com/alexa/"+search_query
    try:
        f = urlopen(link)
        myfile = f.read()
        return myfile.decode("utf-8")
    except Exception as err:
        print ("########## ERROR ")
        print (err)
        return "error"
    
def get_search_msg(intent, session):
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """
    session_attributes = {}
    card_title = "Search"
    search_query = intent['slots']["search_key"]["value"]
    api_response = fetch_data_from_api(search_query)
    speech_output = "Search intent here " + api_response
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "I don't know if you heard me, welcome to your custom alexa application!"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
