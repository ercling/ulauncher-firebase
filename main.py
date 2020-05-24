from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction

class FirebaseLauncherExtension(Extension):

    def __init__(self):
        super(FirebaseLauncherExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())

class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):

        actions = list()
        query = event.get_argument() or ""

        array = [
            [
                "Project Overview",
                OpenUrlAction("https://console.firebase.google.com/project/_/overview"),
                "images/firebase_logo.png"
            ],
            [
                "Authentication",
                OpenUrlAction("https://console.firebase.google.com/project/_/authentication/users"),
                "images/auth.png"
            ],
            [
                "Firestore",
                OpenUrlAction("https://console.firebase.google.com/project/_/database/firestore/data"),
                "images/firestore.png"
            ],
            [
                "Realtime Database",
                OpenUrlAction("https://console.firebase.google.com/project/_/database/data"),
                "images/realtimedb.png"
            ],
            [
                "Storage",
                OpenUrlAction("https://console.firebase.google.com/project/_/storage"),
                "images/storage.png"
            ],
            [
                "Hosting",
                OpenUrlAction("https://console.firebase.google.com/project/_/hosting"),
                "images/functions.png"
            ],
            [
                "Functions",
                OpenUrlAction("https://console.firebase.google.com/project/_/functions/list/"),
                "images/functions.png"
            ],
            [
                "ML Kit",
                OpenUrlAction("https://console.firebase.google.com/project/_/ml"),
                "images/functions.png"
            ],
            [
                "Crashlytics",
                OpenUrlAction("https://console.firebase.google.com/project/_/crashlytics"),
                "images/crashlytics.png"
            ],
            [
                "Performance",
                OpenUrlAction("https://console.firebase.google.com/project/_/performance"),
                "images/performance.png"
            ],
            [
                "Test Lab",
                OpenUrlAction("https://console.firebase.google.com/project/_/testlab/histories"),
                "images/testlab.png"
            ],
            [
                "App Distribution",
                OpenUrlAction("https://console.firebase.google.com/project/_/appdistribution"),
                "images/appdistribution.png"
            ],
            [
                "Dashboard",
                OpenUrlAction("https://console.firebase.google.com/project/_/analytics"),
                "images/analytics.png"
            ],
            [
                "Predictions",
                OpenUrlAction("https://console.firebase.google.com/project/_/predictions"),
                "images/predictions.png"
            ],
            [
                "A/B Testing",
                OpenUrlAction("https://console.firebase.google.com/project/_/experiments/list"),
                "images/abtesting.png"
            ],
            [
                "Cloud Messaging",
                OpenUrlAction("https://console.firebase.google.com/project/_/notification"),
                "images/notification.png"
            ],
            [
                "In-App Messaging",
                OpenUrlAction("https://console.firebase.google.com/project/_/inappmessaging"),
                "images/inapp.png"
            ],
            [
                "Remote Config",
                OpenUrlAction("https://console.firebase.google.com/project/_/config"),
                "images/config.png"
            ],
            [
                "Dynamic Links",
                OpenUrlAction("https://console.firebase.google.com/project/_/durablelinks"),
                "images/durablelinks.png"
            ],
            [
                "AdMob",
                OpenUrlAction("https://console.firebase.google.com/project/_/admob"),
                "images/admob.png"
            ],
            [
                "Extensions",
                OpenUrlAction("https://console.firebase.google.com/project/_/extensions"),
                "images/extensions.png"
            ],
            [
                "Usage and billing",
                OpenUrlAction("https://console.firebase.google.com/project/_/usage"),
                "images/firebase_logo.png"
            ],
        ]

        if query != "":
           array = [x for x in array if query.lower() in x[0].lower()]

        for val in array:
            actions.append(
                ExtensionResultItem(name=val[0], on_enter=val[1], icon=val[2])
            )

        return RenderResultListAction(actions)

if __name__ == '__main__':
    FirebaseLauncherExtension().run()
