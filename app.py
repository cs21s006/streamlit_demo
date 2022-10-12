import os
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

st.set_page_config(layout="wide")

st.markdown("## AI4Bharat - IndicTTS")

cols = st.columns(6)
cols[0].markdown('**Language**')
cols[1].markdown('**Speaker**')
cols[2].markdown('**AI4Bharat**')
cols[3].markdown('**GT**')
cols[4].markdown('**Vakyansh**')
cols[5].markdown('**Donlab**')

languages = os.listdir('demo')

language2title = {
    'as': 'Assamese',
    'bn': 'Bengali',
    'brx': 'Bodo',
    'gu': 'Gujarati',
    'hi': 'Hindi',
    'kn': 'Kannada',
    'ml': 'Malayalam',
    'mni': 'Manipuri',
    'mr': 'Marathi',
    'or': 'Odia',
    'raj': 'Rajasthani',
    'ta': 'Tamil',
    'te': 'Telugu'
}

for language in sorted(languages):
    language_dir = os.path.join('demo', language)
    files = os.listdir(language_dir)
    # cols2 = st.columns(9)
    
    cols = st.columns(6)
    file = None
    for file in files:
        if 'female' in file and file.endswith('_a.wav'):
            break
        else:
            file = None
    if file is not None:
        cols[0].markdown(language2title[language])
        cols[1].markdown('Female')
        filepath = os.path.join(language_dir, file)
        for idx, append in enumerate('abcd'):
            sample_path = filepath.replace('_a.wav', f'_{append}.wav')
            if os.path.exists(sample_path):
                cols[idx+2].audio(sample_path)
            else:
                cols[idx+2].markdown('-')

    cols = st.columns(6)
    file = None
    for file in files:
        if 'male' in file and not 'female' in file and file.endswith('_a.wav'):
            break
        else: 
            file = None
    if file is not None:
        cols[0].markdown(language2title[language])
        cols[1].markdown('Male')
        filepath = os.path.join(language_dir, file)
        for idx, append in enumerate('abcd'):
            sample_path = filepath.replace('_a.wav', f'_{append}.wav')
            if os.path.exists(sample_path):
                cols[idx+2].audio(sample_path)
            else:
                cols[idx+2].markdown('-')

    


# option = st.selectbox(
#      'Select a language:',
#      ('Tamil', 'Hindi', 'Marathi')
#      )

# if option == 'Tamil':
#     ### START: Tamil
#     st.markdown("### Tamil")

#     models = [
#         'AI4Bharat|Male|FastPitch+HiFiGAN|samples/samples_indictts_ta_male_fastpitch', 
#         'AI4Bharat|Multi|FastPitch+HiFiGAN|samples/samples_googletts_ta_multi_fastpitch', 
#         'Vakyansh|Male|GlowTTS+HiFiGAN|samples/samples_vakyansh_ta_male_glowtts', 
#         'DonLab|Male|Tacotron2+WaveGlow|samples/samples_donlab_ta_male_tacotron2'
#     ]

#     texts = [
#         '1) செஸ் ஒலிம்பியாட் போட்டியை சென்னை முதல் முறையாக நடத்திய பிறகு, ஜவாஹர்லால் நேரு உள்விளையாட்டு அரங்கில் பிரமாண்டமான முறையில் அதன் நிறைவு விழா நடைபெற்றது.',
#         '2) இலங்கையின் முன்னாள் ஜனாதிபதி கோட்டாபய ராஜபக்ஷ, தாய்லாந்திற்கு செல்லவுள்ளதாக ராய்ட்டர்ஸ் செய்தி வெளியிட்டுள்ளது.',
#         '3) காமன்வெல்த் போட்டிகளில் இந்தியாவுக்கு மூன்றாவது தங்கப் பதக்கத்தை பெற்று தந்துள்ளார் பளுதூக்கும் வீரர் அச்சிண்டா செயுலி.',
#         '4) தமிழ்நாட்டின் ஆதிச்சநல்லூர் அகழாய்வில் தங்க நெட்டிப்பட்டம், வெண்கல பொருட்கள் கண்டெடுக்கப்பட்டுள்ளன.',
#         '5) ஈலோன் மஸ்க்கின் ஸ்பேஸ் எக்ஸ் நிறுவனம் ஏராளமான செயற்கைக்கோள்களை வட்டப்பாதைக்கு அனுப்பிக்கொண்டிருக்கிறது.'
#     ]


#     cols = st.columns(len(texts)+2)
#     cols[0].markdown('**Model**')
#     cols[1].markdown('**Speaker**')
#     for j, text in enumerate(texts):
#         cols[j+2].markdown(f'**Text Prompt {j+1}**')

#     for i, model in enumerate(models):
#         cols = st.columns(len(texts)+2)
#         cols[0].markdown(f"{model.split('|')[0]}: {model.split('|')[2]}")
#         cols[1].markdown(model.split('|')[1])
#         for j, text in enumerate(texts):
#             with open(f"{model.split('|')[3]}/{j+1}.wav", 'rb') as file:
#                 cols[j+2].audio(file.read())

