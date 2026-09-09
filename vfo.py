import os 
import shutil

while True:

            while True:
                source_dir = input("Enter the path of the folder containing the subfolders: ").strip()
                source_dir = source_dir.strip('"').strip("'")
                if os.path.exists(source_dir):
                    print()
                    print(f"Success! found directory: {source_dir}\n"
                    ) 
                    break
                else:
                    print()

                    print("Error: That directory path does not exist. TRY AGAIN!")

            print()

            video_files = []

            video_extensions_allowed = (".mp4", ".mkv", ".avi")


            for root, dirs, files in os.walk(source_dir):
                for file in files:
                    if file.lower().endswith(video_extensions_allowed):

                        full_path = os.path.join(root, file)
                        video_files.append(full_path)
                    

            print(f"Found {len(video_files)} video file(s): ")
            print()
            for video in video_files:
                print(f" - {video}")

            print()

            expected_dir = input("Enter where to move the extracted video files: ").strip('"').strip("'")
            print()
            if not os.path.exists(expected_dir):
                choice = input("Destination folder does not exist. Create it? (Y/N): ").strip('"').strip("'").upper()
                if choice == "Y":
                    os.makedirs(expected_dir)
                    print()
                    print(f"Created folder: {expected_dir}")
                else:
                    print()
                    print("Operation cancelled.")
                    exit()
            print()
            confirm = input(f"Are you sure you want to move {len(video_files)} files to {expected_dir}? (Y/N): ").strip('"').strip("'").upper()
            print()
            if confirm == "Y":
                for video_path in video_files:
                    file_name = os.path.basename(video_path)
                    target_path = os.path.join(expected_dir, file_name)
                    shutil.move(video_path, target_path)
                    print(f"Moved: {file_name}")
                print()
                print("All files moved successfully! ")

            else:
                print()
                print("Move cancelled. ")
    