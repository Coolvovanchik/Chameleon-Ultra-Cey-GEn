import random
import os
import sys
import time
from collections import OrderedDict

# Конфигурация
AUTHOR_TAG = "@Pinaplast42"
VERSION = "C.U.Gen v7.1"
DEFAULT_FILENAME = "cu_keys.dic"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SAVE_FOLDER = os.path.join(SCRIPT_DIR, "CUGEN_KEYS")

# Цветовая палитра
class Colors:
    GREEN = "\033[92m"
    DARK_GREEN = "\033[32m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"
    BOLD = "\033[1m"
    LINE = "\033[92m" + "▬" * 60 + "\033[0m"
    HEADER = "\033[92m" + "▄■▀▄■▀" * 10 + "\033[0m"

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def show_banner():
    clear_screen()
    print(f"""{Colors.DARK_GREEN}
   ██████╗ ██╗   ██╗ ██████╗ ███████╗ ███╗   ██╗
  ██╔════╝ ██║   ██║██╔════╝ ██╔════╝ ████╗  ██║
  ██║      ██║   ██║██║  ███╗█████╗   ██╔██╗ ██║
  ██║      ██║   ██║██║   ██║██╔══╝   ██║╚██╗██║
  ╚██████╗ ╚██████╔╝╚██████╔╝███████╗ ██║ ╚████║
   ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝ ╚═╝  ╚═══╝                       
    {Colors.GREEN}{VERSION} | {AUTHOR_TAG}
    {Colors.HEADER}""")

class KeyGenerator:
    @staticmethod
    def matrix_effect(text):
        for char in text:
            print(f"{Colors.GREEN}{char}{Colors.RESET}", end='', flush=True)
            time.sleep(0.02)
        print()

    @staticmethod
    def base_keys():
        return list(OrderedDict.fromkeys([
            '000000000000', 'FFFFFFFFFFFF',
            'A0A1A2A3A4A5', 'D3F7D3F7D3F7',
            'A1B2C3D4E5F6', '4B4C4F434B4C'
        ]))

    @staticmethod
    def uid_variants(uid):
        uid = uid.upper().replace(':', '')[:8].ljust(8, 'F')
        keys = set()
        
        patterns = [
            f"{uid}FFFF",
            f"FF{uid[2:]}",
            f"{uid[:6]}0000",
            f"{uid[:4]}{uid[:4]}"
        ]
        
        print(f"\n{Colors.DARK_GREEN}>>> ИНИЦИАЛИЗАЦИЯ UID-ГЕНЕРАТОРА...")
        for key in patterns:
            keys.add(key)
            print(f"{Colors.GREEN}[+] Паттерн: {Colors.YELLOW}{key}")
            time.sleep(0.1)
        
        print(f"\n{Colors.DARK_GREEN}>>> ГЕНЕРАЦИЯ СЛУЧАЙНЫХ КОМБИНАЦИЙ...")
        for _ in range(10):
            while True:
                key = f"{uid[:6]}{random.choice('0123456789ABCDEF')}{random.choice('0123456789ABCDEF')}"
                if key not in keys:
                    keys.add(key)
                    print(f"{Colors.GREEN}[+] Сгенерирован: {Colors.YELLOW}{key}")
                    time.sleep(0.05)
                    break
        
        return list(keys)

    @staticmethod
    def transport_keys():
        return list(OrderedDict.fromkeys([
            ('08904CA8C148', "Метро (Общий шаблон 1)"),
            ('76F9D4481315', "Метро (Общий шаблон 2)"),
            ('4E3554089A12', "Автобус (Стандарт A)"),
            ('AB34CD56EF78', "Автобус (Стандарт B)"),
            ('554433221100', "Электрички (Паттерн 5)"),
            ('0F0F0F0F0F0F', "Специальный транспорт"),
            ('F0F0F0F0F0F0', "Резервные системы"),
            ('AABBCCDDEEFF', "Общественный транспорт")
        ]))

    @staticmethod
    def random_keys(count):
        keys = set()
        print(f"\n{Colors.DARK_GREEN}>>> ЗАПУСК СЛУЧАЙНОЙ ГЕНЕРАЦИИ...")
        
        start_time = time.time()
        while len(keys) < count:
            key = ''.join(random.choice('0123456789ABCDEF') for _ in range(12))
            if key not in keys:
                keys.add(key)
                current = len(keys)
                if current % 1000 == 0 or current == count:
                    elapsed = time.time() - start_time
                    print(f"{Colors.GREEN}[~] Прогресс: {current}/{count} "
                          f"| Время: {elapsed:.1f}s {Colors.YELLOW}", end='\r')
        
        print(f"\n{Colors.GREEN}[✓] ГЕНЕРАЦИЯ УСПЕШНО ЗАВЕРШЕНА")
        return list(keys)

def menu():
    while True:
        show_banner()
        print(f"{Colors.DARK_GREEN}╔════════════════════════════════════════════╗")
        print(f"{Colors.GREEN}║ {Colors.YELLOW}1.{Colors.GREEN} БАЗОВЫЕ КЛЮЧИ               {Colors.DARK_GREEN}[STATUS: ONLINE]{Colors.GREEN} ║")
        print(f"{Colors.GREEN}║ {Colors.YELLOW}2.{Colors.GREEN} UID-ГЕНЕРАТОР              {Colors.DARK_GREEN}[STATUS: ONLINE]{Colors.GREEN} ║")
        print(f"{Colors.GREEN}║ {Colors.YELLOW}3.{Colors.GREEN} ТРАНСПОРТНЫЕ СИСТЕМЫ       {Colors.DARK_GREEN}[STATUS: ONLINE]{Colors.GREEN} ║")
        print(f"{Colors.GREEN}║ {Colors.YELLOW}4.{Colors.GREEN} СЛУЧАЙНАЯ ГЕНЕРАЦИЯ        {Colors.DARK_GREEN}[STATUS: ONLINE]{Colors.GREEN} ║")
        print(f"{Colors.GREEN}║ {Colors.YELLOW}0.{Colors.RED} ВЫХОД                      {Colors.DARK_GREEN}[STATUS: STANDBY]{Colors.GREEN} ║")
        print(f"{Colors.DARK_GREEN}╚════════════════════════════════════════════╝")
        
        choice = input(f"\n{Colors.GREEN}>>> ВВЕДИТЕ КОМАНДУ: {Colors.YELLOW}")
        if choice in {'0','1','2','3','4'}:
            return choice
        print(f"{Colors.RED}⚠ ОШИБКА: НЕВЕРНАЯ КОМАНДА!{Colors.RESET}")
        time.sleep(1)

