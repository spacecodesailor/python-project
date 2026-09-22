FROM python:3.9-slim 
WORKDIR /app 
COPY simple.py . 
EXPOSE 8080 
CMD ["python", "simple.py"] 
