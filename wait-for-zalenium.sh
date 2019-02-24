#!/usr/bin/env bash
printf "Waiting for Zalenium docker container..."

attempt_counter=0
max_attempts=12

until $(curl --output /dev/null --silent --head --fail http://zalenium:4444/grid/console); do
    if [[ ${attempt_counter} -eq ${max_attempts} ]]; then
      printf "Zalenium docker container cannot be reached!"
      exit 1
    fi

    printf "."
    attempt_counter=$(($attempt_counter+1))
    sleep 5
done

printf "\nZalenium docker container has been reached! Starting tests."

behave