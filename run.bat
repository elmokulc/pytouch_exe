@echo off
call xhost +
call docker-compose up --build -d app