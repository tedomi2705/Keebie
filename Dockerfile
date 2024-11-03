FROM node:18-alpine AS frontend
# copy yarn.lock and package.json
COPY ./frontend/package.json /app/frontend/package.json
COPY ./frontend/yarn.lock /app/frontend/yarn.lock
# set working directory
WORKDIR /app/frontend
# cache node modules
RUN --mount=type=cache,target=/root/.yarn YARN_CACHE_FOLDER=/root/.yarn yarn install
# add app
COPY ./frontend /app/frontend
RUN yarn build


FROM python:3.11-alpine
COPY ./backend/requirements.txt /app/backend/requirements.txt
WORKDIR /app/backend
RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt
COPY ./backend /app/backend
COPY --from=frontend /app/frontend/build /app/frontend/build
EXPOSE 8000
CMD ["python", "main.py"]

