#!/bin/env python

import xmlrpc.client
from pyrtorrent.torrent import Torrent

class Rtorrent(object):
    def __init__(self, url):
        self.url = url

    def attribute(self, attribute, *args, is_bool=False):
        """
        Return attribute from rTorrent xmlrpc
        """
        with xmlrpc.client.ServerProxy(self.url) as client:
            result = getattr(client, attribute)(*args)
            if is_bool:
                return result == 1
            else:
                return result

    def all_torrents(self):
        """
        Fetch all torrents from rTorrent
        """
        with xmlrpc.client.ServerProxy(self.url) as client:
            return [Torrent(self, x) for x in client.download_list()]

    def add_torrent(self, torrent):
        """
        Add a torrent
        """
        self.attribute('load_start', torrent, is_bool=False)
