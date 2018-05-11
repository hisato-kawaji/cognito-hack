#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import argparse
from boto3.session import Session


def auth_cognito(profile, pool_id, client_id, username, password):

    session = Session(profile_name=profile)
    try:
        aws_client = session.client('cognito-idp')
        aws_result = aws_client.admin_initiate_auth(
            UserPoolId=pool_id,
            ClientId=client_id,
            AuthFlow="ADMIN_NO_SRP_AUTH",
            AuthParameters={
                "USERNAME": username,
                "PASSWORD": password,
            }
        )

        # 認証完了
        return aws_result

    except:
        return None


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--profile', type=str, required=True,
                        help='input aws profile name (DO NOT USE DEFAULT PROFILE)')
    parser.add_argument('-l', '--pool', type=str, required=True,
                        help='cognito user pool id')
    parser.add_argument('-c', '--client', type=str, required=True,
                        help='cognito user pool client id')
    parser.add_argument('-u', '--username', type=str, required=True,
                        help='cognito authable user name')
    parser.add_argument('-s', '--password', type=str, required=True,
                        help='cognito authable pass word')

    args = parser.parse_args()
    profile = args.profile
    userpool_id = args.pool
    client_id = args.client
    username = args.username
    password = args.password
    result = auth_cognito(
        profile, userpool_id, client_id,
        username, password
    )

    if result is None:
        print('False')
    else:
        print('True')
