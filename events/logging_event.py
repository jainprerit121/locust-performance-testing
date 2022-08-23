import os

import requests
from locust import events

import logging


@events.spawning_complete.add_listener
def spawn_users(user_count, **kwargs):
    print("Spawned ......................... ", user_count, " users.")


@events.request_success.add_listener
def send_notification(**kwargs):
    print("================= Sending the success notification ===================")
    # post_message_to_slack("Success!", "#temp-test-channel")


@events.request_failure.add_listener
def send_notification(**kwargs):
    print("================= Sending the failed notification =================")


@events.quitting.add_listener
def sla(environment, **kwargs):
    if environment.stats.total.fail_ratio > 0.01:
        logging.error("tests failed due to failure ratio > 0.01%")
        environment.process_exit_code = 1
        print(environment.process_exit_code)

    else:
        logging.info("================= locust process is exiting =============")
        environment.process_exit_code = 0
        print(environment.process_exit_code)


def post_message_to_slack(text, slack_channel, blocks = None):
    return requests.post('https://slack.com/api/chat.postMessage', {
        'token': os.SLACK_TOKEN,
        'channel': slack_channel,
        'text': text
    }).json()