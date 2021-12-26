from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов

DBHOST = env.str("DBHOST")  # Тоже str, но для айпи адреса хоста
PGUSER = env.str("PGUSER")
PGPASSWORD = env.str("PGPASSWORD")
DATABASE = env.str("DATABASE")

LANGUAGE_RU = 'ru'  # default
LANGUAGE_EN = 'en'
LANGUAGE_UZ = 'uz'