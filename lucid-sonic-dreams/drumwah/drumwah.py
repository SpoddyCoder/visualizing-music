from lucidsonicdreams import LucidSonicDream

L = LucidSonicDream(song = '../../ai-music-viz/audio-source/drumwah.wav',
                    style = '../../ai-music-viz/cache/stylegan/cached-pkls/stylegan2/cat.pkl')

L.hallucinate(file_name = '../../ai-music-viz/lsd-renders/drumwah/drumwah-cats.mp4',
             fps = 60, # Actual video FPS. Was: fps=self.sr/self.frame_duration. frame_dur=int(sr/fps - (sr/fps % 64)) (sr = sample rate)
             speed_fpm = 6,
             truncation = 0.3, # Between 0 and 1

             pulse_react = 0.32,
             pulse_percussive = True, # If True while pulse_harmonic is False, pulse reacts to the audio's percussive elements.
             pulse_harmonic = False, # If True while pulse_percussive is False, pulse reacts to the audio's harmonic elements

             motion_react = 0.07,
             motion_percussive = False,
             motion_harmonic = True,
             motion_randomness = 0.02, # Between 0 and 1

             contrast_percussive = True,
             contrast_strength = 0.16,

             flash_percussive = False,
             flash_strength = 0.05,

             #custom_effects = [swirl_effect],

             save_frames = False # Does nothing now
             )