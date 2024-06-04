from .jian import *

NODE_CLASS_MAPPINGS = {
    "Text2AutioEdgeTts": text_2_autio,
    "novel_draft": create_draf,
    "novel_draft_2": sc_cao_gao,
}

NODE_DISPLAY_NAME_MAPPINGS = {
   "Text2AutioEdgeTts": "微软文本转语音",
   "novel_draft": "草稿名字",
   "novel_draft_2": "草稿gongzuo",
}
