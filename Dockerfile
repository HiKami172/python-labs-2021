FROM python:3.8

ENV TARGET /usr/src/app/

WORKDIR "${TARGET}"

COPY . "${TARGET}"
RUN set -ex \ 
    pip3 install --no-cache-dir -r requirements.txt \
    && rm requirements.txt

CMD ["python3", "fibonacci.py"]
