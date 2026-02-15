import os
import django
import argparse


parser = argparse.ArgumentParser(description='Конфигурация программы через аргументы командной строки.')
parser.add_argument('--db-host', help='Хост базы данных')
parser.add_argument('--db-port', help='Порт базы данных')
parser.add_argument('--db-name', help='Имя базы данных')
parser.add_argument('--db-user', help='Пользователь базы данных')
parser.add_argument('--db-password', help='Пароль базы данных')
parser.add_argument('--db-secret-key', help='Секретный ключ Django')

args = parser.parse_args()
if args.db_host:
    os.environ['DB_HOST'] = args.db_host
if args.db_port:
    os.environ['DB_PORT'] = args.db_port
if args.db_name:
    os.environ['DB_NAME'] = args.db_name
if args.db_user:
    os.environ['DB_USER'] = args.db_user
if args.db_password:
    os.environ['DB_PASSWORD'] = args.db_password
if args.db_secret_key:
    os.environ['DB_SECRET_KEY'] = args.db_secret_key


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()


from datacenter.models import Passcard


if __name__ == '__main__':
    passcards = Passcard.objects.all()
    active_passcards = Passcard.objects.filter(is_active=True)

    print('Всего пропусков', Passcard.objects.count())
    print('Активных пропусков', len(active_passcards))