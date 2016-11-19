"""
This is a cron file.
"""
import dropbox
from app.models import Observatory, DataEntry, ImageDataEntry


def split_str(str):
    arr = str.split('-')
    if arr[-1].endswith('.png') or arr[-1].endswith('.jpg') or arr[-1].endswith('.PNG') or arr[-1].endswith('.JPG'):
        arr[-1] = arr[-1][:-4]
    elif arr[-1].endswith('.jpeg'):
        arr[-1] = arr[-1][:-5]
    return arr


def make_url(url):
    if url.endswith('?dl=0'):
        url = url[:-5]
    return url.replace('www.dropbox', 'dl.dropboxusercontent')


def save_observatory(observatory):
    try:
        obs = Observatory.objects.get(key=observatory)
    except:
        obs = Observatory(name=observatory, key=observatory)
        obs.save()
    return obs


def save_data_entry(title, instrument, observatory, text):
    try:
        data_entry = DataEntry.objects.get(title=title, observatory=observatory)
    except:
        data_entry = DataEntry(title=title, instrument=instrument, observatory=observatory, text=text)
        data_entry.save()
    return data_entry


def save_image_entry(entry, url, arr):
    try:
        img = ImageDataEntry.objects.get(url=make_url(url), filename=entry.name)
    except ImageDataEntry.DoesNotExist:
        obs = save_observatory(arr[2])
        data_entry = save_data_entry(arr[0], arr[1], obs, arr[3])
        img = ImageDataEntry(filename=entry.name, url=make_url(url), model=data_entry)
        img.save()
        print '---NAO EXISTEE------------'
    return img


def schedule_job():
    dbx = dropbox.Dropbox('M6iN1nYzh_YAAAAAAACUfhWR5kFUT-4Hwak6aAwSANv5vP0tLCHmnHCi37y9acqY')
    for entry in dbx.files_list_folder('').entries:
        url = dbx.sharing_create_shared_link(entry.path_display).url
        arr = split_str(entry.name)
        img = save_image_entry(entry, url, arr)
