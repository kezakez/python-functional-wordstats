from django.http import HttpResponse
from django import forms
from django.shortcuts import render_to_response
import httplib
from HTMLParser import HTMLParser
import json
import wordstats

class SearchForm(forms.Form):
	url = forms.CharField()

def stats(request):
	if (request.method == 'POST'):
		form = SearchForm(request.POST)
		if (form.is_valid()):
			url = form.cleaned_data['url']
			
			input = getWords(getDocument(url))

			output = wordstats.stats(input)
			jsonstats = json.dumps(output.wordcount, indent=4)
			
			return render_to_response('graph.html', { 'shortest': output.shortest, 'longest': output.longest, 'wordcount': jsonstats })
	else:
		form = SearchForm()
		
	return render_to_response('index.html', { 'form': form })

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def getWords(input):
  s = MLStripper()
  s.feed(input)
  return s.get_data()

def getDocument(url):
	# only do http links
	if (url.startswith("http://")):
		url = url.replace("http://", "", 1)
		
		# split out the url into host and doc
		host = url
		path = "/"

		urlparts = url.split("/")
		if (len(urlparts) > 1):
			host = urlparts[0]
			path = url.replace(host, "", 1)

		# make the first request
		conn = httplib.HTTPConnection(host)
		req = conn.request("GET", path)
		res = conn.getresponse()

		return res.read()
	return ""

