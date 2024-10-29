import logging
from src.infrastructure.external_services.swapi_service import SWAPIService
from src.domain.person import Person

logger = logging.getLogger('star_wars_logger')

class SWAPIRepository:
    """Returns an array of People.

    Gets all the star wars characters(people) form the external service (SWAPI)
    """
    def __init__(self):
        self.service = SWAPIService()

    def get_all_people(self):
        try:
            data = self.service.fetch_all_people()
            people = [Person(**person_data) for person_data in data]
            return people
        except Exception as e:
            logger.exception("Failed to retrieve or parse people data.")
            raise