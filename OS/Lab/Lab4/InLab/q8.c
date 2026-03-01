#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <signal.h>

void handle_alarm(int sig) {
    printf("\n[Alarm Received] 5 seconds are up! Terminating gracefully...\n");
    exit(0);
}

int main() {
    signal(SIGALRM, handle_alarm);
    printf("Setting alarm for 5 seconds...\n");
    alarm(5);

    int counter = 0;
    while (1) {
        sleep(1);
        counter++;
        printf("Looping... %d second(s) elapsed.\n", counter);
    }

    return 0;
}

