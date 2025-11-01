#!/usr/bin/env python3
import subprocess
import os
import glob
import argparse
from typing import Dict, List, Tuple, Optional, Any

class LanguageManager:
    """Class for managing interface translations"""
    
    def __init__(self) -> None:
        self.languages: Dict[str, Dict[str, str]] = {
            'ru': self.get_russian_texts(),
            'en': self.get_english_texts()
        }
        self.current_lang = 'ru'
    
    def get_russian_texts(self) -> Dict[str, str]:
        return {
            # Common texts
            'title': "Скрипт для создания скриншотов и получения информации о видео",
            'general_params': "📁 Общие параметры:",
            'input_file': "Введите путь к видеофайлу",
            'file_not_found': "⚠️  Файл '{}' не найден!",
            'default_value': "по умолчанию: {}",
            
            # Command sections
            'section_ffmpeg': "1. Создание скриншотов с помощью FFmpeg",
            'section_vcsi': "2. Создание сетки скриншотов с помощью vcsi.py", 
            'section_mediainfo': "3. Получение технической информации о видео",
            'section_confirmation': "Подтверждение выполнения команд",
            
            # FFmpeg parameters
            'ffmpeg_fps': "Интервал скриншотов (1/fps)",
            'ffmpeg_quality': "Качество (1-31, где 1 - лучшее)",
            'ffmpeg_output': "Шаблон имен файлов скриншотов",
            
            # VCSI parameters
            'vcsi_width': "Ширина сетки в пикселях",
            'vcsi_grid': "Размер сетки (столбцы x строки)",
            'vcsi_end_delay': "Задержка в конце (%)",
            'vcsi_start_delay': "Задержка в начале (%)", 
            'vcsi_output': "Имя выходного файла",
            
            # MediaInfo parameters
            'mediainfo_output': "Имя файла для информации",
            
            # Confirmation and execution
            'confirmation_title': "Будут выполнены следующие команды:",
            'confirmation_prompt': "Выполнить команды? (y/n): ",
            'cancelled': "Отмена выполнения.",
            'execution_start': "🚀 Начало выполнения команд",
            
            # Execution status
            'executing': "Выполняется команда: {}",
            'success': "✅ Команда выполнена успешно",
            'error': "❌ Ошибка при выполнении команды: {}",
            'error_stderr': "Ошибка: {}",
            'command_not_found': "❌ Команда или программа не найдена. Проверьте установку необходимого ПО.",
            
            # Results
            'results_title': "Итоги выполнения:",
            'success_count': "Успешно выполнено: {} из {} команд",
            'all_success': "🎉 Все команды выполнены успешно!",
            'some_errors': "⚠️  Некоторые команды завершились с ошибками",
            'created_files': "Созданные файлы:",
            'file_exists': "  📄 {}",
            
            # Command descriptions
            'desc_ffmpeg': "Создание отдельных скриншотов (FFmpeg)",
            'desc_vcsi': "Создание сетки скриншотов (VCSI)", 
            'desc_mediainfo': "Получение технической информации (MediaInfo)",
            
            # Language selection
            'language_choice': "Выберите язык / Choose language:",
            'language_option_ru': "1 - Русский",
            'language_option_en': "2 - English",
            'language_invalid': "Неверный выбор. Используется русский язык по умолчанию. / Invalid choice. Using default Russian.",
            
            # New texts for file selection
            'file_selection_title': "Найденные видеофайлы в текущем каталоге:",
            'file_selection_prompt': "Выберите номер файла или введите путь вручную",
            'file_selection_option': "  {} - {}",
            'file_selection_manual': "  {} - Ввести путь вручную",
            'file_selection_invalid': "Неверный номер файла. Попробуйте снова.",
            'no_video_files': "Видеофайлы не найдены в текущем каталоге.",
        }
    
    def get_english_texts(self) -> Dict[str, str]:
        return {
            # General texts
            'title': "Script for creating screenshots and getting video information",
            'general_params': "📁 General parameters:",
            'input_file': "Enter path to video file",
            'file_not_found': "⚠️  File '{}' not found!",
            'default_value': "default: {}",
            
            # Command sections
            'section_ffmpeg': "1. Creating screenshots with FFmpeg",
            'section_vcsi': "2. Creating screenshot grid with vcsi.py",
            'section_mediainfo': "3. Getting technical information about video", 
            'section_confirmation': "Command execution confirmation",
            
            # FFmpeg parameters
            'ffmpeg_fps': "Screenshot interval (1/fps)",
            'ffmpeg_quality': "Quality (1-31, where 1 is best)",
            'ffmpeg_output': "Screenshot filename pattern",
            
            # VCSI parameters
            'vcsi_width': "Grid width in pixels",
            'vcsi_grid': "Grid size (columns x rows)",
            'vcsi_end_delay': "End delay (%)",
            'vcsi_start_delay': "Start delay (%)",
            'vcsi_output': "Output filename",
            
            # MediaInfo parameters
            'mediainfo_output': "Information output filename",
            
            # Confirmation and execution
            'confirmation_title': "The following commands will be executed:",
            'confirmation_prompt': "Execute commands? (y/n): ",
            'cancelled': "Execution cancelled.",
            'execution_start': "🚀 Starting command execution",
            
            # Execution status
            'executing': "Executing command: {}",
            'success': "✅ Command completed successfully",
            'error': "❌ Error executing command: {}",
            'error_stderr': "Error: {}",
            'command_not_found': "❌ Command or program not found. Check required software installation.",
            
            # Results
            'results_title': "Execution results:",
            'success_count': "Successfully executed: {} out of {} commands",
            'all_success': "🎉 All commands completed successfully!",
            'some_errors': "⚠️  Some commands completed with errors",
            'created_files': "Created files:",
            'file_exists': "  📄 {}",
            
            # Command descriptions
            'desc_ffmpeg': "Creating individual screenshots (FFmpeg)",
            'desc_vcsi': "Creating screenshot grid (VCSI)",
            'desc_mediainfo': "Getting technical information (MediaInfo)",
            
            # Language selection
            'language_choice': "Выберите язык / Choose language:",
            'language_option_ru': "1 - Русский",
            'language_option_en': "2 - English", 
            'language_invalid': "Неверный выбор. Используется русский язык по умолчанию. / Invalid choice. Using default Russian.",
            
            # New texts for file selection
            'file_selection_title': "Found video files in current directory:",
            'file_selection_prompt': "Select file number or enter path manually",
            'file_selection_option': "  {} - {}",
            'file_selection_manual': "  {} - Enter path manually",
            'file_selection_invalid': "Invalid file number. Please try again.",
            'no_video_files': "No video files found in current directory.",
        }
    
    def set_language(self, lang_code: str) -> bool:
        """Set the current language"""
        if lang_code in self.languages:
            self.current_lang = lang_code
            return True
        return False
    
    def get_text(self, key: str, *args: Any) -> str:
        """Get text in current language with argument substitution"""
        text = self.languages[self.current_lang].get(key, key)
        if args:
            try:
                return text.format(*args)
            except:
                return text
        return text

