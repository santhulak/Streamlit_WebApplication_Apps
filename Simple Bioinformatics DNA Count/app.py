import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

image = Image.open('DNA.jpg')
st.image(image,use_column_width=True,width=1000)
st.write ("""

# DNA Nucleoid Count Application

""")

#Enter DNA input sequence
st.header('Enter DNA Sequence')

seq_input ="DNA Query \nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

#Input text box for entering DNA sequence
sequence = st.text_area("Sequence Input", seq_input,height=150)
"sequence Input:\n"+ sequence

st.subheader("Split the Sequence")
#Split the sequence and display it in new line
sequence = sequence.splitlines()
sequence

#skip the first line >DNA Query 2
st.subheader("Skip the first line")
sequence = sequence[1:]
sequence

st.subheader("Join the Sequence")
sequence = ''.join(sequence)
sequence

st.subheader("DNA Nucleotide Count")
def DNA_nucleotide_count(seq):
    d = dict([
        ('A',seq.count('A')),
        ('T',seq.count('T')),
        ('G',seq.count('G')),
        ('C',seq.count('C'))
    ])
    return d

X = DNA_nucleotide_count(sequence)
X

st.subheader("Display the count with Names")
st.write('There are '+ str(X['A'])+' adenine (A)')
st.write('There are '+ str(X['T'])+' thymine (T)')
st.write('There are '+ str(X['G'])+' guanine (G)')
st.write('There are '+ str(X['C'])+' cytosine (C)')

st.subheader("Display Data as Dataframe")
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'nucleotide'})
st.write(df)

st.subheader("Display Barchart using Altair")
p = alt.Chart(df).mark_bar().encode(
    x = 'nucleotide',
    y = 'count'
)
p = p.properties(
    width=alt.Step(80) #controls the width of the bar
)

st.write(p)