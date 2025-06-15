import random
import os
import sys
import time
from collections import OrderedDict

# Конфигурация
AUTHOR_TAG = "@Pinaplast42"
VERSION = "C.U.Gen v7.2"
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
            'A1B2C3D4E5F6', '4B4C4F434B4C',
            '123456789ABC', 'DEADBEEF1234',
            'A5B4C3D2E1F0', '0F1E2D3C4B5A'
        ]))

    @staticmethod
    def transport_dictionary():
        """Возвращает полный словарь транспортных ключей"""
        keys = [
            'A0A1A2A3A4A5', 'A82607B01C0D', '2AA05ED1856F', '73068F118C13',
            'FBC2793D540B', 'AE3D65A3DAD4', 'A73F5DC1D333', '69A32F1C2F19',
            '9BECDF3D9273', '08B386463229', 'CD4C61C26E3D', '0E8F64340BA4',
            '6B02733BB6EC', '403D706BA880', 'C11F4597EFB5', '0DB520C78C1C',
            '3EBCE0925B2F', '16A27AF45407', 'ABA208516740', 'CD64E567ABCD',
            '764CD061F1E6', '1CC219E9FEC1', '2FE3CB83EA43', '07894FFEC1D6',
            '04C297B91308', '7A38E3511A38', '7545DF809202', '5125974CD391',
            'FBF225DC5D58', '2910989B6880', 'EAAC88E5DC99', '2B7F3253FAC5',
            'D3A297DC2698', '0F1C63013DBA', 'E35173494A81', '6B8BD9860763',
            'F8493407799D', '5EFBAECEF46B', '31C7610DE3B0', '4ACEC1205D75',
            '7038CD25C408', 'B39D19A280DF', '70D901648CB9', '73E5B9D9D3A4',
            '372CC880F216', '9868925175BA', 'CE26ECB95252', '8F79C4FD8A01',
            'A74332F74994', 'B90DE525CEB6', 'FBA88F109B32', 'EFCB0E689DB3',
            'C8454C154CB5', 'AB16584C972A', 'ECF751084A80', 'D3EAFB5DF46D',
            '7DE02A7F6025', '2735FC181807', 'BF23A53C1F63', '2ABA9519F574',
            'CB9A1F2D7368', '84FD7F7A12B6', 'C7C0ADB3284F', '186D8C4B93F9',
            '9F131D8C2057', '3A4BBA8ADAF0', '67362D90F973', '8765B17968A2',
            '6202A38F69E2', '40EAD80721CE', '100533B89331', '0DB5E6523F7C',
            '653A87594079', '51119DAE5216', 'D8A274B2E026'
        ]
        return list(OrderedDict.fromkeys(keys))  # Удаление дубликатов

    @staticmethod
    def random_keys(count, mode=0):
        keys = set()
        print(f"\n{Colors.DARK_GREEN}>>> ЗАПУСК СЛУЧАЙНОЙ ГЕНЕРАЦИИ...")
        
        # Если режим 1, подготовим шаблоны (база + транспорт)
        templates = []
        if mode == 1:
            templates = KeyGenerator.base_keys() + KeyGenerator.transport_dictionary()
        
        start_time = time.time()
        last_update = start_time
        generated = 0
        
        while len(keys) < count:
            if mode == 0:
                # Режим 0: полностью случайный
                key = ''.join(random.choices('0123456789ABCDEF', k=12))
            elif mode == 1 and templates:
                # Режим 1: частичная замена (8 символов) на основе шаблона
                base = random.choice(templates)
                positions = random.sample(range(12), 8)  # 8 случайных позиций
                new_key = list(base)
                for pos in positions:
                    new_key[pos] = random.choice('0123456789ABCDEF')
                key = ''.join(new_key)
            else:
                # Резервный вариант
                key = ''.join(random.choices('0123456789ABCDEF', k=12))
            
            if key not in keys:
                keys.add(key)
                generated += 1
                current_time = time.time()
                
                # Обновление прогресса каждые 0.5 секунд
                if current_time - last_update > 0.5 or generated == count:
                    elapsed = current_time - start_time
                    speed = generated / elapsed if elapsed > 0 else 0
                    print(f"{Colors.GREEN}[~] Прогресс: {generated}/{count} | "
                          f"Скорость: {speed:.1f} keys/sec | "
                          f"Время: {elapsed:.1f}s {Colors.YELLOW}", end='\r')
                    last_update = current_time
        
        print(f"\n{Colors.GREEN}[✓] ГЕНЕРАЦИЯ УСПЕШНО ЗАВЕРШЕНА")
        return list(keys)

