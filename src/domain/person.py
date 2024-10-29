import logging

logger = logging.getLogger('star_wars_logger')


class Person:
    """
    Dynamic Person class definition.
    The attributes are set by the keys of the dictionary passed to it.
    """
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key == 'name':
                logger.info(f"Person {value} created")
            setattr(self, key, value)
