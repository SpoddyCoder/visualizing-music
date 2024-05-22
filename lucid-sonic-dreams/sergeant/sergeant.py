from lucidsonicdreams import LucidSonicDream

L = LucidSonicDream(song = '../../ai-music-viz/audio-source/sergeant-24.wav',
                    style = 'figure drawings')

L.hallucinate(file_name = '../../ai-music-viz/lsd-renders/sergeant-2.mp4',
             fps = 60, # Actual video FPS. Was: fps=self.sr/self.frame_duration. frame_dur=int(sr/fps - (sr/fps % 64)) (sr = sample rate)
             speed_fpm = 12,
             truncation = 0.6, # Between 0 and 1

             pulse_react = 0.62,
             pulse_percussive = True, # If True while pulse_harmonic is False, pulse reacts to the audio's percussive elements.
             pulse_harmonic = False, # If True while pulse_percussive is False, pulse reacts to the audio's harmonic elements

             motion_react = 0.4,
             motion_percussive = False,
             motion_harmonic = True,
             motion_randomness = 0.2, # Between 0 and 1

             contrast_percussive = True,
             contrast_strength = 0.86,

             flash_percussive = True,
             flash_strength = 0.05,

             #custom_effects = [swirl_effect],

             save_frames = False # Does nothing now
             )