# Global object for language management
lang = LanguageManager()

def find_video_files(search_dir: str) -> List[str]:
    """Find video files in specified directory"""
    video_extensions: List[str] = ['*.mkv', '*.mp4', '*.avi', '*.mov', '*.wmv', '*.flv', 
                       '*.webm', '*.m4v', '*.3gp', '*.ts', '*.mts', '*.m2ts']
    video_files: List[str] = []
    
    for extension in video_extensions:
        pattern = os.path.join(search_dir, extension)
        video_files.extend(glob.glob(pattern))
    
    return sorted(video_files)

def choose_video_file(input_dir: str) -> Optional[str]:
    """Function to select video file from input directory or enter manually"""
    video_files = find_video_files(input_dir)
    
    if not video_files:
        print(lang.get_text('no_video_files'))
        return get_input(lang.get_text('input_file'))
    
    print(f"\n{lang.get_text('file_selection_title')}")
    
    # Display found files
    for i, file in enumerate(video_files, 1):
        filename = os.path.basename(file)
        print(lang.get_text('file_selection_option', i, filename))
    
    # Add manual input option
    print(lang.get_text('file_selection_manual', len(video_files) + 1))
    
    try:
        choice = input(f"\n{lang.get_text('file_selection_prompt')}: ").strip()
            
        if not choice:
            # If empty input, use first file
            return video_files[0]
            
        if choice.isdigit():
            choice_num = int(choice)
            if 1 <= choice_num <= len(video_files):
                return video_files[choice_num - 1]
            elif choice_num == len(video_files) + 1:
                return get_input(lang.get_text('input_file'))
            else:
                print(lang.get_text('file_selection_invalid'))
        else:
            # If not a number, treat as direct file path
            return choice
                
    except ValueError:
        print(lang.get_text('file_selection_invalid'))

    return None

