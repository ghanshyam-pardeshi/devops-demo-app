FROM python:3.9
WORKDIR C:\Users\ghanshyam.pardeshi\devops-demo-app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]