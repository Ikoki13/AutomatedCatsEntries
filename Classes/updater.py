import requests
import os
import zipfile

class Updater:

    def checkForUpdates(self, currentVersion):
        response = requests.get('https://api.github.com/repos/Ikoki13/AutomatedCatsEntries/releases/latest')
        response_json = response.json()
        latestVersion = response_json['tag_name']

        if latestVersion > currentVersion:
            # Korrektur: Zugriff auf die Download-URL des ersten Assets
            downloadURL = response_json['zipball_url']
            return downloadURL
        return None

    def downloadAndInstallUpdate(self, downloadURL):
        localFilename = downloadURL.split('/')[-1]
        with requests.get(downloadURL, stream=True) as r:
            with open(localFilename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)

        # Extrahieren des Updates
        with zipfile.ZipFile(localFilename, 'r') as zipRef:
            for member in zipRef.namelist():
                # Optional: Alte Dateien löschen, wenn notwendig
                target_path = os.path.join(os.getcwd(), member)
                if os.path.exists(target_path):
                    try:
                        if os.path.isdir(target_path):
                            shutil.rmtree(target_path)
                        else:
                            os.remove(target_path)
                    except PermissionError as e:
                        print(f"Fehler beim Löschen der alten Datei: {e}")
                zipRef.extract(member, os.getcwd())

        # Angenommen, das Update benötigt keine weiteren Installationsschritte,
        # andernfalls müssten Sie hier spezifische Befehle einfügen
        print("Update erfolgreich heruntergeladen und extrahiert")