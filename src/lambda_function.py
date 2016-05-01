"""
This sample demonstrates a simple skill built with the Amazon Alexa Skills Kit.
The Intent Schema, Built-in Slots, and Sample Utterances for this skill, as well
as testing instructions are located at http://amzn.to/1LzFrj6

For additional samples, visit the Alexa Skills Kit Getting Started guide at
http://amzn.to/1LGWsLG

Author: i_virus
Date: 2016-04-30
"""

from __future__ import print_function
from twilio.rest import TwilioRestClient
from config import *
import wikipedia


def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    session_attributes = {}

    applicationId = event['session']['application']['applicationId']
    if applicationId != TWILIO_APPLICATION_ID:
        should_end_session = True
        bad_request_output = "Bad Request"
        print("Bad ApplicationId Received: "+applicationId)
        return build_response(session_attributes, build_speechlet_response("Twilio", bad_request_output, None, should_end_session))

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'])

def on_launch(launch_request):
    """ Called when the user launches the skill without specifying what they
    want
    """
    print("on_launch requestId=" + launch_request['requestId'])

    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request):
    """ Called when the user specifies an intent for this skill """
    print("on_intent requestId=" + intent_request['requestId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "kstateIntent":
        return kstateIntentHandler(intent)

    elif intent_name == "wildcatIntent":
        return wildcatIntentHandler(intent)

    elif intent_name == "willieIntent":
        return willieIntentHandler(intent)

    elif intent_name == "haleIntent":
        return haleIntentHandler(intent)

    elif intent_name == "neilsenIntent":
        return neilsenIntentHandler(intent)

    elif intent_name == "andresenIntent":
        return andresenIntentHandler(intent)

    elif intent_name == "feldhausenIntent":
        return feldhausenIntentHandler(intent)

    elif intent_name == "eyvIntent":
        return eyvIntentHandler(intent)

    elif intent_name == "twilioIntent":
        return twilioIntentHandler(intent)

    elif intent_name == "helpIntent":
        return helpIntentHandler(intent)

    elif intent_name == "unknownIntent":
        return unknownIntentHandler(intent)

    elif intent_name == "quitIntent":
        return quitIntentHandler(intent)

    else:
        return misunderstoodHandler(intent)
        #raise ValueError("Invalid intent")

# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    session_attributes = {}
    card_title = "Welcome"

    speech_output = "Hey Wildcats... welcome to Hack K-State.  " \
                    "Don't freak out by my voice... I am Willie... Tell me what can I do for ya?"

    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "too much noise... could ya repeat that for me buddy?"

    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def kstateIntentHandler(intent):
    card_title = "K-State"

    speech_output = "K-State is the place for hackers "

    return build_response(None, build_speechlet_response(
        card_title, speech_output, None, False))

def wildcatIntentHandler(intent):
    card_title = "Wildcat"

    print(intent['slots'])

    slots = intent['slots']

    speech_output = "Once a Wildcat...  wildcat forever"

    return build_response(None, build_speechlet_response(
        card_title, speech_output, None, False))

def willieIntentHandler(intent):
    card_title = "Willie"

    speech_output = "I am Willie the Wildcat... GO CATS"

    return build_response(None, build_speechlet_response(
        card_title, speech_output, None, False))

def haleIntentHandler(intent):
    card_title = "Hale Library"

    speech_output = "Where ALL hackers meet secretly and share their knowledge to gain more knowledge"

    return build_response(None, build_speechlet_response(
        card_title, speech_output, None, False))

def neilsenIntentHandler(intent):
    card_title = "Dr Mitch Nielsen"

    speech_output = "He is a true hacker"

    return build_response(None, build_speechlet_response(
        card_title, speech_output, None, False))

def andresenIntentHandler(intent):
    card_title = "Dr Daniel Andresen"

    speech_output = "He hacked the Beocat out of nothing.. you can find him in E Two One Seven Eight or reach out to him at dan@cis.ksu.edu"

    return build_response(None, build_speechlet_response(
        card_title, speech_output, None, False))

def feldhausenIntentHandler(intent):
    card_title = "Russell Feldhausen"

    speech_output = "He helps other hackers... lot of them.  You can reach him  russfeld @ ksu DOT edu "

    return build_response(None, build_speechlet_response(
        card_title, speech_output, None, False))

def eyvIntentHandler(intent):
    card_title = "Eugene Vasserman"

    speech_output = "He is hackproof...  Thats all I know about him"

    return build_response(None, build_speechlet_response(
        card_title, speech_output, None, False))

def kevindiceIntentHandler(intent):
    card_title = "Kevin Dice"

    speech_output = "How do you think you are able to hack today"

    return build_response(None, build_speechlet_response(
        card_title, speech_output, None, False))

def asleycolemanIntentHandler(intent):
    card_title = "Asley Coleman"

    speech_output = "Hacker"

    return build_response(None, build_speechlet_response(
        card_title, speech_output, None, False))

def atoddIntentHandler(intent):
    card_title = "Alex Todd"

    speech_output = "Big time Hacker"

    return build_response(None, build_speechlet_response(
        card_title, speech_output, None, False))

def allanjayIntentHandler(intent):
    card_title = "A J Cabanatuan"

    speech_output = "He is bored so he is not hacking this time"

    return build_response(None, build_speechlet_response(
        card_title, speech_output, None, False))

def chrispIntentHandler(intent):
    card_title = "CHris Piggott"

    speech_output = "He is doing CASUAL hacking"

    return build_response(None, build_speechlet_response(
        card_title, speech_output, None, False))

def beocatIntentHandler(intent):
    card_title = "Beocat"

    speech_output = "A tiny hacking machine for BIG hackers"

    return build_response(None, build_speechlet_response(
        card_title, speech_output, None, False))


def lambdaisloveIntentHandler(intent):
    card_title = "Jake Elrich"

    speech_output = "You mean the RUSTY hacker"

    return build_response(None, build_speechlet_response(
        card_title, speech_output, None, False))

def twilioIntentHandler(intent):
    card_title = "Twilio"
    print(intent['slots'])

    try:
        cellNumber = ""
        messageText = ""

        slots = intent['slots']

        cellNumber = slots['numberSlot']['value']

        messageText = slots['msgSlot']['value']

        # call the method to send text
        if(sendText(to_num=cellNumber,msg_text=messageText)):
            #success
            speech_output = "Message sent"
        else:
            #failure
            speech_output = "Sorry could not sent the message  and Don't worry I will ask the idiots to fix the issue"
    except Exception:
        speech_output = "too much noise.... Sorry didn't get the details... please try again"

    # Setting reprompt_text to None signifies that we do not want to reprompt
    # the user. If the user does not respond or says something that is not
    # understood, the session will end.
    return build_response(None, build_speechlet_response(
        card_title, speech_output, None, False))

def sendText(to_num, msg_text="Hey Wildcats! Good luck for the HACK-K-STATE! - i_virus", from_num=TWILIO_NUMBER):
    try:
        client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
        client.messages.create(
            to=to_num,
            from_=from_num,
            body=msg_text
            )
        return True
    except Exception as e:
        print("Failed to send message: ")
        print(e.code)
        print("Message: ")
        print(e.msg)
        return False


def helpIntentHandler(intent):
    card_title = "Help"

    speech_output = "You can ask me about K-State or I can send a text to a phone number for you, thanks to Twilio dot com."
    speech_output += " OR I can tell you some secret about Judge Russ..."

    return build_response(None, build_speechlet_response(
        card_title, speech_output, None, False))

def unknownIntentHandler(intent):
    card_title = "Unknown"

    print(intent['slots'])

    slots = intent['slots']

    try:
        result = wikipedia.summary(slots['unknownSlot']['value'],sentences=1)

        speech_output = "All I know from Wikipedia is " + result
    except Exception as e:
        print(e)
        speech_output = "Oops something went wrong.  Don't worry I have asked the idiots to fix the issue"

    return build_response(None, build_speechlet_response(
        card_title, speech_output, None, False))

def misunderstoodHandler(intent):
    card_title = "Misunderstood"

    speech_output = "Sorry didn't get that... please try again"

    return build_response(None, build_speechlet_response(
        card_title, speech_output, None, True))

def quitIntentHandler(intent):
    card_title = "Bye"

    speech_output = "man... what an awesome people you guys are... keep it up... am not going anywhere... just call me if ya need somehthing"

    return build_response(None, build_speechlet_response(
        card_title, speech_output, None, True))

# --------------- Helpers that build all of the responses ----------------------


def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': 'SessionSpeechlet - ' + title,
            'content': 'SessionSpeechlet - ' + output
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
