@echo off

set NETWORK_NAME=video-lib-network

docker run -itd  --network %NETWORK_NAME% -p 5000:5000 my-video-lib-api
