"""
Abstractions for Data Repository
"""

from abc import ABC, abstractmethod


class DataRepositoryAPI(ABC):
    """ Abstaract class for research data repository APIs"""
    
    @abstractmethod
    def create_item(self, **argv):
        """
        Creates a new item in the user account attached to a research data repository. 
        The type of item(s) to be created depends on the iplementation.
        """
        pass

    @abstractmethod
    def get_item(self, **argv):
        """
        Retrieves one or more items in the user account attached to the reserch data repository.
        """
        pass

    @abstractmethod
    def update_item(self, **argv):
        """
        Updates metadata of an existing item in the user account attached to the research data
        repository.
        """
        pass

    @abstractmethod
    def delete_item(self, **argv):
        """
        deletes an existing item in the user account attached to the research data
        repository.
        """
