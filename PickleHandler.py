# @title Load and Handle Data

import pickle
import os
import logging

class PickleHandler:
    def __init__(self, folder_path, file_name, none_on_error:bool = True):
        self.folder_path = folder_path
        self.file_path = os.path.join(self.folder_path, file_name)
        self.file_log_path = os.path.join(self.folder_path, f'''log_{file_name.replace('.','_')}.log''')
        self._error_return_None = none_on_error
        
        # Configure logging
        # Create instance-specific logger
        self.file_logger = logging.getLogger(f'PickleHandler_{file_name}')
        self.file_logger.setLevel(logging.INFO)
        
        # Create a file handler
        file_handler = logging.FileHandler(self.file_log_path)

        # Create a formatter and set the formatter for the handler
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        # Add the handler to the logger
        self.file_logger.addHandler(file_handler)

    def save(self, data):
        with open(self.file_path, 'wb') as file:
            pickle.dump(data, file)
        print(f'Data saved to {self.file_path}')
        self.file_logger.info(f'Data saved to {self.file_path}')

    def load(self):
        try:
            with open(self.file_path, 'rb') as file:
                data = pickle.load(file)
            print(f'Data loaded from {self.file_path}')
            self.file_logger.info(f'Data loaded from {self.file_path}')
            return data
            
        except FileNotFoundError:
            print(f'File not found at {self.file_path}. Returning None.')
            self.file_logger.error(f'File not found at {self.file_path}. Returned None')
            if self._error_return_None: return None
            raise FileNotFoundError
            
        except pickle.UnpicklingError:
            print(f'Error loading data [Unpickling] from {self.file_path}. Returning None.')
            self.file_logger.error(f'Error loading data [Unpickling] from {self.file_path}. Returning None.')
            if self._error_return_None: return None
            raise

    def load_logs(self):
        if not os.path.exists(self.file_log_path):
            print(f'Log file not found at {self.file_log_path}.')
            return []
    
        with open(self.file_log_path, 'r') as file:
            logs = file.readlines()
            
        return logs
            
    def print_logs(self):
        logs = self.load_logs()
        for log in logs:
            print(log.strip())
