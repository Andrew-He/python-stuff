#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi


formGet = """
		<form action="/testform">   
			<input name="q">
			<input type="submit">
		</form>
		"""
formPost = """
		<form method="post" action=/testform>
			<input name="q">
			<input type="submit">
		</form>
		"""
form = """
		<form method ="post">
			what is your birthday?
			<br>
			<label>Year 
				<input type = "text" name ="year" value = %(year)s>
			</label>
			<label>Month
				<input type = "text" name ="month" value = %(month)s>
			</label>
			<label>Day
				<input type = "text" name ="day" value = %(day)s>
			</label>
			<div style="color:red"> %(error)s </div>
			<br>
			<input type ="submit">
		</form>
		"""

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']

month_abbvs = dict((m[:3].lower(), m) for m in months)

def valid_month(month):
	if month:
		short_month = month[:3].lower() 
		return month_abbvs.get(short_month)

def valid_day(day):
	if day and day.isdigit():
		day = int(day)
		if day > 0 and day <= 31:
			return day

def valid_year(year):
	if year and year.isdigit():
		year = int(year)
		if 1900 < year and year < 2020:
			return year

def escape_html(s):
	for (i, o) in (("&", "&amp;"), 
					(">", "&gt;"), 
					("<", "&lt;"), 
					('"', "&quot;")):
		s = s.replace(i,o)
	return s 

class MainHandler(webapp2.RequestHandler):
    def write_form(self,error="", year="", month ="", day=""):
    	self.response.out.write(form % {"error" : error, 
    									"year" : cgi.escape(year, quote=True), 
    									"month": cgi.escape(month, quote=True), 
    									"day":   cgi.escape(day, quote=True)  })

    def get(self):
    	# self.response.headers['Content-Type'] = 'text/html'
        self.write_form()

    def post(self):
    	user_year = self.request.get('year')
    	user_month = self.request.get('month')
    	user_day =  self.request.get('day')

    	year = valid_year(user_year)
    	month = valid_month(user_month)
    	day = valid_day(user_day)
 
    	if not ( month and day and year):
    		self.write_form("format wrong", user_year,  user_month, user_day)
    	else:	 
    		self.redirect( "/thanks" )  


class TestHandler(webapp2.RequestHandler):
	def post(self):
		q = self.request.get('q')
		self.response.headers['Content-Type']='text/plain'
		self.response.out.write(self.request)

class ThanksHandler(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type']='text/html'
		self.response.out.write("<center>Thanks for submission</center>")
		

app = webapp2.WSGIApplication([
    ('/', MainHandler), 
    ('/thanks', ThanksHandler), 
    ('/testform', TestHandler)
], debug=True)








