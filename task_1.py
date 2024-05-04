from pathlib import Path
import shutil
import sys

def parse_arguments():

    if len(sys.argv) > 1:
        source_dir = Path(sys.argv[1])
    else:
        source_dir = Path(".")
    if len(sys.argv) > 2:
        destination_dir = Path(sys.argv[2])
    else:
        destination_dir = Path("dist")
    return source_dir, destination_dir

def copy_files(source_dir, destination_dir):
    
    for item in source_dir.iterdir():
        if item.is_dir():
            copy_files(item, destination_dir)
        else:
            try:
                extension = item.suffix
                extension_dir = destination_dir / extension[1:]
                extension_dir.mkdir(parents=True, exist_ok=True)
                shutil.copy2(item, extension_dir)
            except Exception as e:
                print(f"Помилка: {e}")

def main():
    source_dir, destination_dir = parse_arguments()
    destination_dir.mkdir(parents=True, exist_ok=True)
    copy_files(source_dir, destination_dir)
    print("Копіювання завершено.")

if __name__ == "__main__":
    main()
