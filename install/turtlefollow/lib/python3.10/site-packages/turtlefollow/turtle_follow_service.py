import random
from rclpy.node import Node
from turtlesim.srv import Spawn
from turtlesim.srv import TeleportAbsolute
from turtlefollow.srv import FollowTurtle

class TurtleFollowService(Node):
    def __init__(self):
        super().__init__('turtle_follow_service')
        self.srv = self.create_service(FollowTurtle, '/turtles_follow', self.follow_turtle_callback)
        self.turtles = ["turtle1", "turtle2", "turtle3"]  # Placeholder: Gerçek turtle listesi

    def follow_turtle_callback(self, request, response):
        target_turtle_name = request.target_name
        self.get_logger().info(f'Following target turtle: {target_turtle_name}')

        # Check if the turtle exists
        if target_turtle_name not in self.get_turtles():
            response.success = False
            response.message = f"Turtle {target_turtle_name} not found. Available turtles: {', '.join(self.get_turtles())}"
        else:
            # Move all turtles to follow the target turtle
            for turtle in self.get_turtles():
                if turtle != target_turtle_name:
                    self.follow_target_turtle(turtle, target_turtle_name)
            response.success = True
            response.message = "OK"
        return response

    def get_turtles(self):
        # Gerçek zamanlı olarak mevcut olan turtles'ı döndürmelisiniz
        # Placeholder olarak self.turtles'ı kullanıyoruz
        return self.turtles

    def follow_target_turtle(self, turtle_name, target_name):
        # Gerçek bir takip için hedef turtle'ın koordinatlarını almanız gerekiyor
        target_x, target_y = self.get_turtle_position(target_name)
        client = self.create_client(TeleportAbsolute, f'/{turtle_name}/teleport_absolute')
        while not client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info(f'Waiting for /{turtle_name}/teleport_absolute service...')
        request = TeleportAbsolute.Request()
        request.x = target_x
        request.y = target_y
        client.call_async(request)

    def get_turtle_position(self, turtle_name):
        # Gerçek bir takip için turtle'ın konumunu almanız gerekiyor
        # Placeholder olarak sabit bir koordinat kullanıyoruz
        return 5.0, 5.0  # Bu kısım hedef turtle'ın gerçek konumu ile güncellenmeli

def main(args=None):
    import rclpy
    rclpy.init(args=args)
    node = TurtleFollowService()
    rclpy.spin(node)

if __name__ == '__main__':
    main()
