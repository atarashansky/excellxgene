import logging
import sys
from backend.common.utils.utils import import_plugins

__version__ = "2.9.6"
display_version = "cellxgene v" + __version__

try:
    import_plugins("backend.server.plugins")
except Exception as e:
    # Make sure to exit in this case, as the server may not be configured as expected.
    logging.critical(f"Error in import_plugins: {str(e)}")
    sys.exit(1)
