import requests

headers = {
    'authority': 'www.youtube.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': 'SAPISIDHASH 1677280516_4ff31be2b050d0d020a87407d95ebc8bbb152667',
    'content-type': 'application/json',
    # 'cookie': '__Secure-3PSID=MAgz_Xw5eOyQVgjzfypWY5U5azD4IQ4hed48j2LkeoBsEY_o_mgJI8LwXFywxQgIhk53rQ.; __Secure-3PAPISID=wTJ4pkjeLJgbCypy/AVJI3ud3B3WVOOa6T; __Secure-3PSIDCC=AJi4QfHYOM_vRrELKHfY88rbAInDp6frtoUUu4e-OWWqkre4--PQ8vB4MF7U2ltn4JvKTgTj; DEVICE_INFO=ChxOekU1TnpnME56azVOamN5TnpZd016TXlOdz09EJ7Jj58GGJ7Jj58G; VISITOR_INFO1_LIVE=yUaicF3O0qc; YSC=DmF-6AwPvPo; PREF=f4=4000000&tz=America.New_York; GPS=1; CONSISTENCY=AEhaiyvnNX5sq93wHDsfzq8Ij6WtXayDuDo8Zg8XqgR906Ju8bUC-l7lOan04RGg6skeBbFJZjyNLTvgAM8aCdoQng7fsF58dDVCtts83pgz5hnDvaRZEQ9ekxFQEHPxLT-nuxjGA-5MUWxp37gzpXM; ST-1kc74yn=itct=COQBEKQwGAEiEwikoJDnpK_9AhVOupwKHQYoB30yB3JlbGF0ZWRI9oTm1ofZgp-8AZoBBQgBEPgd&csn=MC4yMTM0NDUyNjAyNDU5NzYy&endpoint=%7B%22clickTrackingParams%22%3A%22COQBEKQwGAEiEwikoJDnpK_9AhVOupwKHQYoB30yB3JlbGF0ZWRI9oTm1ofZgp-8AZoBBQgBEPgd%22%2C%22commandMetadata%22%3A%7B%22webCommandMetadata%22%3A%7B%22url%22%3A%22%2Fwatch%3Fv%3DCArjX-gzi5o%22%2C%22webPageType%22%3A%22WEB_PAGE_TYPE_WATCH%22%2C%22rootVe%22%3A3832%7D%7D%2C%22watchEndpoint%22%3A%7B%22videoId%22%3A%22CArjX-gzi5o%22%2C%22nofollow%22%3Atrue%2C%22watchEndpointSupportedOnesieConfig%22%3A%7B%22html5PlaybackOnesieConfig%22%3A%7B%22commonConfig%22%3A%7B%22url%22%3A%22https%3A%2F%2Frr2---sn-ab5sznzk.googlevideo.com%2Finitplayback%3Fsource%3Dyoutube%26oeis%3D1%26c%3DWEB%26oad%3D3200%26ovd%3D3200%26oaad%3D11000%26oavd%3D11000%26ocs%3D700%26oewis%3D1%26oputc%3D1%26ofpcc%3D1%26msp%3D1%26odepv%3D1%26id%3D080ae35fe8338b9a%26ip%3D209.2.224.160%26initcwndbps%3D1753750%26mt%3D1677280149%26oweuc%3D%26pxtags%3DCg4KAnR4EggyNDQyODQxNg%26rxtags%3DCg4KAnR4EggyNDQyODQxNA%252CCg4KAnR4EggyNDQyODQxNQ%252CCg4KAnR4EggyNDQyODQxNg%252CCg4KAnR4EggyNDQyODQxNw%252CCg4KAnR4EggyNDQyODQxOA%252CCg4KAnR4EggyNDQyODQxOQ%252CCg4KAnR4EggyNDQyODQyMA%22%7D%7D%7D%7D%7D',
    'origin': 'https://www.youtube.com',
    'referer': 'https://www.youtube.com/watch?v=vD4KyHrZgnY',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"110.0.5481.177"',
    'sec-ch-ua-full-version-list': '"Chromium";v="110.0.5481.177", "Not A(Brand";v="24.0.0.0", "Google Chrome";v="110.0.5481.177"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '',
    'sec-ch-ua-platform': '"macOS"',
    'sec-ch-ua-platform-version': '"11.6.0"',
    'sec-ch-ua-wow64': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'same-origin',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'x-client-data': 'CIu2yQEIo7bJAQjEtskBCKmdygEI1P3KAQiTocsBCMLJzAEI1vXMAQjwgM0BCO6LzQEIi4zNAQjTjc0BCLmRzQEI0uGsAgibhK0CGNjszAE=',
    'x-goog-authuser': '0',
    'x-goog-visitor-id': 'Cgt5VWFpY0YzTzBxYyjzg-WfBg%3D%3D',
    'x-origin': 'https://www.youtube.com',
    'x-youtube-bootstrap-logged-in': 'false',
    'x-youtube-client-name': '1',
    'x-youtube-client-version': '2.20230221.06.00',
}

