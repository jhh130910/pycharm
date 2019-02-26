class SamtoolsError(Exception):
    '''exception raised in case of an error incurred in the samtools
    library.'''

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)