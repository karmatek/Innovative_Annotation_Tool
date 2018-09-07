import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(
    # The release date of the version of the API you want to use.
    '2018-03-19',
    # visual-recognition's API key
    iam_api_key='cdH1cuZP6Oik4LWWBS5fqEBGo957ZSpjwvGWleVBICOW')

images_url='https://vignette.wikia.nocookie.net/phobia/images/4/44/Skin_mole.jpg'

res = visual_recognition.classify(parameters=json.dumps({'url': images_url}),classifier_ids='Mole_1221677203')
print(json.dumps(res))