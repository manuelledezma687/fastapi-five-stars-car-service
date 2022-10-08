#!/bin/bash

source venv/bin/activate
pip install -r requierements.txt

uvicorn main:app --reload
