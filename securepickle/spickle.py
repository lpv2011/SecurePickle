import pickle
import hashlib
from dataclasses import dataclass, field

def hash_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

@dataclass(frozen=True) #After the object is created, its fields cannot be modified
class SpickleObject:
    serialized_data: bytes
    hash: str = field(init=False) #init = False, to make hash field not part of the constructor

    def __post_init__(self): #__post_init__ method, to get called automatically after the obj is initialized
        object.__setattr__(self, 'hash', hash_bytes(self.serialized_data))

def dumps(obj) -> SpickleObject:
    serialized_data = pickle.dumps(obj)
    return SpickleObject(serialized_data=serialized_data)

def loads(SpickleObject):
    metadata_hash = SpickleObject.hash
    serialized_hash = hash_bytes(SpickleObject.serialized_data)
    if(metadata_hash == serialized_hash):
        return pickle.loads(SpickleObject.serialized_data)
    else:
        raise ValueError("Hashes do not match!!")
 