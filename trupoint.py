import web
urls = (
	'/', 'Home'
	)
class Parent:
	def __init__(self):
		self.render=web.template.render('templates/')
		self.request_data = web.input()
		self.header = self.render.header()
		self.footer = self.render.footer()

class Home(Parent):
	def GET(self):
		action = ''
		if self.request_data:
			if self.request_data.action == "dive":
				return self.render.dive(self.header, self.footer)

			elif self.request_data.action == "explanation":
				return self.render.explain(self.header, self.footer)

			elif self.request_data.action == "use":
				return self.render.use(self.header, self.footer)

			elif self.request_data.action == "resolution":
				return self.render.resolution(self.header, self.footer)
				
			else:
				return self.render.home(self.header, self.footer)
		else:			
			return self.render.home(self.header, self.footer)

if __name__ == '__main__':
	app=web.application(urls, globals())
	app.run()