"""Implementation of Data Repository for 4TU Reasearch Data"""


from jupyterfair.core.data_repository_api import DataRepositoryAPI
from jupyterfair.core.connection import Connection
from jupyterfair.core.item import Item


class FourTuAPI(DataRepositoryAPI):

    def __init__(self, connection) -> None:
        
        if isinstance(connection, Connection):
            self.connection = connection
        else:
            raise TypeError("connection attribute must be an instace of the Connection class")
        return None
        

    def create_item(self, item:Item)-> dict:
        """Creates an article in a 4TU.ResearchData account
        
        params:
            item: metadata required for creating an article. An instance of the Item class
        returns: response as JSON-like
        """

        if not isinstance(item, Item):
            raise TypeError("payload must be an instance of the Item class")

        request_url= self.connection.root_url + '/articles'
        response=self.connection.post(request=request_url, payload=item())

        return response.json()


    def get_item(self) -> dict:
        """Lists articles in the user account
        
        returns:
            JSON-like array with zero or more articles
        """
        request_url= self.connection.root_url + '/articles'
        response=self.connection.get(request=request_url)

        return response.json()


    def update_item(self, item:Item) -> None:
        """
        Updates metadata of an existing item in the user account attached to the research data
        repository.

        params:
            item: item to be updated.
            payload: changes to be made to the metadata of an item
        
        """
        if not isinstance(item, Item):
            raise TypeError("payload must be an instance of the Item class")

        pass


    def delete_item(self, item) -> None:
        """
        Deletes an existing item in the user acccount.
        params:
        """
        pass


if __name__ == '__main__':
    pass


   