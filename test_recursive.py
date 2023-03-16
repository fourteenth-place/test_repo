import numpy as np
import random
from tqdm import tqdm


def chunk_oids(oids, chunksize):
    oid_chunks = [oids[i : i + chunksize] for i in range(0, len(oids), chunksize)]
    return oid_chunks


def get_features_object_ids(object_ids):
    # chaos - 1 in 10 fail
    result = round(random.uniform(0, 1), 1)
    if result < 0.5:
        print("failure")
        raise Exception("failure")
    else:
        return object_ids


def retry_get_features_object_ids(object_ids):
    try:
        features = get_features_object_ids(object_ids=object_ids)
    except Exception:
        # Split in half
        oids_groups = np.array_split(object_ids, 2)
        # Loop over both, calling retry get object ids if fail
        features = []
        for group in oids_groups:
            if len(group) == 0:
                continue
            group_features = retry_get_features_object_ids(object_ids=group)
            features.extend(group_features)
    # Return successful
    return features


def get_all_features(record_count=5):
    all_object_ids = [i for i in range(100)]
    oid_chunks = chunk_oids(oids=all_object_ids, chunksize=record_count)
    all_features = []
    for chunk in tqdm(oid_chunks):
        results = retry_get_features_object_ids(chunk)
        all_features.extend(results)
    return all_features


af = get_all_features()
print(af)
print(len(af) == 100)
print(1)
