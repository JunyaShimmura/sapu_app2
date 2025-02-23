import streamlit as st

# Session State にテキストデータを保存 streamlitはボタン押すとリロードするからsession管理
if "text_data" not in st.session_state:
    st.session_state.text_data =""  #初期化
text_data ="テキスト"
with st.form(key='profile_form'):
    name = st.text_input('名前')
    address = st.text_input('住所')
    age_category = st.radio(
    '年齢層',
    ('子供18歳未満','大人18歳以上'))
    hobby = st.multiselect(
        '趣味',
        ('スポーツ','読書','アニメ','映画'))
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')
    if submit_btn:
        st.text(f'ようこそ！{name}さん！{address}に送信しました。')
        st.text(f'年齢層:{age_category} ')
        st.text(f'趣味：{",".join(hobby)}')
    # ダウンロードするテキストデータ
        st.session_state.text_data = f"{name},{address},{age_category},{hobby}"
#詳しくは、Streamlit inputウィジェット ▶︎ https://docs.streamlit.io/library/api...

#音声ファイルをアップロード
uploadedFile = st.file_uploader("音声ファイルをアップロードしてください",type=["mp3","wav","ogg"])
#アップロードされたら処理
if uploadedFile is not None:
    #ファイル表示
    st.audio(uploadedFile, format="audio/mp3")
    st.success("音声ファイルをアップロードしました")

#ダウンロード処理 
st.download_button(
    label="テキストをダウンロード",
    data=st.session_state.text_data,
    file_name="downloadTxt.txt",
    mime="text/plain"
) 

