import logging
import os


def setup_logging():

    log_directory = 'logs'
    log_file = 'app.log'

    # Create folder if not exists
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s.%(msecs)03d - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(os.path.join(log_directory, log_file))  # Log a archivo
        ]
    )

    # Crea un logger para tu aplicación
    logger = logging.getLogger('fastapi_app')
