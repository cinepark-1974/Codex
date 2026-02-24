import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.io as pio            # Plotly 차트를 이미지로 변환하기 위해 필요
import OpenAI as Chatgpt4
from PyPDF2 import PdfReader
import json
import io
import re

st.title("블루진픽처스 시나리오 닥터")
st.write("BLUE JEANS PICTURES SCRIPT DOCTOR 1.0")
