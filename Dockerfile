FROM python:3.7
LABEL mainteiner = "blazej.szewczyk"
RUN python3 -m pip install requests
WORKDIR /app
ADD . /app
COPY api_book_call.py /app
CMD [ "python", "api_book_call.py"]