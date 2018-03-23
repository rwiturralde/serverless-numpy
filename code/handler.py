from __future__ import print_function
import os
import sys
import logging
sys.path.append('lib')
import numpy


# get logger level from function env var and create logger
log_level = os.getenv('LOG_LEVEL', 'INFO')
numeric_level = getattr(logging, log_level.upper(), None)
if not isinstance(numeric_level, int):
    raise ValueError('Invalid log level: %s' % log_level)

logger = logging.getLogger(__name__)
logger.setLevel(numeric_level)


def validate_event(event):
    """
    Validate the contents of the event passed to the this function.

    :param event: Dict event object passed to this function
    :return: None
    :raises AttributeError: The provided method doesn't exist in NumPy
    :raises Exception: Missing required parameters in function event
    """
    # Check that we were passed the required arguments
    if 'method' in event and 'arguments' in event:
        numpy_method_name = event.get('method')

    # Check that the NumPy method is valid
        if hasattr(numpy, numpy_method_name) and callable(getattr(numpy, numpy_method_name)):
            return
        else:
            error_message = "Invalid NumPy method: {}".format(numpy_method_name)
            logger.error(error_message)
            raise AttributeError(error_message)
    else:
        error_message = "Missing required parameter(s). Event must contain fields for \'method\' and \'arguments\'"
        logger.error(error_message)
        raise TypeError(error_message)


def lambda_handler(event, context):
    """
    Delegate method and arguments to NumPy

    :param event: Dict of details of event that triggered this function.
            Should contain two entries:
                event.method - NumPy method to invoke
                event.arguments - Array of ordered arguments to pass to the  method
    :return: Dict containing the NumPy result after passing the arguments to the method.
    :raises Exception:
    """

    # Check that we were passed the required arguments
    validate_event(event)

    try:
        numpy_method_name = event.get('method')
        numpy_argument_array = event.get('arguments')

        logger.info("Handing call to the NumPy {} method with arguments: {}".format(numpy_method_name, numpy_argument_array))
        result = getattr(numpy, numpy_method_name)(*numpy_argument_array)
        logger.info("Result from NumPy is {}".format(result))
        return {'result': result}
    except:
        error_message = "Unexpected error: {}".format(str(sys.exc_info()))
        logger.error(error_message)
        raise Exception(error_message)

