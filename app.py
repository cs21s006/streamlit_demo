import os
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout='wide')
st.markdown('## AI4Bharat - Expressive TTS Samples')

samples_dir = 'expressive_ta_dravidian_subjective'
files = os.listdir(samples_dir)
emotions = ['happy', 'sad', 'angry', 'fear', 'disgust', 'surprise']
speakers = ['emotive_female', 'female', 'male']

def get_index(f):
    return int(f.split('_')[0])

def filter_speakers(files, speaker):
    filtered = []
    for file in files:
        if speaker == 'male':
            if ('male' in file and 'female' not in file) or 'emotive_female' in file:
                filtered.append(file)
        elif 'female' in file:
            filtered.append(file)
    return filtered

option = st.selectbox('Language: ', ['Kannada', 'Malayalam', 'Tamil', 'Telugu'])
if option == 'Tamil':
    st.markdown('### Tamil')
    cols = st.columns(8)
    cols[0].markdown('##### Index')
    cols[1].markdown('##### Speaker')
    cols[2].markdown('##### Emotion')
    cols[3].markdown('##### v2: Expressive Voice (Emotive)')
    cols[4].markdown('##### v2: Expressive Voice (Neutral)')
    cols[5].markdown('##### v2: IndicTTS Voice (Emotive)')
    cols[6].markdown('##### v2: IndicTTS Voice (Neutral)')
    cols[7].markdown('##### v1: IndicTTS Voice')
    st.markdown("""---""")
    ta_files = sorted([f for f in files if 'ta' in f])
    indices = sorted(list(set([get_index(f) for f in ta_files])))
    for index in indices:
        index_files = [f for f in ta_files if index == get_index(f)]
        for speaker in ['female', 'male']:
            speaker_files = filter_speakers(index_files, speaker)
            emotion = speaker_files[0].split('_')[-1].replace('.wav', '')
            cols = st.columns(8)
            cols[0].markdown(f'{index}')
            cols[1].markdown(f'**{speaker.capitalize()}**')
            cols[2].markdown(emotion)
            print(speaker_files)
        
            speaker_file = f'{str(index)}_ta_emotive_female_{emotion}.wav'
            with open(os.path.join(samples_dir, speaker_file), 'rb') as f:
                cols[3].audio(f.read())

            speaker_file = f'{str(index)}_ta_emotive_female_neutral.wav'
            with open(os.path.join(samples_dir, speaker_file), 'rb') as f:
                cols[4].audio(f.read())

            speaker_file = f'{str(index)}_ta_{speaker}_{emotion}.wav'
            with open(os.path.join(samples_dir, speaker_file), 'rb') as f:
                cols[5].audio(f.read())
            
            speaker_file = f'{str(index)}_ta_{speaker}_neutral.wav'
            with open(os.path.join(samples_dir, speaker_file), 'rb') as f:
                cols[6].audio(f.read())
            
            speaker_file = f'{str(index)}_ta_{speaker}_v1.wav'
            with open(os.path.join(samples_dir, speaker_file), 'rb') as f:
                cols[7].audio(f.read())

if option in ['Kannada', 'Malayalam', 'Telugu']:
    lang = {'Kannada': 'kn', 'Malayalam': 'ml', 'Telugu': 'te'}[option]
    st.markdown(f'### option')
    cols = st.columns(8)
    cols[0].markdown('##### Index')
    cols[1].markdown('##### Speaker')
    cols[2].markdown('##### Emotion')
    cols[3].markdown('##### v2: Expressive Voice (Emotive)')
    cols[4].markdown('##### v2: Expressive Voice (Neutral)')
    cols[5].markdown('##### v2: IndicTTS Voice (Emotive)')
    cols[6].markdown('##### v2: IndicTTS Voice (Neutral)')
    cols[7].markdown('##### v1: IndicTTS Voice')
    st.markdown("""---""")
    lang_files = sorted([f for f in files if lang in f])
    indices = sorted(list(set([get_index(f) for f in lang_files])))
    for index in indices:
        index_files = [f for f in lang_files if index == get_index(f)]
        print(index_files)
        for speaker in ['female', 'male']:
            speaker_files = filter_speakers(index_files, speaker)
            emotion = speaker_files[0].split('_')[-1].replace('.wav', '')
            if emotion == 'neutral':
                emotion = speaker_files[1].split('_')[-1].replace('.wav', '')
            
            cols = st.columns(8)
            cols[0].markdown(f'{index}')
            cols[1].markdown(f'**{speaker.capitalize()}**')
            cols[2].markdown(emotion)
            print(speaker_files)
        
            speaker_file = f'{str(index)}_{lang}_{speaker}_{emotion}.wav'
            with open(os.path.join(samples_dir, speaker_file), 'rb') as f:
                cols[5].audio(f.read())
            
            speaker_file = f'{str(index)}_{lang}_{speaker}_neutral.wav'
            with open(os.path.join(samples_dir, speaker_file), 'rb') as f:
                cols[6].audio(f.read())
            
            speaker_file = f'{str(index)}_{lang}_{speaker}_v1.wav'
            with open(os.path.join(samples_dir, speaker_file), 'rb') as f:
                cols[7].audio(f.read())
            
        






