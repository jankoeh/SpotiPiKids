#!/usr/bin/env python3
# -*- coding: utf-8 -*-

SPOTIFY_CLI = "/home/pi/.local/bin/spotify"
DEVICE = '"raspotify (rasppi4)"'


def spotify_cmd( cmd ):
    """
    Execute spotify command using SPOTIFY_CLI
    """
    from os import system
    ret = system("{} {}".format(SPOTIFY_CLI, cmd))
    #if ret != 0:
    #    print( "Command not successfull: ", cmd )
    return ret


def set_default_device():
    """
    Set device according to DEVICE variable
    """
    return spotify_cmd("devices -s {}".format(DEVICE))