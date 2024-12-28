import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from datetime import datetime

class DateTimePublisher(Node):
    def __init__(self):
        super().__init__('datetime_publisher')
        self.publisher_ = self.create_publisher(String, 'current_datetime', 10)
        timer_period = 1.0  # 1秒ごとに日時を出力
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        msg = String()
        msg.data = current_time
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {current_time}')

def main(args=None):
    rclpy.init(args=args)
    node = DateTimePublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
