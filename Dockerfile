FROM python:3.12-slim
#AS build
    # why that version? my host machine is 3.12.3 python version

WORKDIR /app
# COPY requirements.txt ./

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# COPY backend.py readme.md ./app/

EXPOSE 5000

ENTRYPOINT [ "python", "backend.py" ]

# prepare for mutlti-stage:
# FROM openjdk:8-jre-slim
# WORKDIR /app/target
# COPY --from=build /app/target .
# copy only the built JAR file from the previous stage
