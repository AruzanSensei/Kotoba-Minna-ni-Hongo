import streamlit as st
import pandas as pd

# Membuat data dalam bentuk dictionary
data = {
    'Kata': [
        'わたし', 'あなた', 'あの ひと', 'あの かた', 'ーさん', '～ちゃん', '～じん', 
        'せんせい', 'きょうし', 'がくせい', 'かいしゃいん', 'しゃいん', 'ぎんこういん', 
        'いしゃ', 'けんきゅうしゃ', 'だいがく', 'びょういん', 'だれ（どなた）', '～さい', 
        'なんさい（おいくつ）', 'はい', 'いいえ', 'はじめまして', 'からきました', 
        'どうぞよろしくおねがいします', 'しつれいですが', 'おなまえは?', 
        'こちらは 〜さんです', 'イギリス', 'インド', 'ブラジル', 'にほん', 
        'タイ', 'ドイツ', 'ちゅうごく'
    ],
    'Kanji': [
        '私', '', 'あの人', 'あの方', '', '', '', 
        '先生', '教師', '学生', '会社員', '社員', '銀行員', 
        '医者', '研究者', '大学', '病院', '', '～歳', 
        '何歳', '', '', '', '', '', '', '',
        '', '', '', '', '', '', '', ''
    ],
    'Arti': [
        'Saya', 'Anda', 'Orang itu/beliau', 'Orang itu/beliau', 'Saudara-bapak-ibu', 'Akhiran untuk panggilan anak-anak', 
        'Orang', 'Guru, dosen, pengajar', 'Guru, dosen', 'Pelajar', 'Karyawan perusahaan', 
        'Karyawan perusahaan', 'Karyawan bank', 'Dokter', 
        'Peneliti', 'Universitas', 'Rumah sakit', 'Siapa', '--tahun', 'Berapa umurnya', 
        'Ya', 'Tidak, bukan', 'Perkenalkan', 'Datang dari, Berasal dari', 'Salam kenal', 
        'Permisi, maaf', 'Siapa namanya?', 'Ini bapak〜/ Ini ibu, sdr.', 'Inggris', 'India', 
        'Brasil', 'Jepang', 'Thailand', 'Jerman', 'Cina'
    ],
    'Romaji': [
        'watashi', 'anata', 'ano hito', 'ano kata', '-san', '-chan', '-jin', 
        'sensei', 'kyoushi', 'gakusei', 'kaishain', 'shain', 'ginkouin', 
        'isha', 'kenkyuusha', 'daigaku', 'byouin', 'dare (donata)', '-sai', 
        'nansai (oikutsu)', 'hai', 'iie', 'hajimemashite', 'kara kimashita', 
        'douzo yoroshiku onegaishimasu', 'shitsureidesuga', 'onamae wa?', 
        'kochira wa 〜san desu', 'Igirisu', 'Indo', 'Burajiru', 'Nihon', 
        'Tai', 'Doitsu', 'Chuugoku'
    ],
    'Keterangan': [
    '', '', '', 'lebih sopan dari あの ひと', ' akhiran untuk mengekspresikan kesopanan yang diletakkan di belakang nama orang', 'akhiran yang dipakai untuk anak laki-laki dan anak perempuan sebagai pengganti 〜 さん yang diletakkan di belakang nama anak', 'akhiran yang menyatakan warga negara. contoh: アメリカじん (orang amerika)', 'tidak dipakai jika tidak menyebut pekerjaan sendiri', '', '', '',
    'dipakai bersama nama perusahaan', '', '', '', '', '', '', '', '', '', 
    '', 'ucapan salam pada waktu pertama kali berkenalan', '', 
    'ucapan terakhir untuk perkenalan diri', 
    'digunakan ketika bertanya tentang hal yang pribadi seperti nama, alamat, dan sebagainya', 
    '', '', '', '', '', '', '', '', ''
    ]
}

df = pd.DataFrame(data)

st.write("untuk pengalaman yang lebih baik gunakan fitur 'tampilan dekstop' di chrome, dan masuk ke setting (titik 3 pada pojok kanan, sebelah gambar kucing) lalu aktifkan 'wide mode' :)")

# Opsi untuk menampilkan Romaji atau tidak
show_kata = st.checkbox('Tampilkan Kata', value=True)
show_arti = st.checkbox('Tampilkan Arti', value=True)
show_kanji = st.checkbox('Tampilkan Kanji', value=False)
show_romaji = st.checkbox('Tampilkan Romaji', value=False)
show_keterangan = st.checkbox('Tampilkan Keterangan', value=False)

st.title("Kosakata - Bab 1")

# Menampilkan tabel dengan atau tanpa kolom Romaji
columns_to_show = []
if show_kata:
    columns_to_show.append('Kata')
if show_kanji:
    columns_to_show.append('Kanji')
if show_arti:
    columns_to_show.append('Arti')
if show_romaji:
    columns_to_show.append('Romaji')
if show_keterangan:
    columns_to_show.append('Keterangan')

# Menampilkan tabel sesuai dengan kolom yang dipilih
if columns_to_show:
    st.table(df[columns_to_show])
else:
    st.write("Tidak ada kolom yang dipilih untuk ditampilkan.")

st.write("by aru")