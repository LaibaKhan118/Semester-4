#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/wait.h>

typedef struct {
    float temperature;
    float humidity;
} WeatherData;

int main() {
    int pipefds[2];
    WeatherData data;
    pid_t pid;
    if (pipe(pipefds) == -1) {
        perror("pipe");
        exit(EXIT_FAILURE);
    }
    pid = fork();

    if (pid == -1) {
        perror("fork");
        exit(EXIT_FAILURE);
    }

    if (pid == 0) {
        close(pipefds[1]);
        while (read(pipefds[0], &data, sizeof(WeatherData)) > 0) {
            if (data.temperature > 40.0) {
                printf("Processor [PID %d]: ALERT: High Temperature! (%.2f C)\n", getpid(), data.temperature);
            } else {
                printf("Processor [PID %d]: Normal Weather Conditions. (%.2f C)\n", getpid(), data.temperature);
            }
        }
        close(pipefds[0]);
        exit(0);
    } else {
        close(pipefds[0]);
        for (int i = 0; i < 3; i++) {
            data.temperature = 30.0 + (i * 15.0);
            data.humidity = 50.0 + i;
            printf("Sensor [PID %d]: Sending Temp: %.2f C\n", getpid(), data.temperature);
            write(pipefds[1], &data, sizeof(WeatherData));
            sleep(2);
        }
        close(pipefds[1]);
        wait(NULL);
    }

    return 0;
}
