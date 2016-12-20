class CollisionDetector(object) :
	
	def __init__(self, ship, asteroids, projectiles) :
		self.ship = ship
		self.asteroids = asteroids #list
		self.projectiles = projectiles #list

	'''
	Check if the ship has been hit by an specific asteroid
	'''
	def ship_hits_asteroid(self, a) :
		pass

	''' 
	Since multiple asteroids can be hit at the same time,
	this method returns a list with asteroids impacted
	'''
	def get_hit_asteroids(self, asteroids, projectiles) :
		hit_asteroids = [] 
		for a in asteroids :
			for p in projectiles :
				if self.projectile_hits_asteroid(p, a) :
					hit_asteroids.append(a)
		return hit_asteroids

	'''
	Checks if an specific asteroid has been hit by an 
	specific projectle
	'''
	def projectile_hits_asteroid(self, projectile, asteroid) :
		return  projectile.pos.distance(asteroid.pos) <= asteroid.size

	'''
	Handles the given MUTABLE types (asteroids and projectiles) when
	both collide. Return the hit asteroids so the caller can do more
	with that information, for example, create an explosion animation 
	where the asteroid was and then place more little asteroids in its
	place
	'''
	def handle_projectile_hits_asteroid(self, asteroids, projectiles, generator) :
		hit_asteroids = []
		for a in asteroids :
			for p in projectiles :
				if self.projectile_hits_asteroid(p, a) :
					#asteroids.remove(a)
					#projectiles.remove(p)
					if a.type == 1 :
						generator.generate_debris(a.pos)
