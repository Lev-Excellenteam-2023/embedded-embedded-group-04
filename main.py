from typing import List, Tuple
from utils.consts import VIDEO_PATH
from hazards_detection.pothole_detection.pothole_video_detection import analyze_potholes_video




def print_welcome_message():
    print("Hello! Welcome to the Pothole Detection Application")


def hazard_detector(video_path: str) -> List[Tuple[Tuple[float, float], str]]:
    return analyze_potholes_video(video_path)


def main():
    print_welcome_message()

    while True:
        print("\nOptions:")
        print("1. Detect Potholes with Video")
        print("2. Detect Potholes with Live Camera")
        print("3. Quit")
        analyzed_result = []
        choice = input("Enter your choice: ")

        if choice == '1':
            analyzed_result = hazard_detector(VIDEO_PATH)
        elif choice == '2':
            analyzed_result = hazard_detector()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
