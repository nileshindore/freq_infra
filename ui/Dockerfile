FROM python:3

WORKDIR /usr/src/app
COPY requirement.txt .
RUN pip install --no-cache-dir -r requirement.txt
COPY . .
EXPOSE 5000
RUN chmod 700 start.sh
CMD [ "./start.sh" ]