def save_keys(keys, filename):
    try:
        if not os.path.exists(SAVE_FOLDER):
            os.makedirs(SAVE_FOLDER)
            print(f"{Colors.GREEN}[+] СОЗДАНА ДИРЕКТОРИЯ: {SAVE_FOLDER}")
        
        full_path = os.path.join(SAVE_FOLDER, filename)
        existing = set()
        
        if os.path.exists(full_path):
            with open(full_path, 'r') as f:
                existing = {line.strip() for line in f}
        
        unique_new = set(keys) - existing
        duplicates = len(keys) - len(unique_new)
        
        if not unique_new:
            print(f"{Colors.YELLOW}[!] НЕТ НОВЫХ КЛЮЧЕЙ ДЛЯ СОХРАНЕНИЯ")
            return False
        
        print(f"\n{Colors.DARK_GREEN}>>> НАЧАТО СОХРАНЕНИЕ ДАННЫХ...")
        with open(full_path, 'a') as f:
            for i, key in enumerate(unique_new, 1):
                f.write(f"{key}\n")
                if i % 100 == 0:
                    print(f"{Colors.GREEN}[~] ЗАПИСАНО: {i}/{len(unique_new)} "
                          f"{Colors.DARK_GREEN}| ДУБЛИКАТОВ: {duplicates}", end='\r')
        
        print(f"\n{Colors.GREEN}[✓] ДАННЫЕ УСПЕШНО ЭКСПОРТИРОВАНЫ")
        print(f"{Colors.DARK_GREEN}├ УНИКАЛЬНЫЕ КЛЮЧИ: {Colors.GREEN}{len(unique_new)}")
        print(f"{Colors.DARK_GREEN}├ ОБНАРУЖЕНО ДУБЛИКАТОВ: {Colors.RED}{duplicates}")
        print(f"{Colors.DARK_GREEN}└ ПОЛНЫЙ ПУТЬ: {Colors.YELLOW}{os.path.abspath(full_path)}")
        return True
        
    except Exception as e:
        print(f"\n{Colors.RED}[✗] КРИТИЧЕСКАЯ ОШИБКА: {e}")
        return False

def main():
    if os.name == "nt":
        os.system("title C.U.Gen - HACKER MODE")
    
    while True:
        choice = menu()
        
        if choice == '0':
            print(f"\n{Colors.GREEN}[+] ВЫХОД ИЗ СИСТЕМЫ...")
            sys.exit()
            
        keys = []
        try:
            if choice == '1':
                keys = KeyGenerator.base_keys()
                print(f"\n{Colors.GREEN}[+] БАЗОВЫЕ КЛЮЧИ ЗАГРУЖЕНЫ: {len(keys)}")
                
            elif choice == '2':
                uid = input(f"\n{Colors.GREEN}>>> ВВЕДИТЕ UID КАРТЫ: {Colors.YELLOW}").strip()
                if not all(c in '0123456789ABCDEFabcdef' for c in uid):
                    print(f"{Colors.RED}[✗] НЕВЕРНЫЙ ФОРМАТ UID!")
                    continue
                keys = KeyGenerator.uid_variants(uid)
                
            elif choice == '3':
                transport = KeyGenerator.transport_keys()
                print(f"\n{Colors.DARK_GREEN}>>> ДОСТУПНЫЕ ТРАНСПОРТНЫЕ СИСТЕМЫ:")
                for idx, (key, desc) in enumerate(transport, 1):
                    print(f"{Colors.GREEN}[{idx}] {Colors.YELLOW}{key} {Colors.DARK_GREEN}- {desc}")
                keys = [k[0] for k in transport]
                
            elif choice == '4':
                try:
                    count = int(input(f"\n{Colors.GREEN}>>> ВВЕДИТЕ КОЛИЧЕСТВО: {Colors.YELLOW}"))
                    count = max(1, count)
                    keys = KeyGenerator.random_keys(count)
                except:
                    print(f"{Colors.RED}[✗] НЕВЕРНЫЙ ВВОД!")
                    continue
            
            if keys:
                if input(f"\n{Colors.GREEN}>>> ЭКСПОРТИРОВАТЬ РЕЗУЛЬТАТ? (Y/n): {Colors.YELLOW}").lower() != 'n':
                    filename = input(f"{Colors.GREEN}>>> ИМЯ ФАЙЛА ({DEFAULT_FILENAME}): {Colors.YELLOW}") or DEFAULT_FILENAME
                    save_keys(keys, filename)
            
        except Exception as e:
            print(f"\n{Colors.RED}[✗] СИСТЕМНАЯ ОШИБКА: {e}")
        
        input(f"\n{Colors.DARK_GREEN}>>> НАЖМИТЕ ENTER ДЛЯ ПРОДОЛЖЕНИЯ...{Colors.RESET}")

if __name__ == "__main__":
    main()