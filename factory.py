#When to use?
#
#// This is complicated. Instead use a factory
#$TVObj = new TV($param1, $param2, $param3);
#$LivingroomObj = new LivingRoom($TVObj, $param1, $param2);
#$KitchenroomObj = new Kitchen($param1, $param2);
#$HouseObj = new House($LivingroomObj, $KitchenroomObj);
#
#// Like this ...
#class HouseFactory {
#    public function create() {
#        $TVObj = new TV($param1, $param2, $param3);
#        $LivingroomObj = new LivingRoom($TVObj, $param1, $param2);
#        $KitchenroomObj = new Kitchen($param1, $param2);
#        $HouseObj = new House($LivingroomObj, $KitchenroomObj);
#
#        return $HouseObj;
#    }
#}
#
#$houseFactory = new HouseFactory();
#$HouseObj = $houseFactory->create();
#
# Factory pattern

class Shape(object):
	
	# Create based on class name
	def factory(type):
		if type == "Circle": return Circle()
		if type == "Square": return Square()
		if type == "Triangle": return Triangle()
		assert 0, "Bad Shape creation: " + type
	# Make factory a static method
	factory = staticmethod(factory)

class Circle:
	def draw(self): print("Circle.draw")
	def erase(self): print("Circle.erase")

class Square:
	def draw(self): print("Square.draw")
	def erase(self): print("Square.erase")

class Triangle:
	def draw(self): print("Triangle.draw")
	def erase(self): print("Triangle.erase")

def main():
	a = Shape.factory("Circle")
	a.draw()
	a.erase()

	b = Shape.factory("Square")
	b.draw()
	b.erase()

	c = Shape.factory("Triangle")
	c.draw()
	c.erase()

if __name__ == "__main__":
	main()
