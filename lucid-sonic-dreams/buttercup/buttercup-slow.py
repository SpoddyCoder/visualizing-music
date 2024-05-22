from lucidsonicdreams import LucidSonicDream

L = LucidSonicDream(song = '../../ai-music-viz/audio-source/buttercup-24.wav',
                    #  pulse_audio = '../../ai-music-viz/audio-source/snippet.wav', # Ignore other pulse settings and use this audio track to pulse
                    #  motion_audio = '../../ai-music-viz/audio-spleeted/buttercup/bass.wav',
                    #  contrast_audio = '../../ai-music-viz/audio-spleeted/buttercup/other.wav',
                    #  flash_audio = '../../ai-music-viz/audio-spleeted/buttercup/vocals.wav',
                     style = 'modern art')
    

L.hallucinate(file_name = '../../ai-music-viz/lsd-renders/buttercup/buttercup-lsd-slow.mp4',
             fps = 60, # Actual video FPS. Was: fps=self.sr/self.frame_duration. frame_dur=int(sr/fps - (sr/fps % 64)) (sr = sample rate)
             speed_fpm = 4,
             truncation = 1.0, # Between 0 and 1

             pulse_react = 0.62,
             pulse_percussive = True, # If True while pulse_harmonic is False, pulse reacts to the audio's percussive elements.
             pulse_harmonic = False, # If True while pulse_percussive is False, pulse reacts to the audio's harmonic elements

             motion_react = 0.37,
             motion_percussive = False,
             motion_harmonic = True,
             motion_randomness = 0.2, # Between 0 and 1

             contrast_percussive = True,
             contrast_strength = 0.26,

             flash_percussive = False,
             flash_strength = 0.05,

             #custom_effects = [swirl_effect],

             save_frames = False # Does nothing now
             )