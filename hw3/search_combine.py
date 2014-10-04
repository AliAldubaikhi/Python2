import data_load
import searcher
import indexer


def searchForContent():
    data_load.get_traversal_data()
    search_data = indexer.read_data()
    searcher.search(search_data)


searchForContent()
