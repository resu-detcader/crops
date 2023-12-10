from hashlib import sha1

import bencoder


def get_source(torrent_data):
    try:
        return torrent_data[b"info"][b"source"]
    except KeyError:
        return None

def get_infohash(torrent_data):
    encoded_info = bencoder.bencode(torrent_data[b"info"])
    hash = sha1(encoded_info).hexdigest().upper()

    return hash

def get_new_hash(torrent_data, new_source):
    torrent_data[b"info"][b"source"] = new_source

    return get_infohash(torrent_data)


def get_torrent_data(filename):
    with open(filename, "rb") as f:
        data = bencoder.bdecode(f.read())

    return data


def save_torrent_data(filename, torrent_data):
    with open(filename, "wb") as f:
        f.write(bencoder.bencode(torrent_data))
