""" Search fanfiction.net """

root = 'https://www.fanfiction.net'

section = '/book/Harry-Potter'
query_template = '/?&%s'

_query_gen = {
        'srt': 0,   # sortid
        'g1': 0,    # genreid1
        'g2': 0,    # genreid2
        '_g1': 0,   # _genreid1
        'lan': 0,   # languageid
        'r': 0,     # censorid
        'len': 0,   # length
        't': 0,     # timerange
        's': 0,     # statusid
        'c1': 0,    # characterid1
        'c2': 0,    # characterid2
        'c3': 0,    # characterid3
        'c4': 0,    # characterid4
        '_c1': 0,   # _characterid1
        '_c2': 0,   # _characterid2
        'v1': 0,    # verseid1
        '_v1': 0    # _verseid1
}

def _generate_query_path():
    queries = []
    for q, val in _query_gen:
        queries.append('%s=%s' % (q, str(val)))
    return root + section + query_template % ('&'.join(queries))

