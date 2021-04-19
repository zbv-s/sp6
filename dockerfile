FROM ubuntu
RUN apt update && apt install python3 -y
COPY sp6.py .
CMD python3 sp6.py
