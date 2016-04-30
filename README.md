#Sample AWS Lambda function for Alexa
A simple [AWS Lambda](http://aws.amazon.com/lambda) function that demonstrates how to write a skill for the Amazon Echo using the Alexa SDK. It uses Twilio REST API and the python client to send

## Concepts
This sample shows how to create a Lambda function for handling Alexa Skill requests that:

- Multiple slots: has 2 slots (numberSlot and msgSlot)
- NUMBER slot: demonstrates how to handle number slots.
- LITERAL slot type: demonstrates using LITERAL slot types to handle a free-form text values

## Setup
To run this example skill you need to follow below setups. The first is to get a Twilio.com account and buy a number to be able to send text messages. Once that is done deploy the example code in lambda, and then configure the Alexa skill to use Lambda.

### Twilio Account and Number Setup
1. Register yourself in Twilio.com.
2. Buy a number.
3. Setup a Messaging Service under Programable SMS service using the number.
4. Once everything is ready note the ACCOUNT-SID and AUTH-TOKEN, we will use them in our python code running on Amazon Lambda.

### AWS Lambda Setup
1. Go to the AWS Console and click on the Lambda link. Note: ensure you are in us-east or you won't be able to use Alexa with Lambda.
2. Click on the Create a Lambda Function or Get Started Now button.
3. Skip the blueprint
4. Name the Lambda Function "twilioSendText" and a description like "Send text from Echo using Twilio.com".
5. Select the runtime as Python 2.7
6. Go to the the src directory, select all files in lib/python2.7/site-packages and then create a zip file, make sure the zip file does not contain the directory itself, otherwise Lambda function will not work.
7. Add the lambda_function.py to the file using below command in linux/osX
zip Archive.zip add lambda_function.py
8. Create a config.py file in the same location as the lambda_function.py and just add below variables with required data. Make sure to not expose this file to public on Github or somewhere else.
TWILIO_APPLICATION_ID=""
ACCOUNT_SID = ""
AUTH_TOKEN = ""
TWILIO_NUMBER = ""
9. Select Code entry type as "Upload a .ZIP file" and then upload the .zip file to the Lambda
10. Keep the Handler as lambda_function.lambda_handler (this refers to the lambda_handler method in lambda_function.py file in the zip).
12. Create a Basic execution role with default values.
13. Leave the Advanced settings as the defaults.
14. Click "Next" and review the settings then click "Create Function"
15. Click the "Event Sources" tab and select "Add event source"
16. Set the Event Source type as Alexa Skills kit and Enable it now. Click Submit.
17. Copy the ARN from the top right to be used later in the Alexa Skill Setup.

### Alexa Skill Setup
1. Go to the [Alexa Console](https://developer.amazon.com/edw/home.html) and click Add a New Skill.
2. Set "twilio" for the skill name and "twilio" as the invocation name, this is what is used to activate your skill. For example you would say: "Alexa, Ask twilio to send text to ... that ..."
3. Select the Lambda ARN for the skill Endpoint and paste the ARN copied from above. Click Next.
4. Copy the Intent Schema from the included twilioIntentSchema.json.
6. Copy the Sample Utterances from the included twilioSampleUtterance.txt. Click Next.
7. Go back to the skill Information tab and copy the appId. Paste the appId into the config.py file for the variable TWILIO_APPLICATION_ID,
   then update the lambda source zip file with this change and upload to lambda again, this step makes sure the lambda function only serves request from authorized source.
8. You are now able to start testing your sample skill! You should be able to go to the [Echo webpage](http://echo.amazon.com/#skills) and see your skill enabled.
9. In order to test it, try to say some of the Sample Utterances from the Examples section below.
10. Your skill is now saved and once you are finished testing you can continue to publish your skill.

## Examples

### One-shot model:
    User: "Alexa, tell twilio send text to seven eight five three one seven zero three six zero that it is working."
    Alexa: "Message sent"

### Dialog model: (In Progress)
    User: "Alexa, tell twilio draft a text to seven eight five three one seven zero three six zero that it is working."
    Alexa: "Message drafted. Do you want to send it?"
    User: Yes
    Alexa: "Message sent"
