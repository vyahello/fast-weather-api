FROM vyahello/fwa-base:0.1.0
LABEL version=0.1.0 \
      metadata="The main image for fast weather api application" \
      maintainer="Volodymyr Yahello <vyahello@gmail.com>"
ARG VERSION
ENV CODE_DIR="/app" \
    IMAGE_REPO="vyahello/fwa" \
    SERVER_PORT=4444 \
    IMAGE_VERSION=${VERSION}
WORKDIR ${CODE_DIR}
COPY weather weather
COPY requirements.txt settings.json docker/entry.sh ./
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -v requirements.txt
ENTRYPOINT ["/app/entry.sh"]
