import requests, requests_oauthlib, sys, json


def init_auth(consumer_key, consumer_secret, access_token, access_secret):
	auth_obj = requests_oauthlib.OAuth1(consumer_key, consumer_secret, access_token, access_secret)
	if verify_credentials(auth_obj):
		print ('Validated credentials OK')
		return auth_obj
	else:
		print ('Credentials validation failed')
		sys.exit(1)

def verify_credentials(auth_obj):
	url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
	response = requests.get(url, auth=auth_obj)
	print ("Auth Request status = ",response.status_code)
	return response.status_code
	#get_mentions(auth_obj)
	
def get_mentions(auth_obj):
		url = "https://api.twitter.com/1.1/statuses/mentions_timeline.json?count=200&since_id=1"
		response = requests.get(url, auth=auth_obj)
		for tweets in json.loads(response.text):
			print (tweets['text'])
		#print (response.text)
		print ("Twitter Mentions",response.status_code)

def help():
		print ("Please pass three arguments e.g. python <Script> <API KEY> <API SECRET> <ACCESS TOKEN> <ACCESS TOKEN SECRECT>")
		sys.exit()
	
if __name__ == '__main__':
	if len(sys.argv) < 4:
		help()
	else:
		consumer_key=sys.argv[1]
		consumer_secret=sys.argv[2]
		access_token=sys.argv[3]
		Access_Token_Secret=sys.argv[4]
	auth_obj = init_auth(consumer_key, consumer_secret, access_token, Access_Token_Secret)
	get_mentions(auth_obj)