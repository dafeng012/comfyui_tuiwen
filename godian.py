from .utils import *
from uuid import uuid4


def tracks():
    return {
        "attribute": 0,
        "flag": 0,
        "id": generate_id(),
        "is_default_name": True,
        "name": "",
        "segments": [],
        "type": ""
    }


def segment_video():
    return {
        "cartoon": False,
        "clip": {
            "alpha": 1.0,
            "flip": {
                "horizontal": False,
                "vertical": False
            },
            "rotation": 0.0,
            "scale": {
                "x": 1.0,
                "y": 1.0
            },
            "transform": {
                "x": 0.0,
                "y": 0.0
            }
        },
        "common_keyframes": [],
        "enable_adjust": True,
        "enable_color_curves": True,
        "enable_color_match_adjust": False,
        "enable_color_wheels": True,
        "enable_lut": True,
        "enable_smart_color_adjust": False,
        "extra_material_refs": [],
        "group_id": "",
        "hdr_settings": {
            "intensity": 1.0,
            "mode": 1,
            "nits": 1000
        },
        "id": generate_id(),
        "intensifies_audio": False,
        "is_placeholder": False,
        "is_tone_modify": False,
        "keyframe_refs": [],
        "last_nonzero_volume": 1.0,
        "material_id": "",
        "render_index": 0,
        "responsive_layout": {
            "enable": False,
            "horizontal_pos_layout": 0,
            "size_layout": 0,
            "target_follow": "",
            "vertical_pos_layout": 0
        },
        "reverse": False,
        "source_timerange": {
            "duration": 5000000,
            "start": 0
        },
        "speed": 1.0,
        "target_timerange": {
            "duration": 5000000,
            "start": 0
        },
        "template_id": "",
        "template_scene": "default",
        "track_attribute": 0,
        "track_render_index": 0,
        "uniform_scale": {
            "on": True,
            "value": 1.0
        },
        "visible": True,
        "volume": 1.0
    }


def segment_audio():
    return {
        "cartoon": False,
        "clip": None,
        "common_keyframes": [],
        "enable_adjust": False,
        "enable_color_curves": True,
        "enable_color_match_adjust": False,
        "enable_color_wheels": True,
        "enable_lut": False,
        "enable_smart_color_adjust": False,
        "extra_material_refs": [],
        "group_id": "",
        "hdr_settings": None,
        "id": generate_id(),
        "intensifies_audio": False,
        "is_placeholder": False,
        "is_tone_modify": False,
        "keyframe_refs": [],
        "last_nonzero_volume": 1.0,
        # id1=================================================
        "material_id": "",
        "render_index": 0,
        "responsive_layout": {
            "enable": False,
            "horizontal_pos_layout": 0,
            "size_layout": 0,
            "target_follow": "",
            "vertical_pos_layout": 0
        },
        "reverse": False,
        "source_timerange": {
            "duration": 0,
            "start": 0
        },
        "speed": 1.0,
        "target_timerange": {
            "duration": 0,
            "start": 0
        },
        "template_id": "",
        "template_scene": "default",
        "track_attribute": 0,
        "track_render_index": 0,
        "uniform_scale": None,
        "visible": True,
        "volume": 1.0
    }


def vocal():
    return {
        "choice": 0,
        "id": "",
        "production_path": "",
        "time_range": None,
        "type": "vocal_separation"
    }


def videos_items():
    return {
        "aigc_type": "none",
        "audio_fade": None,
        "cartoon_path": "",
        "category_id": "",
        "category_name": "local",
        "check_flag": 63487,
        "crop": {
            "lower_left_x": 0.0,
            "lower_left_y": 1.0,
            "lower_right_x": 1.0,
            "lower_right_y": 1.0,
            "upper_left_x": 0.0,
            "upper_left_y": 0.0,
            "upper_right_x": 1.0,
            "upper_right_y": 0.0
        },
        "crop_ratio": "free",
        "crop_scale": 1.0,
        "duration": 10800000000,
        "extra_type_option": 0,
        "formula_id": "",
        "freeze": None,
        "gameplay": None,
        "has_audio": False,
        "height": 0,
        "id": "",
        "intensifies_audio_path": "",
        "intensifies_path": "",
        "is_ai_generate_content": False,
        "is_unified_beauty_mode": False,
        "local_id": "",
        "local_material_id": "",
        "material_id": "",
        "material_name": "",
        "material_url": "",
        "matting": {
            "flag": 0,
            "has_use_quick_brush": False,
            "has_use_quick_eraser": False,
            "interactiveTime": [],
            "path": "",
            "strokes": []
        },
        "media_path": "",
        "object_locked": None,
        "origin_material_id": "",
        "path": "",
        "picture_from": "none",
        "picture_set_category_id": "",
        "picture_set_category_name": "",
        "request_id": "",
        "reverse_intensifies_path": "",
        "reverse_path": "",
        "smart_motion": None,
        "source": 0,
        "source_platform": 0,
        "stable": {
            "matrix_path": "",
            "stable_level": 0,
            "time_range": {
                "duration": 0,
                "start": 0
            }
        },
        "team_id": "",
        "type": "photo",
        "video_algorithm": {
            "algorithms": [],
            "deflicker": None,
            "motion_blur_config": None,
            "noise_reduction": None,
            "path": "",
            "quality_enhance": None,
            "time_range": None
        },
        "width": 0
    }


