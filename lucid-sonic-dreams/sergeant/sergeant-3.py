from lucidsonicdreams import LucidSonicDream

L = LucidSonicDream(song = '../../ai-music-viz/audio-source/sergeant-24.wav',
                    style = '../../ai-music-viz/cache/stylegan/cached-pkls/stylegan2/figure-drawings.pkl')

L.hallucinate(file_name = '../../ai-music-viz/lsd-renders/sergeant-3.mp4',
             fps = 60, # Actual video FPS. Was: fps=self.sr/self.frame_duration. frame_dur=int(sr/fps - (sr/fps % 64)) (sr = sample rate)
             speed_fpm = 30,
             truncation = 0.5, # Between 0 and 1

             pulse_react = 0.6,
             pulse_percussive = True, # If True while pulse_harmonic is False, pulse reacts to the audio's percussive elements.
             pulse_harmonic = False, # If True while pulse_percussive is False, pulse reacts to the audio's harmonic elements

             motion_react = 0.08,
             motion_percussive = False,
             motion_harmonic = True,
             motion_randomness = 0.05, # Between 0 and 1

             contrast_percussive = False,
             contrast_strength = 0.3,

             flash_percussive = True,
             flash_strength = 0.05,

             batch_size = 10,

             #custom_effects = [swirl_effect],

             save_frames = False # Does nothing now
             )