def menu():
    while True:
        show_banner()
        print(f"{Colors.DARK_GREEN}╔════════════════════════════════════════════╗")
        print(f"{Colors.GREEN}║ {Colors.YELLOW}1.{Colors.GREEN} БАЗОВЫЕ КЛЮЧИ               {Colors.DARK_GREEN}[STATUS: ONLINE]{Colors.GREEN} ║")
        print(f"{Colors.GREEN}║ {Colors.YELLOW}2.{Colors.GREEN} ТРАНСПОРТНЫЙ СЛОВАРЬ       {Colors.DARK_GREEN}[STATUS: ONLINE]{Colors.GREEN} ║")
        print(f"{Colors.GREEN}║ {Colors.YELLOW}3.{Colors.GREEN} СЛУЧАЙНАЯ ГЕНЕРАЦИЯ        {Colors.DARK_GREEN}[STATUS: ONLINE]{Colors.GREEN} ║")
        print(f"{Colors.GREEN}║ {Colors.YELLOW}0.{Colors.RED} ВЫХОД                      {Colors.DARK_GREEN}[STATUS: STANDBY]{Colors.GREEN} ║")
        print(f"{Colors.DARK_GREEN}╚════════════════════════════════════════════╝")
        
        choice = input(f"\n{Colors.GREEN}>>> ВВЕДИТЕ КОМАНДУ: {Colors.YELLOW}")
        if choice in {'0','1','2','3'}:
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
                if i % 100 == 0 or i == len(unique_new):
                    progress = i / len(unique_new) * 100
                    print(f"{Colors.GREEN}[~] ЗАПИСАНО: {i}/{len(unique_new)} "
                          f"({progress:.1f}%) {Colors.DARK_GREEN}| "
                          f"ДУБЛИКАТОВ: {duplicates}", end='\r')
        
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
                print(f"\n{Colors.GREEN}[+] БАЗОВЫЕ КЛЮЧИ ЗАГРУЖЕНЫ: {Colors.YELLOW}{len(keys)}")
                print(f"{Colors.DARK_GREEN}>>> СПИСОК КЛЮЧЕЙ:")
                for key in keys:
                    print(f"{Colors.GREEN}• {Colors.YELLOW}{key}")
                
            elif choice == '2':
                keys = KeyGenerator.transport_dictionary()
                print(f"\n{Colors.GREEN}[+] ТРАНСПОРТНЫЙ СЛОВАРЬ ЗАГРУЖЕН: {Colors.YELLOW}{len(keys)} ключей")
                print(f"{Colors.DARK_GREEN}>>> ПЕРВЫЕ 10 КЛЮЧЕЙ ИЗ СЛОВАРЯ:")
                for key in keys[:10]:
                    print(f"{Colors.GREEN}• {Colors.YELLOW}{key}")
                print(f"{Colors.DARK_GREEN}>>> ПОСЛЕДНИЕ 10 КЛЮЧЕЙ ИЗ СЛОВАРЯ:")
                for key in keys[-10:]:
                    print(f"{Colors.GREEN}• {Colors.YELLOW}{key}")
                print(f"{Colors.DARK_GREEN}>>> ОБЩЕЕ КОЛИЧЕСТВО: {Colors.YELLOW}{len(keys)} ключей")
                
            elif choice == '3':
                try:
                    count = int(input(f"\n{Colors.GREEN}>>> ВВЕДИТЕ КОЛИЧЕСТВО: {Colors.YELLOW}"))
                    count = max(1, min(count, 1000000))  # Ограничение до 1 млн
                    
                    print(f"{Colors.GREEN}>>> РЕЖИМ ГЕНЕРАЦИИ:")
                    print(f"{Colors.GREEN}    {Colors.YELLOW}1.{Colors.GREEN} Полная случайность (быстрее)")
                    print(f"{Colors.GREEN}    {Colors.YELLOW}2.{Colors.GREEN} Частичная замена (разнообразнее)")
                    mode_choice = input(f"{Colors.GREEN}>>> ВЫБЕРИТЕ РЕЖИМ (1): {Colors.YELLOW}") or '1'
                    mode = 0 if mode_choice == '1' else 1
                    
                    keys = KeyGenerator.random_keys(count, mode)
                    print(f"\n{Colors.GREEN}[✓] СГЕНЕРИРОВАНО КЛЮЧЕЙ: {Colors.YELLOW}{len(keys)}")
                except ValueError:
                    print(f"{Colors.RED}[✗] НЕВЕРНЫЙ ВВОД! ВВЕДИТЕ ЧИСЛО")
                    time.sleep(1)
                    continue
            
            if keys:
                if input(f"\n{Colors.GREEN}>>> ЭКСПОРТИРОВАТЬ РЕЗУЛЬТАТ? (Y/n): {Colors.YELLOW}").lower() != 'n':
                    filename = input(f"{Colors.GREEN}>>> ИМЯ ФАЙЛА ({DEFAULT_FILENAME}): {Colors.YELLOW}") or DEFAULT_FILENAME
                    if not filename.endswith('.dic'):
                        filename += '.dic'
                    save_keys(keys, filename)
            
        except Exception as e:
            print(f"\n{Colors.RED}[✗] СИСТЕМНАЯ ОШИБКА: {e}")
        
        input(f"\n{Colors.DARK_GREEN}>>> НАЖМИТЕ ENTER ДЛЯ ПРОДОЛЖЕНИЯ...{Colors.RESET}")

if __name__ == "__main__":
    main()