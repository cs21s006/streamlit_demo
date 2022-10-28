import os

languages = os.listdir('demo')
ISO2language = {
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

row_template = '''
<tr>
    <th scope="row">_language</th>
    <td>_speaker</td>
    <td>_a</td>
    <td>_b</td>
    <td>_d</td>
    <td>_c</td>
</tr>
'''

# <audio controls>
#   <source src="horse.ogg" type="audio/ogg">
#   <source src="horse.mp3" type="audio/mpeg">
#   Your browser does not support the audio tag.
# </audio>

def format_row(language, speaker, samples):
    if len(samples) == 0:
        return ''
    row = row_template
    row = row.replace('_language', ISO2language[language])
    for sample in samples:
        append = sample.split('_')[-1].replace('.wav', '')
        row = row.replace(f'<td>_{append}</td>', f'<td><audio controls><source src="demo/{language}/{sample}" type="audio/wav"></audio></td>')
        row = row.replace('_speaker', speaker)
    for append in ['_a', '_b', '_c', '_d']:
        row = row.replace(f"<td>{append}</td>", '<td></td>')
    return row

rows = []
for language in sorted(languages):
    sample_dir = os.path.join('demo/', language)
    samples = sorted(os.listdir(sample_dir))
    samples_female = [s for s in samples if 'female' in s]
    samples_male = [s for s in samples if 'male' in s and not 'female' in s]
    row = format_row(language, 'Female', samples_female)
    rows.append(row)
    row = format_row(language, 'Male', samples_male)
    rows.append(row)
rows = '\n'.join(rows)

body = f'''
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.1.3/dist/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
    <title>AI4Bharat Models</title>
  </head>
  <body>
    <table class="table">
    <thead>
        <tr>
        <th scope="col">Language</th>
        <th scope="col">Speaker</th>
        <th scope="col">AI4Bharat</th>
        <th scope="col">Ground Truth</th>
        <th scope="col">DON Lab</th>
        <th scope="col">Vakyansh</th>
        </tr>
    </thead>
    <tbody>
        {rows}
    </tbody>
    </table>
    <!-- Optional JavaScript -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.3/dist/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.1.3/dist/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
  </body>
</html>
'''

print(body, file=open('demo.html', 'w'))