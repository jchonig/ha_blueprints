# Home Assistant blueprints

My collection of Home Assistant blueprints.

## Automations

### Daylight Saving Sync

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https://github.com/jchonig/ha_blueprints/blob/main/automations/dst_sync.yaml)

Ensures devices that support daylight saving time (i.e. thermostats
that display the time) are are updated with the current state of
daylight saving.

### Leak Notification

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https://github.com/jchonig/ha_blueprints/blob/main/automations/leak_notification.yaml)

Send a notification when a moisture sensor turns on.
Based on [this gist](https://gist.githubusercontent.com/bbbenji/d4d1fe1856ec54370a422508c8963f2a/raw/f64638a09727cd62141001d99d09ed4444e5a1af/leak-detector-notifier.yaml)

### Voice Timer

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https://github.com/jchonig/ha_blueprints/blob/main/automations/voice_timer_alert.yaml)

Start a `timer` helper by voice, get a spoken confirmation of the
duration, and get an alert (looping sound, TTS, and/or a phone
notification) on the same Assist satellite when it finishes. Say a
stop phrase naming the timer, tap the notification button, or press
the satellite's physical button to silence it — only the timer helper
itself needs to be created by hand.

## Scripts

### ZSE50 Siren Alert

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https://github.com/jchonig/ha_blueprints/blob/main/automations/zse50_siren_alert.yaml)

Creates a callable script that plays a specific tone on one or more ZSE50
siren devices. Create one script instance per alert sound you need and call
it from other automations — no helper entities required.
