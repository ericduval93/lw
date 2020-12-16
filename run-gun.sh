#!/bin/bash

pipenv run gunicorn wgsi:app
