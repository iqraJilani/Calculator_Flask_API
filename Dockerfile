# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster


#RUN export PYTHONPATH=/:/math_app:/math_app/src
#RUN echo $PYTHONPATH
WORKDIR ./math_app
COPY learning_demo/requirements.txt ./math_app
RUN pip install -r requirements.txt

ADD learning_demo ./math_app

ENV PYTHONPATH "${PYTHONPATH}:/math_app"



EXPOSE 5000
CMD ["python",  "api/app.py"]


