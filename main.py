from typing import List, Tuple
from hazards_detection.pothole_detection.pothole_video_detection import analyze_potholes_video
from map.map_generation import generate_map


def camera() -> str:
    return "clip.webm"


def hazard_detector(video_path: str) -> List[Tuple[Tuple[float, float], str]]:
    """
    :param video_path:
    :return:list of coordinates and the photo path for this coordinate image
    """
    return analyze_potholes_video(video_path)


def main():
    video_path = camera()
    analyzed_result = hazard_detector(video_path)


    generated_map = generate_map(analyzed_result)
    generated_map.save("hazards_map.html")


if __name__ == "__main__":
    main()
