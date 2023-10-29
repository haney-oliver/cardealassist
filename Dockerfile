FROM python:3.10.5
FROM --platform=linux/amd64 python:3.10.5 as prod
WORKDIR /project

COPY . .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080", "--root-path", "/api-cardealassist"]
