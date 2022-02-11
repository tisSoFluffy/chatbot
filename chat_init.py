import init
from libraries import pickle
from tensorflow.keras.models import load_model
import json
import random

model = load_model('chatbot_model.h5')

intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))


#classes = ['small_business_cases', 'customer_experience', 'digitial_engagement',
#           'ecommerce','commerce_cloud','b2b_commerce','mobile_commerce','progyny-personalization-and-service-at-scale',
#           'resources','omni_channel_retail','articles','faq','analytics','sales-analytics','support_and_service_analytics',
 #          'tableau-dashboards','accelerators','marketing-analytics','finance-analytics','human-resources-analytics'
#           'solutions','white-papaers','it-analytics','modern-data-architecture','banking-analytics','healthcare-analytics','government-analytics','communications-media','manufacturing-analytics',
 #          'retail-and-wholesale-analytics'
 #          'customer-success-stories','sales-cloud']

#save words
#with open('words.pkl', 'wb') as f:
#    pickle.dump(words, f)
