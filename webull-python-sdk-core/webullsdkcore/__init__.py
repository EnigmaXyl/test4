__version__ = "0.1.6"

import logging

class NullHandler(logging.Handler):
    def emit(self, record):
        """
        null handler
        """
        pass
    
logging.getLogger('webullsdkcore').addHandler(NullHandler())
