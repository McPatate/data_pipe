FROM python:3

WORKDIR /usr/src/webapp

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./webapp.py" ]

EXPOSE 8080
