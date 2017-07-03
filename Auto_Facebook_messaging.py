from fbchat import Client
from fbchat.models import *
import time
import random
from nltk.corpus import brown

client = Client(<username>, <password>)

users  = client.searchForUsers(<username>)
u_id   = users[0].uid

l = brown.sents()

while True:
	next_msg = l[int(random.random() * len(l))]
	time.sleep(random.random() * 5)
	print next_msg
	client.sendMessage(' '.join(next_msg), thread_id=u_id, thread_type=ThreadType.USER)

client.logout()
