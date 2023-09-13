import rosbag
import os


class ImageExtractor:

    def __init__(self, topics):
        self.topics = topics

    def extract_images_from_rosbag(self, rosbag_file):

        # Open the ROS bag file
        bag = rosbag.Bag(rosbag_file, 'r')

        # Iterate through the messages in the bag file
        for idx, (topic, msg, t) in enumerate(bag.read_messages(topics=['/camera/image_raw'])):
            if msg._type == 'sensor_msgs/Image':  # Check if it's an image message

                # Extract the image data as raw bytes
                image_data = bytes(msg.data)
                yield image_data

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

    for idx, image_data in enumerate(image_iterator):
        try:
            # Define the output file path (e.g., output_images/image_001.jpg)
            output_file_path = os.path.join(output_directory, f"image_{idx:04d}.jpg")

            # Save the image data to the specified output path
            with open(output_file_path, 'wb') as image_file:
                image_file.write(image_data)
                print(f"Saved {idx + 1} images to {output_directory}")


        except Exception as e:
            print(f"Error saving image {idx}: {str(e)}")

