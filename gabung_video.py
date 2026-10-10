
import bpy, os
d = os.path.dirname(os.path.abspath(__file__))
fr = os.path.join(d, 'frames'); wav = os.path.join(d, 'audio', 'chase_audio.wav')
out = os.path.join(d, 'porsche_chase_FINAL.mp4')
bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene; r = sc.render
r.resolution_x, r.resolution_y, r.resolution_percentage = 1920, 1080, 100
r.fps = 24; sc.frame_start = 1; sc.frame_end = 456
try: sc.view_settings.view_transform = 'Standard'
except Exception: pass
se = sc.sequence_editor_create()
files = sorted(f for f in os.listdir(fr) if f.lower().endswith('.png'))
st = se.strips.new_image('video', os.path.join(fr, files[0]), 1, 1)
for f in files[1:]: st.elements.append(f)
se.strips.new_sound('suara', wav, 2, 1)
try: r.image_settings.media_type = 'VIDEO'
except Exception: pass
r.image_settings.file_format = 'FFMPEG'
ff = r.ffmpeg; ff.format = 'MPEG4'; ff.codec = 'H264'
for a, v in (('constant_rate_factor', 'HIGH'), ('audio_codec', 'AAC'), ('audio_bitrate', 192), ('audio_channels', 'STEREO'), ('audio_mixrate', 48000)):
    try: setattr(ff, a, v)
    except Exception: pass
r.filepath = out
sc.frame_end = min(456, len(files))
bpy.ops.render.render(animation=True)
print("SELESAI", out)
