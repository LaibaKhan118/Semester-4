#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {
    pid_t pid = fork();

    if (pid < 0) {
        perror("Fork failed");
        return 1;
    }
    else if (pid == 0) {
        printf("Child: running 'ls', pid=%d, ppid=%d\n", getpid(), getppid());
        execlp("ls", "ls", NULL);
        perror("execlp failed");
    }
    else {
        wait(NULL);
        printf("Parent: child finished, pid=%d\n", getpid());
    }

    return 0;
}

