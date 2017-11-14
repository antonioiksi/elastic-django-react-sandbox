def map_field(index_name, field_name, mapping):
    return None


def filter_table_mapping(search_hits, mappings):
    """
    Add field name to mapped field
    :param search_hits: search['hits'] where search is json result for "_search" request to ES
    :param mappings: It's a map like {"indexname":{"tablename":[{"fields":...aka ES mapping }]}}
    :return:
    """

    for hit in search_hits:
        index_name = hit["_index"]
        source = hit["_source"]
        #for field_source in source:
    return None