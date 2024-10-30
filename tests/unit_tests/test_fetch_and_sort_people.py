import pytest
from unittest.mock import MagicMock
from src.use_cases.fetch_and_sort_people import fetch_and_sort_people
from src.domain.person import Person

def test_fetch_and_sort_people():

    # Create a mock repository
    mock_repository = MagicMock()

    # Mock data returned by the repository
    unsorted_people = [
        Person(name='Leia Organa', height='150', mass='49'),
        Person(name='Luke Skywalker', height='172', mass='77'),
        Person(name='Han Solo', height='180', mass='80'),
    ]

    # Expected sorted list by name
    expected_sorted_names = ['Han Solo', 'Leia Organa', 'Luke Skywalker']

    # The repository's get_all_people method returns unsorted_people
    mock_repository.get_all_people.return_value = unsorted_people

    # Call the use case function with the mock repository
    sorted_people = fetch_and_sort_people(mock_repository)

    # Extract names from the sorted list
    sorted_names = [person.name for person in sorted_people]

    # Check if the names are sorted as expected
    assert sorted_names == expected_sorted_names
