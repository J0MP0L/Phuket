import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import os
from flask import Flask

# สร้าง Flask server
server = Flask(__name__)

# สร้าง Dash app และเชื่อมโยงกับ server
app = dash.Dash(__name__, server=server, external_stylesheets=[dbc.themes.BOOTSTRAP])

# ฟังก์ชันสำหรับโหลดไฟล์ HTML
def load_html(file_name):
    file_path = os.path.join(os.getcwd(), file_name)
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

# โหลดกราฟ HTML ที่มีอยู่แล้ว
EOS_map = load_html('figg.html')
fig2 = load_html('เนื้อที่เปรียบเทียบกับผลผลิต.html')
fig3 = load_html('เนื้อที่เปรียบเทียบกับผลผลิตต่อไร่.html')
fig4 = load_html("logarea.html")
fig5 = load_html("percent.html")

# Layout ของ Dashboard
app.layout = html.Div([
    dbc.Container([
        # Title
        html.H1("Rice Cultivation Potential in Southern Thailand", className="my-4"),

        # สร้างแท็บ (Tabs) สำหรับหน้ากราฟ
        dcc.Tabs(id="tabs", value='tab-1', children=[
            dcc.Tab(label='Introduction', value='tab-1'),
            dcc.Tab(label='EOS MAP', value='tab-2'),
            dcc.Tab(label='Comparing Area', value='tab-3'),
            dcc.Tab(label='Comparing Output', value='tab-4'),
        ], className="mb-4"),

        # ส่วนที่แสดงกราฟตามแท็บที่เลือก
        html.Div(id='tabs-content')
    ])
])

