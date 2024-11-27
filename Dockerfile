FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH="/app"

#add python code
EXPOSE 8001
CMD ["uvicorn", "app.main:app", "--host=0.0.0.0" , "--reload" , "--port", "8001"]