def speeds_items():
    return {
        "curve_speed": None,
        "id": "",
        "mode": 0,
        "speed": 1.0,
        "type": "speed"
    }


def sound_items():
    return {
        "audio_channel_mapping": 0,
        "id": "",
        "is_config_open": False,
        "type": ""
    }


def canvases_items():
    return {
        "album_image": "",
        "blur": 0.0,
        "color": "",
        "id": "",
        "image": "",
        "image_id": "",
        "image_name": "",
        "source_platform": 0,
        "team_id": "",
        "type": "canvas_color"
    }


def beats_items():
    return {
        "ai_beats": {
            "beat_speed_infos": [],
            "beats_path": "",
            "beats_url": "",
            "melody_path": "",
            "melody_percents": [
                0.0
            ],
            "melody_url": ""
        },
        "enable_ai_beats": False,
        "gear": 404,
        "gear_count": 0,
        # =====这个跟segments.extra_material_refs第二个字符串一样
        "id": "",
        "mode": 404,
        "type": "beats",
        "user_beats": [],
        "user_delete_ai_beats": None
    }


def audios():
    return {
        "app_id": 0,
        "category_id": "",
        "category_name": "local",
        "check_flag": 1,
        "duration": 0,
        "effect_id": "",
        "formula_id": "",
        # 跟tracks.segments.material_id一样 id1
        "id": "",
        "intensifies_path": "",
        "local_material_id": generate_id(),
        "music_id": generate_id(),
        # ========音频0====
        "name": "",
        "path": "",
        "query": "",
        "request_id": "",
        "resource_id": "",
        "search_id": "",
        "source_platform": 0,
        "team_id": "",
        "text_id": "",
        "tone_category_id": "",
        "tone_category_name": "",
        "tone_effect_id": "",
        "tone_effect_name": "",
        "tone_speaker": "",
        "tone_type": "",
        "type": "extract_music",
        "video_id": "",
        "wave_points": []
    }


def draft_materials_items():
    return {
        "create_time": int(time.time()),
        "duration": 0,
        "extra_info": "",
        "file_Path": "",
        "height": 0,
        "id": generate_id(),
        "import_time": int(time.time()),
        "import_time_ms": int(time.time()) * 10 ** 3,
        "item_source": 1,
        "md5": "",
        "metetype": "0",
        "roughcut_time_range": {
            "duration": -1,
            "start": -1
        },
        "sub_time_range": {
            "duration": -1,
            "start": -1
        },
        "type": 0,
        "width": 0
    }


def material_animations_items():
    return {
                "animations": [],
                "id": "",
                "multi_language_current": "none",
                "type": "sticker_animation"
    }

