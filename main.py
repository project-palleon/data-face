import cv2
import numpy as np
from palleon import encode_image_as_jpeg
from palleon.data_plugin import DataPlugin


class FaceDataPlugin(DataPlugin):
    def __init__(self):
        super().__init__([])

        self._cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    def image_received_hook(self, data, image, input_source, other_metadata):
        current_frame = np.array(image, dtype=np.uint8)
        current_frame_gray = cv2.cvtColor(current_frame, cv2.COLOR_RGB2GRAY)

        faces = self._cascade.detectMultiScale(current_frame_gray)

        if len(faces) == 0:
            return {
                "last_face_img_binary": b"",
            }

        biggest_face = None

        for x, y, width, height in faces:
            if biggest_face is None:
                biggest_face = (x, y, width, height)
                continue

            if width * height > biggest_face[2] * biggest_face[3]:
                biggest_face = (x, y, width, height)

        last_face_img_binary = encode_image_as_jpeg(
            current_frame[biggest_face[1]:biggest_face[1] + biggest_face[3], biggest_face[0]:biggest_face[0] + biggest_face[2]])

        # if input_source == "cam":
        #     cv2.imshow("Gesichter", current_frame)
        #     cv2.waitKey(1)

        return {
            "last_face_img_binary": last_face_img_binary,
        }


if __name__ == "__main__":
    FaceDataPlugin().run()
