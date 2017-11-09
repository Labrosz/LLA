#!/bin/bash

# Bash colors for outputs
RED='\033[0;31m'
GRN='\033[0;32m'
ORG='\033[0;33m'
NC='\033[0m'

echo "Running Latex Language Annotator..."
python lla.py
# : $(pip install --upgrade google-cloud-translate)
# if [ $? -eq 0 ]; then
#     echo -e "${GRN}API up-to-date.${NC}"
#     export GOOGLE_APPLICATION_CREDENTIALS="/home/sorbal/Google_APIs/lla-7a5f87510fb5.json"
#     python lla.py
# else
#     echo -e "${RED}An error accured while installing Google Translate API.Please run the command bellow manually:${NC}"
#     echo -e "${ORG}pip install --upgrade google-cloud-translate${NC}"
# fi
