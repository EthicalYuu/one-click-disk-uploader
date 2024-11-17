# One-Click Disk Uploader

A simple and efficient tool to back up selected folders to a USB flash drive with just a single click. This application provides a user-friendly interface to select, manage, and back up folders to a connected USB drive, ensuring your data is safe and accessible.

## Features

- Detects all connected USB drives.
- Add and remove folders from the backup list.
- Automatically creates directories on the USB drive for the backed-up files.
- Saves folder paths for future sessions.
- Simple graphical user interface using `Tkinter`.
- Error handling for missing or incorrect drive selections.

## Getting Started

Follow these instructions to get a copy of the project running on your local machine.

### Prerequisites

- Python 3.6 or higher
- Required Python libraries:
  - `tkinter`
  - `os`
  - `shutil`
  - `pickle`
  - `distutils.dir_util`

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/EthicalYuu/one-click-disk-uploader.git
2. Navigate to the project directory:
   ```bash
   cd one-click-disk-uploader
3. Install any missing Python libraries (if necessary):
   ```bash
   pip install tkinter

### Usage
1. Run the application:
   ```bash
   python app.py
2. Use the following controls in the interface:
- **Choose FlashDrive**: Select the USB drive for backup.
- **Add Folder**: Add folders to the backup list.
- **Remove Folder**: Remove a selected folder from the list.
- **Back Up**: Start the backup process.
- On closing the application, you can choose to save the current folder paths for the next session.

## How It Works

- The application detects available USB drives and displays them in a dropdown menu.
- You can add folders to the backup list, which is saved persistently using Python's `pickle` module.
- During the backup process, selected folders are copied to the specified USB drive, maintaining their structure.

## Future Enhancements

- Refactor the code: The current code could benefit from optimization and improvements in structure and design, as it was written early in my programming journey.
- Add progress bars for real-time feedback during the backup process.
- Implement support for non-Windows operating systems.
- Allow customization of folder names in the USB drive.
- Include additional file validation options.


