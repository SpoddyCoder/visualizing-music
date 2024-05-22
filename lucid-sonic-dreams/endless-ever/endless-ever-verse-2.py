from lucidsonicdreams import LucidSonicDream

L = LucidSonicDream(song = '../../ai-music-viz/audio-source/endless-ever-24-verse2.wav',
                    pulse_audio = '../../ai-music-viz/audio-spleeted/endless-ever-24-verse2/drums.wav', # Ignore other pulse settings and use this audio track to pulse
                    motion_audio = '../../ai-music-viz/audio-source/endless-ever-24-verse2.wav',
                    contrast_audio = '../../ai-music-viz/audio-spleeted/endless-ever-24-verse2/bass.wav',
                    #  flash_audio = '../../ai-music-viz/audio-spleeted/buttercup/vocals.wav',
                    style = '../../ai-music-viz/cache/stylegan/cached-pkls/stylegan2/textures.pkl')

L.hallucinate(file_name = '../../ai-music-viz/lsd-renders/endless-ever/endless-ever-verse-2.mp4',
             fps = 60, # Actual video FPS. Was: fps=self.sr/self.frame_duration. frame_dur=int(sr/fps - (sr/fps % 64)) (sr = sample rate)
             speed_fpm = 20,
             truncation = 1.0, # Between 0 and 1

             pulse_react = 0.8,
             pulse_percussive = True, # If True while pulse_harmonic is False, pulse reacts to the audio's percussive elements.
             pulse_harmonic = False, # If True while pulse_percussive is False, pulse reacts to the audio's harmonic elements

             motion_react = 0.2,
             motion_percussive = False,
             motion_harmonic = True,
             motion_randomness = 0.02, # Between 0 and 1

             contrast_percussive = False,
             contrast_strength = 0.3,

             flash_percussive = False,
             flash_strength = 0.05,

             batch_size = 10,

             #custom_effects = [swirl_effect],

             save_frames = False # Does nothing now
             )