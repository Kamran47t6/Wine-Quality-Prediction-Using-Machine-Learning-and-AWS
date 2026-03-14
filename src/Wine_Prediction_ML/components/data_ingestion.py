from Wine_Prediction_ML import logger
from Wine_Prediction_ML.utils.common import get_size
from Wine_Prediction_ML.entity.config_entity import DataIngestionConfig
from pathlib import Path
import os
import zipfile
from urllib import request

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        # Check if it's a zip file or CSV file
        if self.config.local_data_file.endswith('.zip'):
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
        else:
            # For CSV files, just copy to the destination if not the same file
            import shutil
            destination = os.path.join(unzip_path, os.path.basename(self.config.local_data_file))
            # Check if source and destination are not the same file
            if os.path.abspath(self.config.local_data_file) != os.path.abspath(destination):
                shutil.copy(self.config.local_data_file, destination)
                logger.info(f"Copied {self.config.local_data_file} to {destination}")
            else:
                logger.info(f"File already in destination: {destination}")