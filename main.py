import threading
import os


unlilar = 'aeiouAEIOU'


def count_unlilar(fayllar_unlilar):
    try:
        
        with open(fayllar_unlilar, 'r', encoding='utf-8') as file_unlilar_1:
            txt = file_unlilar_1.read()
        count = sum(1 for char in txt if char in unlilar)
        print(f"{fayllar_unlilar}: {count} unlilar")
    except Exception as f:
        print(f"Failed to read {fayllar_unlilar}: {f}")


def main():
    file_dir = os.path.dirname(os.path.abspath(__file__))

    
    file_txt = [f for f in os.listdir(file_dir) if f.endswith('.txt')]


    cheaker = [threading.Thread(target=count_unlilar, args=(os.path.join(file_dir, f),)) for f in file_txt]
    

    for thread in cheaker:
        thread.start()
    
    for thread in cheaker:
        thread.join()


if __name__ == "__main__":
    main()