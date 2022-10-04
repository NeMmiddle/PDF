from gtts import gTTS
import pdfplumber
from pathlib import Path



def pdf_to_mp3(file_path='.pdf', language='en'):
    if Path(file_path).is_file() and Path(file_path).suffix == ".pdf":

        print(f'[+] Source file(Исходный файл): {Path(file_path).name}')
        print('[+] Processing(Обработка)...')

        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        text = ''.join(pages)
        text = text.replace('\n', '')

        my_audio = gTTS(text=text, lang=language, slow=False)
        file_name = Path(file_path).stem
        my_audio.save(f'{file_name}.mp3')

        return f'[+] {file_name}.mp3 Successfully saved! {file_name}.mp3 Успешно сохранено!'


    else:
        return f'The file does not exist, check the path to the file!\nФайл не существует, проверьте путь к файлу!'


def main():
    file_path = input("\nEnter the full path to the file(Введите полный путь к файлу) \nExample(Пример): D:\My folder\From pdf to mp3\my file.pdf : ")
    language = input("Choose a language, for example 'en' or 'ru'\nВыберите язык, например 'en' или 'ru': ")
    print(pdf_to_mp3(file_path=file_path, language=language))


if __name__ == '__main__':
    main()

