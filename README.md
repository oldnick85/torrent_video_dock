# 🎬 Torrent Video Dock

A Docker-based automation tool that prepares videos for torrent publishing. This Python script provides an interactive interface for video analysis, processing, and metadata preparation using FFmpeg, [vcsi](https://github.com/amietn/vcsi), and MediaInfo. 🚀

## ✨ Features

- **🌍 Interactive Multi-language Interface**: Choose between Russian and English interfaces
- **🔍 Smart File Selection**: Automatically detects video files in the directory or allows manual input
- **📸 Multiple Screenshot Modes**:
  - Individual screenshots using FFmpeg with customizable intervals
  - Screenshot grid creation using vcsi with adjustable layout
- **📊 Technical Metadata Extraction**: Get detailed video information using MediaInfo
- **🐳 Docker Containerization**: Easy deployment without local dependencies
- **👨‍💻 User-friendly Workflow**: Step-by-step guidance with confirmation prompts

## 📁 Supported Video Formats

- 🎥 MKV, MP4, AVI, MOV, WMV, FLV, WebM, M4V, 3GP, TS, MTS, M2TS

## ⚙️ Requirements

- Docker 🐳
- Docker Compose 🔧

## 🚀 Quick Start

1. **📥 Clone or download the project files**:
 - `main.py`
 - `Dockerfile` 
 - `docker-compose.yml`

2. **📂 Place your video files** in the same directory as the project files

3. **🎯 Run the application**:

```bash
docker-compose run --rm torrent-video-dock
```

## 🛠️ How It Works

### 1. 🌐 Language Selection

Choose your preferred interface language (Russian/English) at startup. 🗣️

### 2. 📋 File Selection

 - The script automatically scans for video files in the current directory 🔍
 - Select from the list or enter a custom file path 📝
 - Supports both relative and absolute paths 🗺️

### 3. 🖼️ Screenshot Configuration

FFmpeg Screenshots: 🎞️

 - Set screenshot interval (frames per second) ⏱️
 - Configure image quality (1-31 scale) 🌟
 - Custom output filename pattern 🏷️

VCSI Grid Screenshots: 🎨

 - Adjust grid width in pixels 📏
 - Set grid dimensions (columns × rows) 🔲
 - Configure start/end delays ⏰
 - Custom output filename 🏷️

### 4. 📊 Technical Information

 - Extract comprehensive media information using MediaInfo 🔧
 - Save to a text file for reference 📄

### 5. ⚡ Execution & Results

 - Review all commands before execution 👀
 - Real-time progress and error reporting 📈
 - Summary of created files and success status ✅

 ## 📤 File Outputs

The script generates three types of files:

 - 📸 Individual Screenshots (screenshot_01.jpg, screenshot_02.jpg, etc.)
 - 🖼️ Screenshot Grid (screenlist.jpg - customizable collage)
 - 📊 Technical Information (mediainfo.txt - detailed video metadata)

## ⚙️ Configuration Options

Command Line Arguments

 - --input-dir, -i: 📁 Specify input directory (default: current directory)
 - --output-dir, -o: 📂 Specify output directory (default: current directory)

Docker Volume Configuration

Modify docker-compose.yml to change volume mounts:
```yaml
volumes:
  - /path/to/your/videos:/app/data/input
  - /path/to/output:/app/data/output
```

## 💡 Usage Examples

Basic Usage
```bash
docker-compose run --rm torrent-video-dock
```

Custom Directories
```bash
docker-compose run --rm -v /my/videos:/app/data/input -v /my/output:/app/data/output torrent-video-dock
```

## 🆘 Troubleshooting

### ❗ Common Issues

 - 🔧 "Command or program not found": Ensure all dependencies are properly installed in the Docker container
 - 📄 File not found: Verify the video file path and Docker volume mounts
 - 🔒 Permission errors: Check file permissions in mounted directories

## 🐛 Debug Mode

For detailed output, you can modify the Docker command to include shell access:
```bash
docker-compose run --rm torrent-video-dock /bin/bash
```

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! 🎉 Please feel free to submit pull requests or open issues for bugs and feature requests.

⚠️ Note: This tool is designed for legitimate video processing and preparation. Please ensure you have the appropriate rights to process any video files used with this tool.

