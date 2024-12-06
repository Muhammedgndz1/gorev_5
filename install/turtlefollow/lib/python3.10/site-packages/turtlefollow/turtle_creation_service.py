import random
from rclpy.node import Node
from turtlefollow.srv import CreateTurtles
from turtlesim.srv import Spawn

class TurtleCreationService(Node):
    def __init__(self):
        super().__init__('turtle_creation_service')
        self.srv = self.create_service(CreateTurtles, '/turtles_create', self.create_turtles_callback)

    def create_turtles_callback(self, request, response):
        turtle_count = request.count
        self.get_logger().info(f'Creating {turtle_count} turtles...')
        
        for i in range(turtle_count):
            name = f"turtle_{i+1}"  # Artan bir sayaçla benzersiz isim oluştur
            x = random.uniform(0.0, 11.0)
            y = random.uniform(0.0, 11.0)
            theta = random.uniform(0.0, 3.14159)

            spawn_client = self.create_client(Spawn, '/spawn')
            while not spawn_client.wait_for_service(timeout_sec=1.0):
                self.get_logger().info('Waiting for /spawn service...')
            
            spawn_request = Spawn.Request()
            spawn_request.x = x
            spawn_request.y = y
            spawn_request.theta = theta
            spawn_request.name = name
            future = spawn_client.call_async(spawn_request)
            future.add_done_callback(self.spawn_callback)

        response.success = True
        response.message = f"{turtle_count} turtles created"
        return response

    def spawn_callback(self, future):
        try:
            future.result()
            self.get_logger().info('Turtle created successfully')
        except Exception as e:
            self.get_logger().error(f'Service call failed: {e}')
