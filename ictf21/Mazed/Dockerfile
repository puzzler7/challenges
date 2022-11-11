FROM python:slim as app

RUN pip install timeout-decorator --no-cache-dir

FROM redpwn/jail
COPY --from=app / /srv
COPY maze.py /srv/app/run
RUN chmod 755 /srv/app/run
COPY flag.txt /srv/app/flag.txt
RUN chmod 444 /srv/app/flag.txt

ENV JAIL_MEM 20M
ENV JAIL_TIME 100
ENV JAIL_CONNS_PER_IP 1
