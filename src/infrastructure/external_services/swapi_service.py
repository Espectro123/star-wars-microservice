import requests
import logging

logger = logging.getLogger('star_wars_logger')

class SWAPIService:
    """Returns an unsorted array of dicts representing the people
    External service.
    Gets all the star wars characters from the swapi API
    """
    def fetch_all_people(self):
        try:
            url = 'https://swapi.dev/api/people'
            all_people = []

            # Iterates over the pages until it gets all the characters (next = none)
            while url:
                response = requests.get(url)
                data = response.json()
                all_people.extend(data['results'])
                url = data['next']
            
        except requests.exceptions.Timeout:
            logger.error(f"Timeout occurred while requesting {url}")
            raise
        except requests.exceptions.HTTPError as http_err:
            logger.error(f"HTTP error occurred: {http_err}")
            raise
        except requests.exceptions.RequestException as req_err:
            logger.error(f"Request exception: {req_err}")
            raise
        except Exception as e:
            logger.exception("An unexpected error occurred in fetch_all_people.")
            raise
        
        return all_people