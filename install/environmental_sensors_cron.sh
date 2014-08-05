#!/usr/bin/env bash

export AUTH_TOKEN=ChangeThisAfterInstall
export TWITTER_CONSUMER_KEY=ReplaceThis
export TWITTER_CONSUMER_SECRET=ReplaceThis
export TWITTER_ACCESS_TOKEN_KEY=ReplaceThis
export TWITTER_ACCESS_TOKEN_SECRET=ReplaceThis

cd /home/pi/Pi-Red-Dwarf && python environmental_sensors.py
