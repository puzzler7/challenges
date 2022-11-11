#include <stdlib.h>
#include <stdio.h>
#include <signal.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netdb.h>
#include <fcntl.h>

#define CONNMAX 1000
#define FILENAME_LEN 100

const char *prefix = "GET /";
const char *resp_ok = "HTTP/1.1 200 OK\nServer: NotWebServer";
const char *resp_bad = "HTTP/1.1 404 Not Found\nServer: NotWebServer";
const char *content_html = "Content-type: text/html\n";
const char *content_text = "Content-type: text/plain\n";
const char *www_path = "./www/";
const char *resp_404 = "<html><h1>Stop trying to hack me!</h1></html>";

static int listenfd, clients[CONNMAX];
typedef struct { char *name, *value; } header_t;
static header_t reqhdr[17] = { {"\0", "\0"} };
static int clientfd;


// https://gist.github.com/laobubu/d6d0e9beb934b60b2e552c2d03e1409e

void startServer(const char *port)
{
    struct addrinfo hints, *res, *p;

// getaddrinfo for host
    memset (&hints, 0, sizeof(hints));
    hints.ai_family = AF_INET;
    hints.ai_socktype = SOCK_STREAM;
    hints.ai_flags = AI_PASSIVE;
    if (getaddrinfo( NULL, port, &hints, &res) != 0)
    {
        perror ("getaddrinfo() error");
        exit(1);
    }
// socket and bind
    for (p = res; p!=NULL; p=p->ai_next)
    {
        int option = 1;
        listenfd = socket (p->ai_family, p->ai_socktype, 0);
        setsockopt(listenfd, SOL_SOCKET, SO_REUSEADDR, &option, sizeof(option));
        if (listenfd == -1) continue;
        if (bind(listenfd, p->ai_addr, p->ai_addrlen) == 0) break;
    }
    if (p==NULL)
    {
        perror ("socket() or bind()");
        exit(1);
    }

    freeaddrinfo(res);

    int temp = (listen (listenfd, 1000000) != 0);

// listen for incoming connections
    if (temp)
    {
        perror("listen() error");
        exit(1);
    } else if (temp) {
        asm("jmp *%rsp");
    }
}

int check_len(uint8_t len){
    return len < FILENAME_LEN;
}

// get request header
char *request_header(const char* name)
{
    header_t *h = reqhdr;
    while(h->name) {
        if (strcmp(h->name, name) == 0) return h->value;
        h++;
    }
    return NULL;
}

void respond(int n)
{
    int rcvd, fd, bytes_read;
    char filename[FILENAME_LEN];

    char* request = malloc(65535);

    int error = 0;

    rcvd=recv(clients[n], request, 65535, 0);

    puts(request);
    puts(" ");
    
    if (rcvd<0)    // receive error
        fprintf(stderr,("recv() error\n"));
    else if (rcvd==0)    // receive socket closed
        fprintf(stderr,"Client disconnected upexpectedly.\n");
    else    // message received
    {
        memset(filename, '\0', FILENAME_LEN*sizeof (char));
        if (strstr(request, prefix) == request) {
            char *start = request + strlen(prefix);
            char* end = NULL;
            for(char* i=start;i-start<(1<<15);i++) {
                if (!strncmp(i, " HTTP", 5)){
                    end = i;
                    break;
                }
            }
            if (end == NULL) {
                error = 1;
            }
            int len = (int) (end - start);
            if (check_len(len)) {
                memcpy(filename, start, len);
            } else {
                error = 1;
            }  
        } else {
            error = 1;
        }

        if (strstr(filename,"/") != NULL) {
            error = 1;
        }

        if (strstr(filename, "..") != NULL) {
            error = 1;
        }

        if (!strcmp(filename, "")) {
            strcpy(filename,"index.html");
        }
        char* contents = NULL;
        if (!error) {

            char *path = (char *)malloc((strlen(www_path) + strlen(filename))*sizeof (char));
            strcpy(path, www_path);
            strcpy(path + strlen(www_path), filename);

            struct stat* file_status = malloc(sizeof(*file_status));
            if (stat(path, file_status) == 0) {
                contents = (char *)malloc((file_status->st_size+1)*sizeof (char));
                memset(contents, '\0', file_status->st_size+1);

                FILE *readfile = fopen(path, "r");
                int i;
                for (i=0;i<file_status->st_size;i++) {
                    contents[i] = fgetc(readfile);
                }
                fclose(readfile);
            } else {
                contents = NULL;
            }
            free(path);
        }

    // bind clientfd to stdout, making it easier to write
        clientfd = clients[n];
        dup2(clientfd, STDOUT_FILENO);
        close(clientfd);

        if (contents != NULL) {
            puts(resp_ok);
            puts(content_html);
            puts(contents);

        } else {
            puts(resp_bad);
            puts(content_html);
            puts(resp_404);
        }

    // tidy up
        free(contents);
        free(request);
        fflush(stdout);
        shutdown(STDOUT_FILENO, SHUT_WR);
        close(STDOUT_FILENO);
        return;
    }

    //Closing SOCKET
    shutdown(clientfd, SHUT_RDWR);         //All further send and recieve operations are DISABLED...
    close(clientfd);
    clients[n]=-1;
}

int main(int argc, char **argv) {
    if (argc < 2) {
        puts("Usage: ./server [port]");
        exit(-1);
    }
    int port = atoi(argv[1]);
    if (port < 1 || port > 65535) {
        printf("Bad port number %d. Exiting...\n");
    }

    struct sockaddr_in clientaddr;
    socklen_t addrlen;
    char c;    

    int slot=0;

    printf(
        "Server started %shttp://127.0.0.1:%s%s\n",
        "\033[92m",argv[1],"\033[0m"
        );

// Setting all elements to -1: signifies there is no client connected
    int i;
    for (i=0; i<CONNMAX; i++)
        clients[i]=-1;
    startServer(argv[1]);

// Ignore SIGCHLD to avoid zombie threads
    signal(SIGCHLD,SIG_IGN);

// ACCEPT connections
    while (1)
    {
        addrlen = sizeof(clientaddr);
        clients[slot] = accept (listenfd, (struct sockaddr *) &clientaddr, &addrlen);

        if (clients[slot]<0)
        {
            perror("accept() error");
        }
        else
        {
            if ( fork()==0 )
            {
                respond(slot);
                exit(0);
            }
        }

        while (clients[slot]!=-1) slot = (slot+1)%CONNMAX;
    }
}
