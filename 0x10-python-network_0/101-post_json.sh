#!/bin/bash
# Bash script that sends a JSON POST request to a URL 
curl -sd "$2" -X POST "$1"
