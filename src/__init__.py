import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

handler = RotatingFileHandler(
    'app.log',
    maxBytes=100000,  # 100 KB
    backupCount=3
)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.info("Logger initialized.")

app_logger = logging.getLogger(__name__)
app_logger.info("App logging ready.")
