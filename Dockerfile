FROM node:18-alpine AS frontend
COPY . /app
WORKDIR /app/frontend
RUN yarn
RUN yarn build


FROM python:3.11-alpine
COPY . /app
WORKDIR /app/backend
RUN pip install -r requirements.txt
EXPOSE 8000
COPY --from=frontend /app/frontend/build /app/frontend/build
CMD ["python", "main.py"]

