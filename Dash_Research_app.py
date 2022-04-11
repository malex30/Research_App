from dash import Dash, html, dcc, Input,Output
import plotly.express as px
import pandas as pd


## data sources to be used for this project

bacteria = pd.read_excel("data/Bacteria_Firebird_ALL_2_6_2022.xlsx")
bacteria.sort_values(by="Sample Date")


# dropping unnecessary columns from dataframe
bacteria.drop(columns=["Lab Test #","Lab #","Area","Center Name","Salesman","Lab Cost","Technician","Sample Type"])

# Initiation of Dash App
app = Dash(__name__)


well_name = bacteria['Location'].values.tolist()

successful_Bacteria_Program = '''
### Keys to a successful Biocide Program

1. Adequate contact time (enought time to kill)
2. Sufficient concentration for MEC "Minimum effective concentration
3. Treatment frequency (prevent microbial rebound)
4. Proactive monitoring (prevent issues from occuring)

'''

figB = px.bar(bacteria, x="Location", y="SRB", title="Bacteria Count")

srb_apb_MD = '''
### Sulfate Reducing Bacteria (SRB)

Sulphate-reducing bacteria (i.e. Desulphovibrio desulphuricans) existing in anaerobic conditions, can cause corrosion of iron. 
These bacteria are capable of living on a mineral diet and, as a result of their metabolism, they produce hydrogen sulphide which attacks iron and steel to form ferrous sulphide. 
Thus steel becomes pitted and cast iron becomes ‘graphitized’ (Cox, 1964), in which state it becomes soft.

# 

### Acid Producing Bacteria (APB)

Acid producing bacteria are capable of producing organic and inorganic acids which can significantly drop the pH beneath the biofilm into the acid range.  
Under these conditions, an acid-driven form of corrosion can occur causing metals to dissolve and concrete structures to lose integrity. 
These acidic metabolic by-products are produced under very reductive (oxygen free) environments. 
The sulfate reducing bacteria are often found within this nutrient rich, oxygen free environment.


'''

# Setting layout attributes
colors = {
    'background': "#09B495",
    'text': "#FFFFFF"
}

app.layout = html.Div(style={'backgroundColor':colors['background']},
    children=[
        html.H1(
            children="Well Site Inspection",
            style={
                'textAlign':'center',
                'color':colors['text']
                }
            ),
        html.H3(
            children="Analyzed report for a well pull, including historic data colleted for the well.",
            style={
                'textAlign':'center',
                'color':colors["text"]
            }
            ),
        dcc.Markdown(successful_Bacteria_Program),
        dcc.Dropdown(
            id="dropdown",
            options= well_name
        ),
        dcc.Graph(
           id="Bacteria",
           figure=figB,
           style={

           }
        ),
         dcc.Markdown(srb_apb_MD),
])

if __name__ == '__main__':
    app.run_server(debug=True)