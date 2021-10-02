class NoInputError(Exception):
    def __str__(self):
        return 'No search input entered'


class NoResultError(Exception):
    def __str__(self):
        return 'Cannot export an empty result'
