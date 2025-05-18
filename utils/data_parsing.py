from utils.postgres_client import get_data_by_layer
from utils.minio_client import get_image_urls
from utils.mongo_client import get_mongo_data_by_layer

def load_layer_data(layer_num):
    layer_key = f"CurrentLayer{layer_num}/225"
    data = get_data_by_layer(layer_num)
    image_url_1, image_url_2 = get_image_urls(layer_num)

    x_labels = list(range(len(data))) if data else []
    rpp = [float(row['RecoatPlatformPosition']) for row in data if 'RecoatPlatformPosition' in row]
    rrp = [float(row['RecoatRecoaterPosition']) for row in data if 'RecoatRecoaterPosition' in row]

    return {
        "layer_number": layer_key,
        "chart_data": data,
        "image_url_1": image_url_1,
        "image_url_2": image_url_2,
        "x_labels": x_labels,
        "RecoatPlatformPosition": rpp,
        "RecoatRecoaterPosition": rrp,
        "detail_url": f"/details/{layer_key}"
    }

def load_detail_data(layer_key):
    mongo_data = get_mongo_data_by_layer(layer_key)
    if not mongo_data:
        raise Exception(f"해당 layer({layer_key})에 대한 MongoDB 데이터가 없습니다.")

    x = list(range(len(mongo_data)))
    oh = [float(doc.get('OxygenHighChamber', 0)) for doc in mongo_data]
    ol = [float(doc.get('OxygenLowChamber', 0)) for doc in mongo_data]
    tb = [float(doc.get('TemperatureBuildplate', 0)) for doc in mongo_data]
    tc = [float(doc.get('TemperatureChamber', 0)) for doc in mongo_data]

    return {
        "layer_key": layer_key,
        "x": x,
        "oxygen_high": oh,
        "oxygen_low": ol,
        "temperature_buildplate": tb,
        "temperature_chamber": tc
    }


