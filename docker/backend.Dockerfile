FROM python:3

WORKDIR /usr/src/app

COPY backend/requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ /usr/src/app/

CMD [ "fastapi", "dev", "--port", "80", "--host", "0.0.0.0", "src/main.py" ]