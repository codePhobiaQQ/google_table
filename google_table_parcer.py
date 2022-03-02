import os
import httplib2
import config
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

import creds

#bot

def get_service_sacc():
    """
    Могу читать и (возможно) писать в таблицы кот. выдан доступ
    для сервисного аккаунта приложения
    sacc-1@privet-yotube-azzrael-code.iam.gserviceaccount.com
    :return:
    """
    creds_json = os.path.dirname(__file__) + "/creds/sacc2.json"
    scopes = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

    creds_service = ServiceAccountCredentials.from_json_keyfile_name(creds_json, scopes).authorize(httplib2.Http())
    return build('sheets', 'v4', http=creds_service)


# service = get_service_simple()
service = get_service_sacc()
sheet = service.spreadsheets()

# https://docs.google.com/spreadsheets/d/xxx/edit#gid=0
sheet_id = config.SHEET_ID

# https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/get
# resp = sheet.values().get(spreadsheetId=sheet_id, range="Лист1!A1:L1000").execute()

def start_parce():
    return sheet.values().get(spreadsheetId=sheet_id, range="Отчет!A1:L1000").execute()