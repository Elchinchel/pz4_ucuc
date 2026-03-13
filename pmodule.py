import json
import traceback
import obrabotka


NO_DATA = object()


def request_data():
    while True:
        try:
            v = input('Введите ДАННЫЕ в формате ЖСОН: ')
        except EOFError:
            print('Стдввод ЗАКОНЧИЛСЯ.')
            return NO_DATA
        try:
            return json.loads(v)
        except Exception:
            traceback.print_exc()
            print('Произошла ОШИБКА. Попробуйте еще раз.')


def main():
    data = request_data()
    if data is NO_DATA:
        return
    obrabotka.do(data)


if __name__ == '__main__':
    main()
