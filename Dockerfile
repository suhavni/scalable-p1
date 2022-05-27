# BUILD STAGE
FROM python:3.9-alpine AS build

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR usr/src/app

COPY ./backend /usr/src/app/
RUN apk add tzdata
RUN pip install --upgrade pip && pip install -r requirements.txt

# DEPLOYMENT STAGE
FROM python:3.9-alpine AS deployment

COPY --from=build usr/src/app/ usr/src/app
COPY --from=build /usr/local/lib/python3.9 /usr/local/lib/python3.9
COPY --from=build /usr/local/bin/gunicorn /usr/local/bin/gunicorn

COPY --from=build /usr/share/zoneinfo/Asia/Bangkok /etc/localtime

WORKDIR /usr/src/app

EXPOSE 5000

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "--threads", "4", "src.wsgi:app"]