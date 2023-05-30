import os
import requests
import json

web_hook_url = 'https://hooks.slack.com/services/WEBHOOK_KEY'

target_message = input("Message: ")

slack_msg = {
	"blocks": [
		{
			"type": "header",
			"text": {
				"type": "plain_text",
				"text": target_message,
				"emoji": true
			}
		}
	]
}

requests.post(web_hook_url, data=json.dumps(slack_msg))