def choose_language() -> None:
    """Function for language selection"""
    print("=" * 60)
    print(lang.get_text('language_choice'))
    print(lang.get_text('language_option_ru'))
    print(lang.get_text('language_option_en'))
    
    choice = input("Ваш выбор / Your choice (1/2): ").strip()
    
    if choice == '2':
        lang.set_language('en')
        print("Language set to English")
    elif choice == '1':
        lang.set_language('ru') 
        print("Язык установлен: Русский")
    else:
        print(lang.get_text('language_invalid'))

def get_input(prompt: str, default: Optional[str] = None) -> Optional[str]:
    """Function to get user input with default value"""
    if default:
        prompt_text = f"{prompt} [{lang.get_text('default_value').format(default)}]: "
    else:
        prompt_text = f"{prompt}: "
    
    user_input = input(prompt_text).strip()
    return user_input if user_input else default

def run_command(command: str, description: str) -> bool:
    """Function to execute command with error handling"""
    print(f"\n{description}")
    print(lang.get_text('executing', command))
    
    try:
        # Execute command and capture output
        result = subprocess.run(
            command, 
            shell=True, 
            check=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            text=True, 
            encoding='utf-8'
        )
        print(lang.get_text('success'))
        if result.stdout:
            print(f"Output: {result.stdout}")
        return True
    except subprocess.CalledProcessError as e:
        # Handle command execution errors
        print(lang.get_text('error', e))
        if e.stderr:
            print(lang.get_text('error_stderr', e.stderr))
        return False
    except FileNotFoundError:
        # Handle case when command is not found
        print(lang.get_text('command_not_found'))
        return False

def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description=lang.get_text('title'))
    parser.add_argument(
        '--input-dir', '-i',
        type=str,
        default='.',
        help='Input directory for video files (default: current directory)'
    )
    parser.add_argument(
        '--output-dir', '-o', 
        type=str,
        default='.',
        help='Output directory for generated files (default: current directory)'
    )
    return parser.parse_args()

