from typing import List, Tuple

from hazards_detection.pothole_detection.pothole_video_detection import analyze_potholes_video
from map_generator import generate_map


def camera() -> str:
    """

    :return:
    """
    return r"C:\Networks\pothole-detection\stock-footage-vehicle-tyre-driving-over-a-" \
           r"damaged-highway-which-is-covered-in-po_m7l7AT5Q.webm"


def hazard_detector(video_path: str) -> List[Tuple[Tuple[float, float], str]]:
    """
    :param video_path:
    :return:list of coordinates and the photo path for this coordinate image
    """
    return analyze_potholes_video(video_path)


def main():
    video_path = camera()
    analyzed_result = hazard_detector(video_path)
    # hazard_type = 'pothole'
    icon_path = 'icon.png'
    hazards_data = []
    print(len(hazards_data))

    for image_path, coordinates, hazard_type in analyzed_result:
        latitude = coordinates[0]
        longitude = coordinates[1]
        hazards_data.append((latitude, longitude, hazard_type, icon_path))

    generated_map = generate_map(hazards_data)
    generated_map.save("hazards_map.html")
    # print_map(analyzed_result)


if __name__ == "__main__":
    main()
