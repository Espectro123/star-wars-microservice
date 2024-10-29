import logging

logger = logging.getLogger('my_app_logger')

def fetch_and_sort_people(repository):
    logger.info("Fetching people data from repository.")
    people = repository.get_all_people()
    logger.info("Sorting people data.")
    # Sort people in ascending order [A->Z]
    sorted_people = sorted(people, key=lambda person: person.name)
    return sorted_people