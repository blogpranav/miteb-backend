import requests, time

# time.sleep(3)

token = "dqU4pVR0ew0:APA91bGj-D5rl2TIMn3HO0CNLuFCFjn9M7YjC1p9RICmGeEQHiTRGyoykrJ1xXvRhZwuESTpkR5yNd4u4zqA3hBjGlLUhKYxnrlBbBOEXijHqLlpSLsUld26EmloRybDMXz3i8uifmqJ"

tokenb = "fpUcrkFTwaI:APA91bE8fdcaDv9MY0J3sZ2fURTMeFD4GozI-sYX8n6RzJUKHBmsuSq2LEfXdtdxXxntus1qL9StwzdsFsCnvmvsxOUhOGxvn0hsUKjrLQ7XQDfIUwb8hOP7wbt3jCSGVNogXSH-sZDt"

payload = {
	'notification': {
      'title': 'Some title',
      'body': 'Blah bleh some foo bar message',
      'icon': 'https://laracasts.com/images/series/circles/do-you-react.png'
	},
};

uid = "Fq10VDgTdAf7t4o4sEUrgY08rGg2"

newinfo = {
  'email': "dummymitclub@gmail.com",
  'phoneNumber': "+917760627296",
  'emailVerified': True,
  'password': "Password@1234"
}

update_user_params = {
	'uid': uid,
	'newinfo': newinfo
}

import urllib
import urllib2

params = urllib.urlencode(update_user_params)
res = urllib2.urlopen("http://localhost:9000/update-user?" + params)
print res.read()
