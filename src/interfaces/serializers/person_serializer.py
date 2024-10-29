class PersonSerializer:
    """
    Need it to present the data however we want.
    In this case it doesn't follow any particular order.
    """
    @staticmethod
    def serialize(people):
        return [vars(person) for person in people]