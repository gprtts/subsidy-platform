#!/bin/bash
cd /opt/subsidy-platform
source venv/bin/activate
python -m parsers.run_all >> logs/parser.log 2>&1
