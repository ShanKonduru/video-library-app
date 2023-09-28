@echo off

set NETWORK_NAME=video-lib-network

docker run -itd  --network %NETWORK_NAME% -p 8888:8888 my-video-lib-app
