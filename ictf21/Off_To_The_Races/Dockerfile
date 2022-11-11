FROM redpwn/jail
COPY --from=python / /srv
COPY races.py /srv/app/run
RUN chmod 755 /srv/app/run
COPY flag.txt /srv/app/flag.txt
RUN chmod 444 /srv/app/flag.txt
COPY hook.sh /jail

ENV JAIL_MEM 20M
ENV JAIL_TIME 100
ENV JAIL_CONNECTIONS_PER_IP 2
