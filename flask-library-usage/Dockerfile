FROM python:alpine3.7
COPY companies_crud.py /app/
WORKDIR /app
RUN pip install flask
EXPOSE 5000
CMD python ./companies_crud.py