import sys
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix  # Assuming /oxts/fix is publishing NavSatFix messages
from datetime import datetime

class FixSubscriber(Node):

    def __init__(self, filename):
        super().__init__('fix_subscriber')
        self.subscription = self.create_subscription(
            NavSatFix,
            '/oxts/fix',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        self.filename = filename
        print(self.filename)
        # Open the file in append mode
        timestamp = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
        self.file = open('data/' + self.filename + "_" + str(timestamp) + '.txt', 'a')

    def listener_callback(self, msg):
        # Get the current timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Format the message with a timestamp
        data_str = f"[{timestamp}] {msg}\n"
        
        # Write the data to the file
        self.file.write(data_str)
        self.get_logger().info(f"Written to file: {data_str.strip()}")

    def __del__(self):
        # Close the file when the node is destroyed
        self.file.close()

def main(args=None):
    if len(sys.argv) != 2:
            print("Usage: python oxts-recorder.py <output filename>")
            sys.exit(1)

    rclpy.init(args=args)

    fix_subscriber = FixSubscriber(sys.argv[1])

    try:
        rclpy.spin(fix_subscriber)
    except KeyboardInterrupt:
        pass
    finally:
        fix_subscriber.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

