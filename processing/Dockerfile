FROM python:3

WORKDIR /usr/src/processing

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./processing.py" ]
