
class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a,**kw)

	def render_str(self,templ)

class MainPage(Handler):
	def render_front(self, title="",art="", error=""):
		self.render("front.html", title = title, art = art, error = error)

	def get(self):
		self.render_front()

	def post(self):
		title = self.request.get("title")
		art = self.request.get("art")
