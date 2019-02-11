#!/usr/bin/env bash
echo "Waiting for Zalenium docker container..."

attempt_counter=0
max_attempts=12

until $(curl --output /dev/null --silent --head --fail http://zalenium:4444/grid/console); do
    if [[ ${attempt_counter} -eq ${max_attempts} ]];then
      echo "Zalenium docker container cannot be reached!"
      exit 1
    fi

    printf '.'
    attempt_counter=$(($attempt_counter+1))
    sleep 5
done

behave