from app import app
import requests
import sys
import json
from flask import render_template, Flask

# apiKey = '6c8ac0ed9c3bdb249bbe32d61526f18a'

response = requests.get('http://deals-api.herokuapp.com/deals/')

dealInfo = {
    deal['store'] : {
        'merchantName' : deal['store-formal'],
        'charityPictureURL' : deal['image-link'],
        'charityName' : deal['charity'],
        'percent' : deal['percent_off'],
        'merchantPictureURL' : 'http://logo.clearbit.com/' + deal['store-link']
    }
    for deal in json.loads(response.text)
}

ae = dealInfo['ae']
ae['merchantDescription'] = 'Stylish, reasonably priced clothing.'
ae['costOfCoupon'] = 10
ae['dealTitle'] = "Get " + str(ae['percent']) + "%" + " off American Eagle"

amz = dealInfo['amazon']
amz['merchantDescription'] = 'Buy anything.'
amz['costOfCoupon'] = 10
amz['dealTitle'] = "Get " + str(ae['percent']) + "%" + " off Amazon"

trg = dealInfo['target']
trg['merchantDescription'] = 'Expect more. Pay less.'
trg['costOfCoupon'] = 10
trg['dealTitle'] = "Get " + str(ae['percent']) + "%" + " off Target"

walm = dealInfo['walmart']
walm['merchantDescription'] = 'Save Money. Live Better.'
walm['costOfCoupon'] = 10
walm['dealTitle'] = "Get " + str(ae['percent']) + "%" + " off Walmart"

cvs = dealInfo['cvs']
cvs['merchantDescription'] = 'Your neighborhood drugstore.'
cvs['costOfCoupon'] = 10
cvs['dealTitle'] = "Get " + str(ae['percent']) + "%" + " off CVS"

hmd = dealInfo['homedepot']
hmd['merchantDescription'] = 'Home improvement for any budget.'
hmd['costOfCoupon'] = 10
hmd['dealTitle'] = "Get " + str(ae['percent']) + "%" + " off Home Depot"

wholf = dealInfo['wholefoodsmarket']
wholf['merchantDescription'] = 'Food you can feel warm and fuzzy about.'
wholf['costOfCoupon'] = 10
wholf['dealTitle'] = "Get " + str(ae['percent']) + "%" + " off Whole Foods"

hanm = dealInfo['hm']
hanm['merchantName'] = 'H&M'
hanm['merchantDescription'] = 'Be stylish.'
hanm['costOfCoupon'] = 10
hanm['dealTitle'] = "Get " + str(ae['percent']) + "%" + " off H&M"

f21 = dealInfo['forever21']
f21['merchantDescription'] = 'Be stylish.'
f21['costOfCoupon'] = 10
f21['dealTitle'] = "Get " + str(ae['percent']) + "%" + " off Forever 21"


@app.route('/')
def homepage():
	return render_template("homepage.html")

@app.route('/<id>')
def dealpage(id):
    try:
        info = dealInfo[id]
    except KeyError:
        return '404'
    info['pageTitle'] = info['dealTitle']  + " -  Deals For Good"

    return render_template('purchase.html', **info)
