@echo off
start cmd /k "F: && cd F:\Demo\vuejs\flask-vuejs-blog\back-end && conda activate demo && flask run"
start cmd /k "cd F: && cd F:\Demo\vuejs\flask-vuejs-blog\front-end && npm run dev"