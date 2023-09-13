import rosbag
import cv2
from cv_bridge import CvBridge
import os

class ImageExtractor:

    def __init__(self, topics):
        self.topics = topics

    def extract_images_from_rosbag(self, rosbag_file):
        # Open the ROS bag file
        bag = rosbag.Bag(rosbag_file, 'r')

        # Initialize a CvBridge to convert ROS Image messages to OpenCV images
        bridge = CvBridge()

        # Iterate through the messages in the bag file
        for topic, msg, t in bag.read_messages(self.topics):
            try:
                # Convert the ROS Image message to an OpenCV image
                cv_image = bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")

                # yield the image here to create an iterator
                yield cv_image

            except Exception as e:
                print("Error converting ROS Image to OpenCV image:", str(e))

        # Close the ROS bag file when done
        bag.close()


if __name__ == "__main__":
    rosbag_file = "resources/livingplace_demo.bag"  # Replace with the path to your ROS bag file
    extractor = ImageExtractor(["/loomo/camera/color/image_raw/"])
    image_iterator = extractor.extract_images_from_rosbag(rosbag_file)

    # Define the output directory where you want to save the images
    output_directory = "output_images"

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for idx, image in enumerate(image_iterator):
        # Define the output file path (e.g., output_images/image_001.jpg)
        output_file_path = os.path.join(output_directory, f"image_{idx:04d}.jpg")

        # Save the image to the specified output path
        cv2.imwrite(output_file_path, image)

    print(f"Saved {idx + 1} images to {output_directory}")
