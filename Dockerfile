FROM python
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY *.py .
CMD ["python", "hello.py"]