FROM python:3.12-slim
EXPOSE 80
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
CMD ["flask", "run", "--host", "0.0.0.0"]


# docker build -t samir3112/test-env:v1 .
# docker run -e "change_env_var=DevOps Team" -d -p 80:80 samir3112/test-env:v1
# curl http://localhost:80/ (access application on host port which is mapped to container)

# docker run -e "change_env_var=Python DevOps Team" -d -p 81:80 samir3112/test-env:v1
# http://localhost:81/

# find env vars on running container
# docker inspect <container_id>

