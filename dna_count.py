#Import Libraries:
from turtle import width
import streamlit as st
import pandas as pd
import altair as alt
import random
from PIL import Image


#Page Title:

image = Image.open("img/dna_banner.jpg")

st.title("DNA Nucleotide Count")
st.text("Counting the nucleotide composition of query DNA")
st.markdown("***")
st.image(image,use_column_width=True)


#Input Text Box:

st.subheader("Enter DNA Sequence")

#Random DNA Sequence Generator:
# dna = ['A','C','G','T']
# bases = int(st.number_input('How many bases? (Between 10 - 1000)',10,1000))
# random_sequence = ''
# for i in range(0,bases):
#     random_sequence+=random.choice(dna)


sequence_input = ''
sequence = st.text_area("Sequence input",sequence_input, height=150)


#Print DNA Input sequence:
st.subheader("Input (DNA Query)")
sequence

#DNA nucleotide count:
st.subheader("Output (DNA Nucleotide Count)")



### 1. Print Dictionary:
st.subheader('*1. Print dictionary:*')

def DNA_nucleotide_count(seq):
    d = dict(
        [
            ('A',seq.count('A')),
            ('C',seq.count('C')),
            ('G',seq.count('G')),
            ('T',seq.count('T'))
        ]
    )
    return d

X = DNA_nucleotide_count(sequence)

X

XA = X['A']
XC = X['C']
XG = X['G']
XT = X['T']

### 2. Print Text:
st.subheader('*2. Print text:*')

st.write(f'There are {XA} adenine (A)')
st.write(f'There are {XC} cytosine (C)')
st.write(f'There are {XG} guanine (G)')
st.write(f'There are {XT} thymine (T)')

### 3. Display DataFrame:
st.subheader('*3. Display DataFrame:*')

df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0:'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns= {'index':'nucleotide'})
st.write(df)

### 4. Display Bar Chart using Altair:
st.subheader('*4. Display Bar Chart:*')

p = alt.Chart(df).mark_bar().encode(
    x = 'nucleotide',
    y = 'count'
)
p = p.properties(
    width=alt.Step(80)
)
st.write(p)