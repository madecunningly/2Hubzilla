import requests
from mastodon import Mastodon
import logging
import configparser


log = logging.getLogger(__name__)


def getMastodonConfig():
    config = configparser.ConfigParser()
    log.info(config.sections())

    config.read('../../config.ini')

    log.info(config.sections())

    if config['MASTODON']:
        for key in config['MASTODON']:
            print(key)

        return(config['MASTODON'])


def registerApp():
    new_app = Mastodon.create_app(
        'pytooterapp',
        scopes=['read', 'write', 'follow', 'push']
        api_base_url='https://mastodon.social',
        to_file='pytooter_clientcred.secret'
    )
    log.info(new_app)

    client_id = new_app[0]
    client_secret = new_app[1]

    return client_id, client_secret


def auth(client_id, username, password):

    mastodon = Mastodon(
        client_id=registerApp()[0],
        client_secret=registerApp()[1],
        api_base_url='https://mastodon.social'
    )
    access_token = mastodon.log_in(
        username,
        password,
        to_file='pytooter_usercred.secret'
    )

    return access_token


def post(access_token):

    mastodon = Mastodon(
        access_token=access_token,
        api_base_url='https://mastodon.social'
    )
    mastodon.toot('Tooting from python using #mastodonpy again!')


def get(access_token):
    mastodon = Mastodon(
        access_token=access_token,
        api_base_url='https://mastodon.social'
    )
    mastodon.toot('Tooting from python using #mastodonpy again!')


def getInstallationData():
    mastodon = Mastodon(
        api_base_url='https://mastodon.social'
    )
    mastodon.retrieve_mastodon_version()


def main():

    #access_token = getMastodonConfig()['access_token']

    print(getInstallationData())


if __name__ == "__main__":
    main()