params = {
    'key': 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8',
    'prettyPrint': 'false',
}

json_data = {
    'context': {
        'client': {
            'hl': 'en',
            'gl': 'US',
            'remoteHost': '209.2.224.160',
            'deviceMake': 'Apple',
            'deviceModel': '',
            'visitorData': 'Cgt5VWFpY0YzTzBxYyjzg-WfBg%3D%3D',
            'userAgent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36,gzip(gfe)',
            'clientName': 'WEB',
            'clientVersion': '2.20230221.06.00',
            'osName': 'Macintosh',
            'osVersion': '10_15_7',
            'originalUrl': 'https://www.youtube.com/watch?v=CArjX-gzi5o',
            'screenPixelDensity': 2,
            'platform': 'DESKTOP',
            'clientFormFactor': 'UNKNOWN_FORM_FACTOR',
            'configInfo': {
                'appInstallData': 'CPOD5Z8GEOyGrwUQzN-uBRDloP4SEILdrgUQuNSuBRDM9a4FENrprgUQyImvBRDn964FEOLUrgUQlPiuBRC4i64FEIfdrgUQtpz-EhC4rP4SEInorgUQouyuBRD-7q4FEPOKrwUQ66r-EhCW3K4FEJH4_BI%3D',
            },
            'screenDensityFloat': 2,
            'timeZone': 'America/New_York',
            'browserName': 'Chrome',
            'browserVersion': '110.0.0.0',
            'acceptHeader': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'deviceExperimentId': 'ChxOekU1TnpnME56azVOamN5TnpZd016TXlOdz09EPOD5Z8GGJ7Jj58G',
            'screenWidthPoints': 861,
            'screenHeightPoints': 889,
            'utcOffsetMinutes': -300,
            'userInterfaceTheme': 'USER_INTERFACE_THEME_LIGHT',
            'memoryTotalKbytes': '8000000',
            'clientScreen': 'WATCH',
            'mainAppWebInfo': {
                'graftUrl': '/watch?v=CArjX-gzi5o',
                'pwaInstallabilityStatus': 'PWA_INSTALLABILITY_STATUS_CAN_BE_INSTALLED',
                'webDisplayMode': 'WEB_DISPLAY_MODE_BROWSER',
                'isWebNativeShareAvailable': False,
            },
        },
        'user': {
            'lockedSafetyMode': False,
        },
        'request': {
            'useSsl': True,
            'internalExperimentFlags': [],
            'consistencyTokenJars': [
                {
                    'encryptedTokenJarContents': 'AEhaiyvnNX5sq93wHDsfzq8Ij6WtXayDuDo8Zg8XqgR906Ju8bUC-l7lOan04RGg6skeBbFJZjyNLTvgAM8aCdoQng7fsF58dDVCtts83pgz5hnDvaRZEQ9ekxFQEHPxLT-nuxjGA-5MUWxp37gzpXM',
                    'expirationSeconds': '600',
                },
            ],
        },
        'clickTracking': {
            'clickTrackingParams': 'COQBEKQwGAEiEwikoJDnpK_9AhVOupwKHQYoB30yB3JlbGF0ZWRI9oTm1ofZgp-8AZoBBQgBEPgd',
        },
        'adSignalsInfo': {
            'params': [
                {
                    'key': 'dt',
                    'value': '1677279732184',
                },
                {
                    'key': 'flash',
                    'value': '0',
                },
                {
                    'key': 'frm',
                    'value': '0',
                },
                {
                    'key': 'u_tz',
                    'value': '-300',
                },
                {
                    'key': 'u_his',
                    'value': '6',
                },
                {
                    'key': 'u_h',
                    'value': '1120',
                },
                {
                    'key': 'u_w',
                    'value': '1792',
                },
                {
                    'key': 'u_ah',
                    'value': '1040',
                },
                {
                    'key': 'u_aw',
                    'value': '1792',
                },
                {
                    'key': 'u_cd',
                    'value': '30',
                },
                {
                    'key': 'bc',
                    'value': '31',
                },
                {
                    'key': 'bih',
                    'value': '889',
                },
                {
                    'key': 'biw',
                    'value': '845',
                },
                {
                    'key': 'brdim',
                    'value': '0,25,0,25,1792,25,1715,1000,861,889',
                },
                {
                    'key': 'vis',
                    'value': '1',
                },
                {
                    'key': 'wgl',
                    'value': 'true',
                },
                {
                    'key': 'ca_type',
                    'value': 'image',
                },
            ],
            'bid': 'ANyPxKpyJtKodRKpRdmIO3QavE8ntnnGX6u90vPwMsoysaMYZpjk44yxRLcVIfwzgdLtap7nQzYW4bZ53dpSZvudAi8MC0G7Cg',
        },
    },
    'videoId': 'CArjX-gzi5o',
    'racyCheckOk': False,
    'contentCheckOk': False,
    'autonavState': 'STATE_NONE',
    'playbackContext': {
        'vis': 0,
        'lactMilliseconds': '-1',
    },
    'captionsRequested': False,
}

