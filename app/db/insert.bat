@echo off

curl -X POST -H "Content-Type: application/json" -d "{
    \"title\": \" google page \",
    \"url\": \"http:\\google.com\"
}" http://localhost:5555/insert
