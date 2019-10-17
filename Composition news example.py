class sports:
	def sportsnews(self):
		print("SportsNews1")
		print("SportsNews1")
		print("SportsNews1")

class movie:
	def movienews(self):
		print("MovieNews1")
		print("MovieNews1")
		print("MovieNews1")


class politics:
	def politicsnews(self):
		print("politicsnews")
		print("politicsnews")
		print("politicsnews")



class durganews:
	def __init__(self,sports,movie,politics):
		self.sports=sports
		self.movie=movie
		self.politics=politics
	def totalnews(self):
		print("below is the news")
		self.sports.sportsnews()
		self.politics.politicsnews()
		self.movie.movienews()

sports=sports()
movie=movie()
politics=politics()
durganews=durganews(sports,movie,politics)
durganews.totalnews()