#     st.markdown("#### Text Prompts:")
#     for j, text in enumerate(texts):
#         st.markdown(text)
#     ### End: Tamil

# elif option == 'Hindi':
#     ### START: Hindi
#     st.markdown("### Hindi")

#     models = [
#         'AI4Bharat|Male|FastPitch+HiFiGAN|samples/samples_indictts_hi_male_fastpitch', 
#         'Vakyansh|Male|GlowTTS+HiFiGAN|samples/samples_vakyansh_hi_male_glowtts', 
#         'DonLab|Male|Tacotron2+WaveGlow|samples/samples_donlab_hi_male_tacotron2'
#     ]

#     texts = [
#         "1) बिहार, राजस्थान और उत्तर प्रदेश से लेकर हरियाणा, मध्य प्रदेश एवं उत्तराखंड में सेना में भर्ती से जुड़ी 'अग्निपथ स्कीम' का विरोध जारी है.",
#         "2) संयुक्त अरब अमीरात यानी यूएई ने बुधवार को एक फ़ैसला लिया कि अगले चार महीनों तक वो भारत से ख़रीदा हुआ गेहूँ को किसी और को नहीं बेचेगा.",
#         "3) वाराणसी: ज्योतिष के छात्र अब बनेंगे आर्किटेक्ट, करेंगे इंटीरियर कोर्स.",
#         "4) महाकुम्भ को भव्य और दिव्य बनाने की तैयारियां शुरू, पर्यावरण संरक्षण पर होगा फोकस.",
#         "5) ब्याज दरों में वृद्धि के बावजूद नहीं घट रही मारुति की कारों की मांग, कई लाख ऑर्डर पैंडिंग."
#     ]


#     cols = st.columns(len(texts)+2)
#     cols[0].markdown('**Model**')
#     cols[1].markdown('**Speaker**')
#     for j, text in enumerate(texts):
#         cols[j+2].markdown(f'**Text Prompt {j+1}**')

#     for i, model in enumerate(models):
#         cols = st.columns(len(texts)+2)
#         cols[0].markdown(f"{model.split('|')[0]}: {model.split('|')[2]}")
#         cols[1].markdown(model.split('|')[1])
#         for j, text in enumerate(texts):
#             with open(f"{model.split('|')[3]}/{j+1}.wav", 'rb') as file:
#                 cols[j+2].audio(file.read())

#     st.markdown("#### Text Prompts:")
#     for j, text in enumerate(texts):
#         st.markdown(text)
#     ### End: Hindi

# elif option == 'Marathi':
#     ### START: Marathi
#     st.markdown("### Marathi")

#     models = [
#         'AI4Bharat|Male|FastPitch+HiFiGAN|samples/samples_indictts_mr_male_fastpitch', 
#         #'Vakyansh|Male|GlowTTS+HiFiGAN|samples/samples_vakyansh_mr_male_glowtts', 
#         'DonLab|Male|Tacotron2+WaveGlow|samples/samples_donlab_mr_male_tacotron2'
#     ]

#     texts = [
#         "1) मविआ सरकार अल्पमतात आल्यानंतर अनेक निर्णय घेतले: मुख्यमंत्री एकनाथ शिंदे यांचा आरोप.",
#         "2) वर्ध्यात भदाडी नदीच्या पुलावर कार डिव्हायडरला धडकून भीषण अपघात, दोघे गंभीर जखमी.", 
#         "3) मुंबई पोलिसांना पाकिस्तानातून धमकीचा मेसेज, विरारमधून एक संशयित ताब्यात, पोलिसांकडून चौकशी सुरु.",
#         "4) पुण्याची अनुष्का पारेख बनली कमी वेळात वजनदार डेडलिफ्ट उचलणारी भारतातील सर्वात 'तरुण' मुलगी.",
#         "5) 'हॉटसीट'वर बसलेल्या तरुणीने सांगितले मुंबई लोकलमधील किस्से; ऐकून बिग बी देखील झाले खुश."
#     ]


#     cols = st.columns(len(texts)+2)
#     cols[0].markdown('**Model**')
#     cols[1].markdown('**Speaker**')
#     for j, text in enumerate(texts):
#         cols[j+2].markdown(f'**Text Prompt {j+1}**')

#     for i, model in enumerate(models):
#         cols = st.columns(len(texts)+2)
#         cols[0].markdown(f"{model.split('|')[0]}: {model.split('|')[2]}")
#         cols[1].markdown(model.split('|')[1])
#         for j, text in enumerate(texts):
#             with open(f"{model.split('|')[3]}/{j+1}.wav", 'rb') as file:
#                 cols[j+2].audio(file.read())

#     st.markdown("Note: Vakyansh - Marathi model is not accessible")
#     st.markdown("#### Text Prompts:")
#     for j, text in enumerate(texts):
#         st.markdown(text)
#     ### End: Marathi