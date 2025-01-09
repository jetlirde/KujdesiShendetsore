import streamlit as st

def sugjero_diete(arsye):
    dieta = {
        "Humbje peshe": "Sugjerohet një dietë e pasur me proteina, fibra dhe shumë pak karbohidrate.",
        "Shtim peshe": "Sugjerohet një dietë e pasur me kalori, proteina dhe yndyra të shëndetshme.",
        "Energjia": "Sugjerohet një dietë e balancuar me karbohidrate, proteina dhe yndyra.",
    }
    return dieta.get(arsye.lower(), "Arsye e panjohur, ju lutem provoni përsëri.")

def sugjero_ushtrime(qellimi):
    ushtrime = {
        "Humbje peshe": "Sugjerohet: ecje e shpejtë, vrapim, yoga dhe ushtrime aerobike.",
        "Shtim muskujsh": "Sugjerohet: peshëngritje, ushtrime rezistence dhe stërvitje HIIT.",
        "Relaksim": "Sugjerohet: yoga, meditimi dhe shëtitje të lehta.",
    }
    return ushtrime.get(qellimi.lower(), "Qëllim i panjohur, ju lutem provoni përsëri.")

def keshilla_per_bmi(bmi):
    if bmi < 18.5:
        return "Ju jeni nën peshë. Konsultohuni me një specialist! Ushqehuni më shpesh dhe përfshini më shumë proteina dhe karbohidrate në dietën tuaj.", "red"
    elif 18.5 <= bmi < 24.9:
        return "Ju keni peshë normale. Vazhdoni një stil jetese të shëndetshëm!", "green"
    elif 25 <= bmi < 29.9:
        return "Ju jeni mbipeshë. Ushtrimet dhe dieta e kontrolluar janë të rekomanduara. Shmangni ushqimet me shumë sheqer dhe yndyrë.", "orange"
    else:
        return "Ju keni obezitet. Konsultohuni me një specialist! Filloni me aktivitete të lehta fizike si ecja dhe kufizoni kaloritë në dietën tuaj.", "red"

def konsultime_shtese(bmi):
    if bmi >= 25:
        return (
            "**Këshilla Shtesë:**\n"
            "- Konsumoni më shumë perime dhe fruta.\n"
            "- Kufizoni ushqimet e përpunuara dhe të skuqura.\n"
            "- Provoni të ecni të paktën 30 minuta çdo ditë.\n"
            "- Pini shumë ujë gjatë ditës."
        )
    return ""

st.title("Kujdesi Shëndetësor 🩺")
st.sidebar.title("Plotësoni të dhënat tuaja")

emri = st.sidebar.text_input("Emri juaj")
mosha = st.sidebar.number_input("Mosha juaj", min_value=1, max_value=120, step=1)
pesha = st.sidebar.number_input("Pesha juaj (kg)", min_value=1.0, step=0.1)
gjatesia = st.sidebar.number_input("Gjatësia juaj (m)", min_value=0.5, step=0.01)

if st.sidebar.button("Llogarit BMI"):
    bmi = pesha / (gjatesia ** 2)
    st.write(f"**Indeksi juaj i masës trupore (BMI):** {bmi:.2f}")
    keshilla, color = keshilla_per_bmi(bmi)
    st.markdown(f"<p style='color:{color};'>{keshilla}</p>", unsafe_allow_html=True)
    shtese = konsultime_shtese(bmi)
    if shtese:
        st.write(shtese)

qellimi = st.selectbox("Cili është qëllimi juaj?", ["humbje peshe", "shtim peshe", "energjia"])
if st.button("Sugjerime"):
    st.write("**Dieta e rekomanduar:**")
    st.write(sugjero_diete(qellimi))
    st.write("**Ushtrimet e rekomanduara:**")
    st.write(sugjero_ushtrime(qellimi))
