from collections import OrderedDict

INDEX_MEDIA = "../../bbctextav-de/output/"
DOMAIN = "https://hadro.github.io/iiif-interactive-transcript/bbctextav-master/"
COLLECTION_ID_TEMPLATE = "iiif/collection.json"
MANIFEST_ID_TEMPLATE = "iiif/{0}.json"
TRANSCRIPT_ID_TEMPLATE = "iiif/{0}-transcript.json"
CANVAS_URI_TEMPLATE = "iiif/{0}/canvas"
ANNOPAGE_URI_TEMPLATE = "iiif/{0}/annopage"
ANNO_URI_TEMPLATE = "iiif/{0}/content-anno-1"
# '.$speech['mediaID'].'  
VIDEO_URI_TEMPLATE = "https://phantor.net/iiif/{0}.mp4"
TEXT_ANNOS_URI_TEMPLATE = "iiif/{0}-transcript.json"
CAPTION_URI_TEMPLATE = "iiif/{0}"

MANIFEST = OrderedDict({
    "@context": [
        "http://www.w3.org/ns/anno.jsonld",
        "http://iiif.io/api/presentation/3/context.json"
    ],
    "id": None,
    "type": "Manifest",
    "label": None,
    "metadata": [

    ],
    "items": [
        {
            "id": None,
            "type": "Canvas",
            "width": 1920,
            "height": 1080,
            "duration": 0,
            "items": [
                {
                    "id": None,
                    "type": "AnnotationPage",
                    "items": [
                        {
                            "id": None,
                            "type": "Annotation",
                            "motivation": "painting",
                            "body" : {
                                "id": None,
                                "type": "Video",
                                "format": "video/mp4",
                                "width": 1920,
                                "height": 1080,
                                "duration": 0
                            },
                            "target": None
                        }
                    ]
                }
            ],
            "annotations": [
                {
                    "id": None,
                    "type": "AnnotationPage"
                }
            ]
        }
    ]
})


TRANSCRIPT_PAGE = OrderedDict({
    "id": None,
    "type": "AnnotationPage",
    "items": [
    
    ]
})

TRANSCRIPT_ANNO = OrderedDict({
    "id": None,
    "type": "Annotation",
    "motivation": "supplementing",
    "body": {
        "type": "TextualBody",
        "language": "en",
        "value": None
    },
    "target": None
})


COLLECTION = OrderedDict({
  "@context": [
    "http://www.w3.org/ns/anno.jsonld",
    "http://iiif.io/api/presentation/3/context.json"
  ],
  "id": None,
  "type": "Collection",
  "label": { "en": [ "IIIF Intro Presentations Demo"]},
  "items": [
  ]
})

COLL_MANIFEST = OrderedDict({
    "id": None,
    "type": "Manifest",
    "label": None
})