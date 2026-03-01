#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <dirent.h>

int main() {
    pid_t pid = fork();

    if (pid < 0) {
        perror("Fork failed");
        return 1;
    }
    else if (pid == 0) {
        DIR *dir = opendir(".");
        if(!dir) {
          perror("DIR Failed!");
          exit(EXIT_FAILURE);
        }
        struct dirent *entry;
        while(entry=readdir(dir)) {
          printf("%s\n", entry->d_name);
        }
    }
    else {
        wait(NULL);
        printf("Parent: child finished, pid=%d\n", getpid());
    }

    return 0;
}
