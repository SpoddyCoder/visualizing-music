import ruclip
from rudalle.pipelines import generate_images, show, super_resolution, cherry_pick_by_ruclip
from rudalle import get_rudalle_model, get_tokenizer, get_vae, get_realesrgan
from rudalle.utils import seed_everything
from deep_translator import GoogleTranslator

# cache
cache_dir = '/home/fernpa/resource-ai/ai-music-viz/cache/ru-dalle/'
image_save_dir = '/home/fernpa/resource-ai/ai-music-viz/expt-renders/ru-dalle/'

# create
text = 'modern art picture full size'
image_prefix = 'gen-image'
translated = GoogleTranslator(source='auto', target='ru').translate(text)
start_seed = 100000   # max 2^32
images_per_res = 2
seed_batches = 1
batch_size = 8
upscale_multiplier = 'x2'   # x2, x4, x8

# prepare models:
device = 'cuda'
dalle = get_rudalle_model('Malevich', pretrained=True, fp16=True, device=device, cache_dir=cache_dir)   # Kandinsky
realesrgran = get_realesrgan(upscale_multiplier, device=device, cache_dir=cache_dir)
tokenizer = get_tokenizer()
vae = get_vae(cache_dir=cache_dir).to(device)
clip, ruclip_processor = ruclip.load('ruclip-vit-base-patch32-384', device=device, cache_dir=cache_dir)
clip = clip.to(device)
#clip_predictor = ruclip.Predictor(clip, processor, device, bs=8)

for seed in range(start_seed, (start_seed + seed_batches)):
    print(f'Text: {text}')
    print(f'Russian: {translated}')
    print(f'Seed: {seed}')

    seed_everything(seed)       # TODO: deterministic=False
    pil_images = []
    scores = []

    for top_k, top_p, images_num in [
        (2048, 0.995, images_per_res),
        (1536, 0.99, images_per_res),
        (1024, 0.99, images_per_res),
        (1024, 0.98, images_per_res),
        (512, 0.97, images_per_res),
        (384, 0.96, images_per_res),
        (256, 0.95, images_per_res),
        (128, 0.96, images_per_res)
    ]:
        _pil_images, _scores = generate_images(translated, tokenizer, dalle, vae, top_k=top_k, images_num=images_num, bs=batch_size, top_p=top_p)
        pil_images += _pil_images
        scores += _scores

    # upscale
    sr_images = super_resolution(pil_images, realesrgran)

    # save images
    for i, img in enumerate(sr_images):
        img.save(f'{image_save_dir}/{image_prefix}-{i}.jpg')
    
    print('Image batch saved.')