# Callback สำหรับการเปลี่ยนเนื้อหาตามแท็บที่เลือก
@app.callback(
    dash.dependencies.Output('tabs-content', 'children'),
    [dash.dependencies.Input('tabs', 'value')]
)
def render_content(tab):
    if tab== "tab-1":
        return html.Div([
            html.H3("Phuket"),
            html.Img(src='/assets/phuket-beach.jpg', style={'width': '40%', 'border-radius': '15px', 'display': 'block', 'margin': 'auto'}),
            dcc.Markdown("""
- **ด้านเรื่องของทางภูมิอากาศ** \n        เนื่องด้วยทางด้านจังหวัดในทางด้านสภาพอากาศในการปลูกข้าวเราจะสามารถเห็นได้ ว่าทางภูเก็ตนั้นได้ รับเรื่องของทางด้านอิทธิพลทางด้านเรื่องของ มรสุม ทั้ง 2 อย่างคือมรสุมทางด้านตะวันออกเฉียงเหนือ เเละทางด้านตะวันตกเฉียงใต้โดยทางด้าน ตกเฉียงใต้จะทำให้ฝนตกนั้นเกิดตลอดทั้งปี ส่วน ในทางด้านตะวันออกเฉียงเหนือนั้นจะเป็นทางด้านคความเเห้งเเล้งมากกว่า โดยเราจะสามารถมองรวมได้ว่าทางตะวันตกเฉียง ใต้ได้รับอิธิพลมากที่สุดจากการที่ผนตก นอกจากนี้ ทำให้ทางภูเก็ตนั้นสามารถปลูกทางด้านข้าวได้มีประสิทธิภาพเนื่องจากการเกิด ความชุ่มชื้นในตัวดินตลอดทั้งปีจากมรสุมตะวันตกเฉียงใต้ 
- **ด้านเรื่องดิน** \n       เราสามารถทำการบอกได้ว่าดินของทาด้านภูเก็ตเราสามารถพบได้ว่าทางด้าน ดินที่มีความเหมาะสมสําหรับปลูกข้าวเนื้อที่ประมาณ 20 836 ไร่ โดยคิดเป็นพื้นที่จำนวนร้อยละ 5.85 ส่วนพื้นที่ นอกนั้นอาจจะปลูกข้าวได้ เเต่ไม่เหมาะสมเท่ากับพื้นที่นี้  เเต่ก็สามารถทำการปลูกข้าวได้ โดยดินพวกนี้อาจมีส่วนประกอบเป็นทางด้านเรื่องของตัวทางดินทราย 
- **ด้านเรื่องของแหล่งน้ำ** \n      แหล่งน้ำเป็นทรัพยากรที่สำคัญทั้งในด้านการรักษาคุณภาพน้ำ สภาพแวดล้อมและการวางแผนพัฒนา ภูเก็ตมีพื้นที่แหล่งน้ำทั้งสิ้น 24 แหล่ง คลอง บางใหญ่เป็นสายน้ำแห่งเดียวในภูเก็ตที่มีน้ำไหลตลอดทั้งปีและยังมีลำธาร ต่างๆ  นอกจากนี้ยังมีคลองที่ไม่ไหลตลอดทั้งปีอีก 118 สาย เเละยังมีทางด้านเรื่องของ อ่างเก็บน้ำบางวาดเป็นอ่างเก็บน้ำที่สำคัญเพียงแห่งเดียวของภูเก็ต จึงส่งผลให้ภูเก็ตขาดแคลนแหล่งนำจืดที่มีคุณภาพสูงที่นำมาใช้บริโภครวมทั้ง เพื่อการพัฒนาจังหวัดภูเก็ต  นอกจากนี้สามารถใชเพื่อที่ทำการเพาะปลุกทางด้านการเกษตรได้เป็นตน้
""")
        ])

    elif tab == 'tab-2':
        return html.Div([
            html.H3("แผนที่ EOS"),
            html.P("กราฟเเสดงการผลผลิตต่อเนื้อที่โดยสงขลาจะมีผลผลิตต่อเนื้อที่สูงที่สุดสูงถึง 499 รองลงมาเป็นภูเก็ตสูงถึง 493 และตามด้วยนครศรีธรรมราชที่สูงถึง 485"),
            html.Iframe(srcDoc=EOS_map, style={"height": "1500px", "width": "100%"}),
        ])
    elif tab == 'tab-3':
        return dbc.Row([
            dbc.Col([
                html.H4("การเปรียบเทียบพื้นที่ในรูปของ logarithm"),
                html.P("จะเห็นได้ว่าภูเก็ตมีเนื้อที่น้อยที่สุดเมื่อเทียบกับจังหวัดอื่น เเต่กลับมีผลผลิตต่อเนื้อที่สูงเป็นอันดับ2"),
                html.Iframe(srcDoc=fig4, style={"height": "1000px", "width": "100%"}),
            ], width=6),
            dbc.Col([
                html.H4("กราฟแสดงสัดส่วนของพื้นที่การเกษตร"),
                html.P("กราฟนี้จะเห็นได้ว่าแม้ภูเก็ตจะมีเนื้อที่ที่น้อยมากเเต่สามารถสร้างผลผลิตต่อเนื้อที่ได้สูงกว่าจังหวัดอื่นๆ"),
                html.Iframe(srcDoc=fig5, style={"height": "1000px", "width": "100%"}),
            ], width=6),
        ])
    elif tab == 'tab-4':
        return dbc.Row([
            dbc.Col([
                html.H4("กราฟเปรียบเทียบเนื้อที่กับผลผลิต"),
                html.P("จะเห็นได้ว่าความสัมพันธ์ระหว่างเนื้อที่กับผลผลิตรวมค่อนข้างมีความสัมพันธ์ที่เป็น linear เเต่ไม่สามารถบอกได้ถึงศักยภาพการปลูกข้าว"),
                html.Iframe(srcDoc=fig2, style={"height": "1000px", "width": "100%"}),
            ], width=6),
            dbc.Col([
                html.H4("กราฟเปรียบเทียบเนื้อที่กับผลผลิตต่อไร่"),
                html.P("กราฟนี้จะเห็นได้ว่าแม้ภูเก็ตจะมีเนื้อที่ที่น้อยมากเเต่สามารถสร้างผลผลิตต่อเนื้อที่ได้สูงกว่าจังหวัดอื่นๆ"),
                html.Iframe(srcDoc=fig3, style={"height": "1000px", "width": "100%"}),
            ], width=6),
        ])

# รันแอป
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8001))  # ใช้ค่าจากตัวแปรสภาพแวดล้อม PORT
    app.run(host="0.0.0.0", port=port)


