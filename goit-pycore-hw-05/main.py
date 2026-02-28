import sys


def parse_log_line(line: str) -> dict:
    # TODO: Розпарсити рядок. Повернути словник {'date': ..., 'time': ..., 'level': ..., 'message': ...}
    parts = line.split(" ", 3)
    if len(parts) < 4:
        return {}
    return {
        "date": parts[0],
        "time": parts[1],
        "level": parts [2],
        "message": parts[3].strip()
    }
    

def load_logs(file_path: str) -> list:
    # TODO: Відкрити файл, прочитати рядки, викликати parse_log_line для кожного.
    List_logs = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            parse_line = parse_log_line(line)
            if parse_line:
                List_logs.append(parse_line)
    return List_logs

    # Обробити помилку FileNotFoundError через try-except


def filter_logs_by_level(logs: list, level: str) -> list:
    target_level = level.upper()
    filter_logs = []
    for log in logs:
        if log["level"] == target_level:
            filter_logs.append(log)
    return filter_logs

    
def count_logs_by_level(logs: list) -> dict:
    Dict_count = {}
    for log in logs:
        level = log["level"]
        Dict_count[level] = coun
    # TODO: Порахувати скільки записів кожного рівня. Повернути словник {'INFO': 3, 'ERROR': 2 ...}
    pass

def display_log_counts(counts: dict):
    # TODO: Красиво вивести таблицю (header, separator, data)
    pass

def main():
    # 1. Перевірка sys.argv (чи передано шлях до файлу)
    
    # 2. Завантаження логів
    
    # 3. Підрахунок і вивід статистики (display_log_counts)
    
    # 4. Якщо є другий аргумент (sys.argv[2]) — вивести деталі для конкретного рівня
    pass

if __name__ == "__main__":
    main()