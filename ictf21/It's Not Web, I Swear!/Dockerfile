FROM ubuntu

RUN useradd -m ctf

RUN mkdir -p /chal
WORKDIR /chal
COPY ./the_real_flag.txt /chal/the_real_flag.txt
COPY ./server /chal/server
COPY ./www /chal/www

RUN chown -R root:ctf /chal && \
    chmod -R 750 /chal /chal/server && \
    chmod -R 740 /chal/the_real_flag.txt /chal/www/* && \
    rm -rf /home/

USER ctf
WORKDIR /chal
CMD ./server 42042 > /dev/null

EXPOSE 5000

# deploy note: 
# docker exec -tid itsnotwebiswear_deployment_1 ./server 5000 > /dev/null
