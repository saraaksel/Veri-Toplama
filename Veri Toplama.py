import requests

BASE_URL = "https://api.coingecko.com/api/v3"

def tum_kripto_paralari_getir():
    """Tüm kripto paraların listesini getirir."""
    url = BASE_URL + "/coins/list"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def kripto_para_bilgisi_getir(kripto_id):
    """Belirtilen kripto ID'sine sahip kripto para bilgisini getirir."""
    url = BASE_URL + f"/coins/{kripto_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def kripto_piyasa_verilerini_getir(kripto_id, para_birimi="usd"):
    """Kripto paranın piyasa verilerini getirir."""
    url = BASE_URL + "/coins/markets"
    params = {"vs_currency": para_birimi, "ids": kripto_id}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def isme_gore_kripto_ara(anahtar_kelime):
    """Kripto paraları isimlerine göre arar."""
    kripto_paralar = tum_kripto_paralari_getir()
    if kripto_paralar:
        sonuc = []
        for kripto in kripto_paralar:
            if anahtar_kelime.lower() in kripto["name"].lower():
                sonuc.append(kripto)
        return sonuc
    else:
        return None

def gecmis_fiyat_verilerini_getir(kripto_id, gun_sayisi=30):
    """Belirtilen kripto paranın geçmiş fiyat verilerini getirir."""
    url = BASE_URL + f"/coins/{kripto_id}/market_chart"
    params = {"vs_currency": "usd", "days": gun_sayisi}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None
