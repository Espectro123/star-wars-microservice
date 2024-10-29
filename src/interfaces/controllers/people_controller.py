import logging
from src.use_cases.get_and_sort_people import fetch_and_sort_people
from src.interfaces.serializers.person_serializer import PersonSerializer
from src.interfaces.repositories.swapi_repository import SWAPIRepository

logger = logging.getLogger('star_wars_logger')

# Fetch the data and serialized it
def get_sorted_people():
    try:
        repository = SWAPIRepository()
        sorted_people = fetch_and_sort_people(repository)
        serialized_data = PersonSerializer.serialize(sorted_people)
        return serialized_data
    except Exception as e:
        logger.exception("An error occurred in get_sorted_people.")
        raise
