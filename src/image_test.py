from dalle2 import Dalle2
dalle = Dalle2("sess-YMsgY2QM2aP3TSK6P2jFwNpsSAhNOTMvsxvNI3d2")
file_paths = dalle.generate_and_download("futuristic cat with a sword in a boat, digital art")
print(file_paths)