response = requests.post('https://www.youtube.com/youtubei/v1/next', params=params, headers=headers, json=json_data)

print(response)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"context":{"client":{"hl":"en","gl":"US","remoteHost":"209.2.224.160","deviceMake":"Apple","deviceModel":"","visitorData":"Cgt5VWFpY0YzTzBxYyjzg-WfBg%3D%3D","userAgent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36,gzip(gfe)","clientName":"WEB","clientVersion":"2.20230221.06.00","osName":"Macintosh","osVersion":"10_15_7","originalUrl":"https://www.youtube.com/watch?v=CArjX-gzi5o","screenPixelDensity":2,"platform":"DESKTOP","clientFormFactor":"UNKNOWN_FORM_FACTOR","configInfo":{"appInstallData":"CPOD5Z8GEOyGrwUQzN-uBRDloP4SEILdrgUQuNSuBRDM9a4FENrprgUQyImvBRDn964FEOLUrgUQlPiuBRC4i64FEIfdrgUQtpz-EhC4rP4SEInorgUQouyuBRD-7q4FEPOKrwUQ66r-EhCW3K4FEJH4_BI%3D"},"screenDensityFloat":2,"timeZone":"America/New_York","browserName":"Chrome","browserVersion":"110.0.0.0","acceptHeader":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","deviceExperimentId":"ChxOekU1TnpnME56azVOamN5TnpZd016TXlOdz09EPOD5Z8GGJ7Jj58G","screenWidthPoints":861,"screenHeightPoints":889,"utcOffsetMinutes":-300,"userInterfaceTheme":"USER_INTERFACE_THEME_LIGHT","memoryTotalKbytes":"8000000","clientScreen":"WATCH","mainAppWebInfo":{"graftUrl":"/watch?v=CArjX-gzi5o","pwaInstallabilityStatus":"PWA_INSTALLABILITY_STATUS_CAN_BE_INSTALLED","webDisplayMode":"WEB_DISPLAY_MODE_BROWSER","isWebNativeShareAvailable":false}},"user":{"lockedSafetyMode":false},"request":{"useSsl":true,"internalExperimentFlags":[],"consistencyTokenJars":[{"encryptedTokenJarContents":"AEhaiyvnNX5sq93wHDsfzq8Ij6WtXayDuDo8Zg8XqgR906Ju8bUC-l7lOan04RGg6skeBbFJZjyNLTvgAM8aCdoQng7fsF58dDVCtts83pgz5hnDvaRZEQ9ekxFQEHPxLT-nuxjGA-5MUWxp37gzpXM","expirationSeconds":"600"}]},"clickTracking":{"clickTrackingParams":"COQBEKQwGAEiEwikoJDnpK_9AhVOupwKHQYoB30yB3JlbGF0ZWRI9oTm1ofZgp-8AZoBBQgBEPgd"},"adSignalsInfo":{"params":[{"key":"dt","value":"1677279732184"},{"key":"flash","value":"0"},{"key":"frm","value":"0"},{"key":"u_tz","value":"-300"},{"key":"u_his","value":"6"},{"key":"u_h","value":"1120"},{"key":"u_w","value":"1792"},{"key":"u_ah","value":"1040"},{"key":"u_aw","value":"1792"},{"key":"u_cd","value":"30"},{"key":"bc","value":"31"},{"key":"bih","value":"889"},{"key":"biw","value":"845"},{"key":"brdim","value":"0,25,0,25,1792,25,1715,1000,861,889"},{"key":"vis","value":"1"},{"key":"wgl","value":"true"},{"key":"ca_type","value":"image"}],"bid":"ANyPxKpyJtKodRKpRdmIO3QavE8ntnnGX6u90vPwMsoysaMYZpjk44yxRLcVIfwzgdLtap7nQzYW4bZ53dpSZvudAi8MC0G7Cg"}},"videoId":"CArjX-gzi5o","racyCheckOk":false,"contentCheckOk":false,"autonavState":"STATE_NONE","playbackContext":{"vis":0,"lactMilliseconds":"-1"},"captionsRequested":false}'
#response = requests.post('https://www.youtube.com/youtubei/v1/next', params=params, cookies=cookies, headers=headers, data=data)