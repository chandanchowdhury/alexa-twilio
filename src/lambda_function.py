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

def sendText(to_num, msg_text="Hey Wildcats! Good luck for the HACK-K-STATE! - i_virus", from_num=TWILIO_NUMBER):
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    client.messages.create(
        to=to_num,
        from_=from_num,
        body=msg_text
        )

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
        return build_response(session_attributes, build_speechlet_response("Twilio", bad_request_output, NONE, should_end_session))

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
    if intent_name == "twilioIntent":
        return twilioIntentHandler(intent)
    else:
        raise ValueError("Invalid intent")

# --------------- Functions that control the skill's behavior ------------------


def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to the Twilio. " \
                    "Please tell me the number and the message to send a text"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Please tell me the number and the message to send a text"

    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def twilioIntentHandler(intent):

    print(intent['slots'])

    slots = intent['slots']

    #for debug
    for slot in slots:
        print(slot)

    cellNumber = slots['numberSlot']['value']
    messageText = slots['msgSlot']['value']

    # call the method to send text
    sendText(to_num=cellNumber,msg_text=messageText)

    session_attributes = {}
    should_end_session = True

    speech_output = "Message sent"
    reprompt_text = None

    # Setting reprompt_text to None signifies that we do not want to reprompt
    # the user. If the user does not respond or says something that is not
    # understood, the session will end.
    return build_response(session_attributes, build_speechlet_response(
        "Twilio", speech_output, reprompt_text, should_end_session))

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
