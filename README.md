# Video-File-Organizer
A python automation tool that recursively scans nested subdirectories, filters video files,
and consolidates them into a target directory. Built to eliminate manual file management for
large media libraries.

## Features 
- Recursive Scanning: uses 'os.walk' to traverse through all subfolders.
- Path Sanitization: uses Automatically handles dragged and dropped or inputed
paths by stripping quotes.
- Targeted Filtering: Isolates video formats ('.mkv', '.mp4', '.avi') from non-video
files.
- Safety First: Prompts for confirmation before moving files to prevent accidental relocation.

## How to Run
1. Open Command Prompt.
2. Navigate to the project directory:
'''cmd cd path\to\folder
3. Run the script
python vfo.py


