import uuid

from utils.utils import log


def gen_uuid():
    # namespace = uuid.NAMESPACE_DNS
    uuid_str = uuid.uuid1().hex
    log(uuid_str)
    return uuid_str