def text_items():
    return {
                "add_type": 2,
                "alignment": 1,
                "background_alpha": 1.0,
                "background_color": "#000000",
                "background_height": 0.14,
                "background_horizontal_offset": 0.0,
                "background_round_radius": 0.0,
                "background_style": 0,
                "background_vertical_offset": 0.0,
                "background_width": 0.14,
                "base_content": "",
                "bold_width": 0.0,
                "border_alpha": 1.0,
                "border_color": "#000000",
                "border_width": 0.08,
                "caption_template_info": {
                    "category_id": "",
                    "category_name": "",
                    "effect_id": "",
                    "is_new": False,
                    "path": "",
                    "request_id": "",
                    "resource_id": "",
                    "resource_name": "",
                    "source_platform": 0
                },
                "check_flag": 7,
                "combo_info": {
                    "text_templates": []
                },
                "content": "{\"text\":\"与此同时\",\"styles\":[{\"fill\":{\"content\":{\"solid\":{\"color\":[1,0.870588,0]}}},\"font\":{\"path\":\"C:/Users/56381/AppData/Local/JianyingPro/Apps/5.8.0.11586/Resources/Font/SystemFont/zh-hans.ttf\",\"id\":\"\"},\"size\":8,\"useLetterColor\":true,\"range\":[0,4]}]}",
                "fixed_height": -1.0,
                "fixed_width": -1.0,
                "font_category_id": "",
                "font_category_name": "",
                "font_id": "",
                "font_name": "",
                "font_path": "C:/Users/56381/AppData/Local/JianyingPro/Apps/5.8.0.11586/Resources/Font/SystemFont/zh-hans.ttf",
                "font_resource_id": "",
                "font_size": 8.0,
                "font_source_platform": 0,
                "font_team_id": "",
                "font_title": "none",
                "font_url": "",
                "fonts": [],
                "force_apply_line_max_width": False,
                "global_alpha": 1.0,
                "group_id": "",
                "has_shadow": False,
                "id": "1DB61B17-B522-49A1-9ED4-F92A5A45F2A7",
                "initial_scale": 1.0,
                "inner_padding": -1.0,
                "is_rich_text": False,
                "italic_degree": 0,
                "ktv_color": "",
                "language": "",
                "layer_weight": 1,
                "letter_spacing": 0.0,
                "line_feed": 1,
                "line_max_width": 0.82,
                "line_spacing": 0.02,
                "multi_language_current": "none",
                "name": "",
                "original_size": [],
                "preset_category": "",
                "preset_category_id": "",
                "preset_has_set_alignment": False,
                "preset_id": "",
                "preset_index": 0,
                "preset_name": "",
                "recognize_task_id": "",
                "recognize_type": 0,
                "relevance_segment": [],
                "shadow_alpha": 0.8,
                "shadow_angle": -45.0,
                "shadow_color": "",
                "shadow_distance": 8.0,
                "shadow_point": {
                    "x": 1.018233764908628,
                    "y": -1.018233764908628
                },
                "shadow_smoothing": 1.0,
                "shape_clip_x": False,
                "shape_clip_y": False,
                "source_from": "",
                "style_name": "",
                "sub_type": 0,
                "subtitle_keywords": None,
                "subtitle_template_original_fontsize": 0.0,
                "text_alpha": 1.0,
                "text_color": "#ffde00",
                "text_curve": None,
                "text_preset_resource_id": "",
                "text_size": 30,
                "text_to_audio_ids": [],
                "tts_auto_update": False,
                "type": "subtitle",
                "typesetting": 0,
                "underline": False,
                "underline_offset": 0.22,
                "underline_width": 0.05,
                "use_effect_default_color": True,
                "words": {
                    "end_time": [],
                    "start_time": [],
                    "text": []
                }
            }
def text_segment_items():
    return {
                    "caption_info": None,
                    "cartoon": False,
                    "clip": {
                        "alpha": 1.0,
                        "flip": {
                            "horizontal": False,
                            "vertical": False
                        },
                        "rotation": 0.0,
                        "scale": {
                            "x": 1.0,
                            "y": 1.0
                        },
                        "transform": {
                            "x": 0.0,
                            "y": -0.762790697674419
                        }
                    },
                    "common_keyframes": [],
                    "enable_adjust": False,
                    "enable_color_curves": True,
                    "enable_color_match_adjust": False,
                    "enable_color_wheels": True,
                    "enable_lut": False,
                    "enable_smart_color_adjust": False,
                    "extra_material_refs": [
                        
                    ],
                    "group_id": "",
                    "hdr_settings": None,
                    "id": generate_id(),
                    "intensifies_audio": False,
                    "is_placeholder": False,
                    "is_tone_modify": False,
                    "keyframe_refs": [],
                    "last_nonzero_volume": 1.0,
                    "material_id": generate_id(),
                    "render_index": 14000,
                    "responsive_layout": {
                        "enable": False,
                        "horizontal_pos_layout": 0,
                        "size_layout": 0,
                        "target_follow": "",
                        "vertical_pos_layout": 0
                    },
                    "reverse": False,
                    "source_timerange": None,
                    "speed": 1.0,
                    "target_timerange": {
                        "duration": 833333,
                        "start": 0
                    },
                    "template_id": "",
                    "template_scene": "default",
                    "track_attribute": 0,
                    "track_render_index": 0,
                    "uniform_scale": {
                        "on": True,
                        "value": 1.0
                    },
                    "visible": True,
                    "volume": 1.0
                }
def durations_items():
    return {
        "index": 0,
        "value":0,
        "start_value": 0 ,
        "end_value":0,     
    }
def items_duraion():
    return{
        "index": 0,
        "dtn": 0,
        "start_value": 0 ,
        "end_value":0,  
        "path": "",
        "name": "",
        "duration": 0,
    }