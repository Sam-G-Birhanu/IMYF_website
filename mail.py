# from flask import Flask, request, jsonify
# import requests  # Used for making requests to Mailchimp API
# from mailchimp3 import MailChimp  # Mailchimp API library
# import os

# app = Flask(__name__)

# # Replace with your Mailchimp API key
# MAILCHIMP_API_KEY = ''
# MAILCHIMP_LIST_ID = ''  # Replace with your Mailchimp list ID

# @app.route('/', methods=['GET'])
# def subscribe():
# #   data = request.get_json()
#   email = ""

#   if not email:
#     return jsonify({'error': 'Missing email address'}), 400

#   # Mailchimp API integration
#   try:
#     client = MailChimp(MAILCHIMP_API_KEY)
#     member_data = {
#       'email_address': email,
#       'status': 'subscribed'  # Set member status to 'subscribed'
#     }
#     response = client.lists.add_list_member(MAILCHIMP_LIST_ID, member_data)

#     if response['status'] == 'subscribed':
#       return jsonify({'success': 'Subscription successful!'})
#     else:
#       return jsonify({'error': f'Mailchimp error: {response}'}), 500
#   except Exception as e:
#     return jsonify({'error': f'Internal error: {str(e)}'}), 500

# if __name__ == '__main__':
#   app.run(debug=True)

import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError

try:
  client = MailchimpMarketing.Client()
  client.set_config({
    "api_key": "",
    "server": ""
  })

  response = client.lists.add_list_member("630f4b0d2d", {"email_address": "samrawitguangulb@gmail.com", "status": "subscribed"})
  print(response)
except ApiClientError as error:
  print("Error: {}".format(error.text))
