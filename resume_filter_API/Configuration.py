import configparser

config = configparser.ConfigParser()

config.read('data/config.ini')

# Access variables
host_ip = config.get('ENVIRONMENT', 'HOST_IP')
host_port = int(config.get('ENVIRONMENT', 'HOST_PORT'))

##accessing database connection
mysql_user = config.get('DATABASE', 'MYSQL_USER')
mysql_password = config.get('DATABASE', 'MYSQL_PASSWORD')
mysql_server = config.get('DATABASE', 'MYSQL_SERVER')
mysql_port = int(config.get('DATABASE', 'MYSQL_PORT'))
mysql_database = config.get('DATABASE', 'MYSQL_DB')

temporary_file_path = config.get('FILE', 'TEMPORARY_FILE')

google_api_key = config.get('GOOGLE', 'GOOGLE_API_KEY')
google_prompt = config.get('GOOGLE', 'PROMPT')
