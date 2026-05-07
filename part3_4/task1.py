# Завдання 1: Рекурсивне сортування файлів за розширенням
import sys
import shutil
from pathlib import Path


def copy_files(src: Path, dst: Path):
    try:
        for item in src.iterdir():
            if item.is_dir():
                copy_files(item, dst)
            elif item.is_file():
                tp = item.suffix[1:] if item.suffix else "No type"
                target_path = dst/tp
                target_path.mkdir(parents=True, exist_ok=True)
                shutil.copy2(item, target_path / item.name)
    except Exception as e: 
        print(f" Помилка доступу {e}")

if __name__ == "__main__":
    src_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    dst_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("dist")
    copy_files(src_dir, dst_dir)