def main() -> None:
    # Parse command line arguments
    args = parse_arguments()
    
    # Normalize paths
    input_dir = os.path.abspath(args.input_dir)
    output_dir = os.path.abspath(args.output_dir)
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Language selection at startup
    choose_language()
    
    print("=" * 60)
    print(lang.get_text('title'))
    print("=" * 60)
    print(f"Input directory: {input_dir}")
    print(f"Output directory: {output_dir}")
    
    # Request video file selection
    print(f"\n{lang.get_text('general_params')}")
    input_file = choose_video_file(input_dir)
    if input_file is None:
        return
    
    # Check if input file exists
    if not os.path.exists(input_file):
        print(lang.get_text('file_not_found', input_file))
        return
    
    # Command 1: FFmpeg screenshots
    print("\n" + "=" * 40)
    print(lang.get_text('section_ffmpeg'))
    print("=" * 40)
    
    fps = get_input(lang.get_text('ffmpeg_fps'), "1000")
    quality = get_input(lang.get_text('ffmpeg_quality'), "1")
    output_pattern = get_input(lang.get_text('ffmpeg_output'), "screenshot_%02d.jpg")
    if output_pattern is None:
        return
    
    # Use output directory for ffmpeg output
    ffmpeg_output = os.path.join(output_dir, output_pattern)
    ffmpeg_cmd = f'ffmpeg -i "{input_file}" -vf "fps=1/{fps}" -qscale:v {quality} {ffmpeg_output}'
    
    # Command 2: VCSI grid screenshots
    print("\n" + "=" * 40)
    print(lang.get_text('section_vcsi'))
    print("=" * 40)
    
    width = get_input(lang.get_text('vcsi_width'), "800")
    grid = get_input(lang.get_text('vcsi_grid'), "4x6")
    end_delay = get_input(lang.get_text('vcsi_end_delay'), "0")
    start_delay = get_input(lang.get_text('vcsi_start_delay'), "0")
    if start_delay is None:
        return
    vcsi_output_name = get_input(lang.get_text('vcsi_output'), "screenlist.jpg")
    if vcsi_output_name is None:
        return
    
    # Use output directory for vcsi output
    vcsi_output = os.path.join(output_dir, vcsi_output_name)
    vcsi_cmd = f'vcsi "{input_file}" -t -w {width} -g {grid} --end-delay-percent {end_delay} --start-delay-percent {start_delay} -o {vcsi_output}'
    
    # Command 3: Mediainfo
    print("\n" + "=" * 40)
    print(lang.get_text('section_mediainfo'))
    print("=" * 40)
    
    mediainfo_output_name = get_input(lang.get_text('mediainfo_output'), "mediainfo.txt")
    if mediainfo_output_name is None:
        return
    
    # Use output directory for mediainfo output
    mediainfo_output = os.path.join(output_dir, mediainfo_output_name)
    mediainfo_cmd = f'mediainfo --LogFile="{mediainfo_output}" "{input_file}"'
    
    # Execution confirmation
    print("\n" + "=" * 50)
    print(lang.get_text('section_confirmation'))
    print("=" * 50)
    
    commands: List[Tuple[str, str]] = [
        (ffmpeg_cmd, lang.get_text('desc_ffmpeg')),
        (vcsi_cmd, lang.get_text('desc_vcsi')),
        (mediainfo_cmd, lang.get_text('desc_mediainfo'))
    ]
    
    # Display all commands that will be executed
    print(lang.get_text('confirmation_title'))
    for i, (cmd, desc) in enumerate(commands, 1):
        print(f"\n{i}. {desc}:")
        print(f"   {cmd}")
    
    # Get confirmation from user
    confirm_prompt = lang.get_text('confirmation_prompt')
    if lang.current_lang == 'ru':
        confirm_options = ['y', 'yes', 'д', 'да']
    else:
        confirm_options = ['y', 'yes']
        
    confirm = input(f"\n{confirm_prompt}").strip().lower()
    
    if confirm not in confirm_options:
        print(lang.get_text('cancelled'))
        return
    
    # Execute commands
    print("\n" + lang.get_text('execution_start') + "=" * 40)
    
    success_count = 0
    for cmd, desc in commands:
        if run_command(cmd, desc):
            success_count += 1
    
    # Display results
    print("\n" + "=" * 50)
    print(lang.get_text('results_title'))
    print(lang.get_text('success_count', success_count, len(commands)))
    
    if success_count == len(commands):
        print(lang.get_text('all_success'))
    else:
        print(lang.get_text('some_errors'))
    
    # Show created files
    print(f"\n{lang.get_text('created_files')}")
    created_files: List[str] = [
        ffmpeg_output.replace('%02d', '*'),  # Pattern for ffmpeg files
        vcsi_output,
        mediainfo_output
    ]
    for file_pattern in created_files:
        if '*' in file_pattern:
            # Handle file patterns with wildcards
            files: List[str] = glob.glob(file_pattern)
            for f in files:
                if os.path.exists(f):
                    print(lang.get_text('file_exists', f))
        else:
            # Handle single files
            if os.path.exists(file_pattern):
                print(lang.get_text('file_exists', file_pattern))

if __name__ == "__main__":
    main()