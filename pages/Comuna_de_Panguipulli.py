import geopandas as gpd
import folium
from streamlit_folium import folium_static
import streamlit as st

st.set_page_config(
    page_title="Visualizador",
    page_icon=":globe_with_meridians:",
    layout="wide"
)

st.sidebar.write("")
st.sidebar.write("En la comuna de Panguipulli existen 66 localidades que reciben ayuda de agua potable en caminones aljibes a través del municipio, entregandose un total de 19.998.000 litros semanales")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")

# Crea dos columnas en el sidebar
col1, col2 = st.sidebar.columns([1,7])





css = '''
<style>
    [data-testid='stSidebarNav'] > ul {
        min-height: 54vh;
    }
</style>
'''

st.markdown(css, unsafe_allow_html=True)

st.title("Ejemplo de capas de información en visualizador web")

st.info("En el siguiente mapa cuenta con un selector de capas para poder activar/desactivar las que desee. En este ejemplo se cuenta con los sectores de la comuna de Paguipulli y en cuales de ellos existe entrega de agua potable a través de camiones aljibes, ya sean estos por parte de un camión municipal o de la gobernación regional."
)

@st.cache_data() 
def get_data():
# Cargar el archivo SHP en un objeto GeoDataFrame
    shp_path = "suelo_pangui2014_Clip.shp"
    gdf = gpd.read_file(shp_path)
    shp1_path = "Entidades_Panguipulli_CamionesALjibes.shp"
    gdf1 = gpd.read_file(shp1_path)
    shp2_path = "APR_Panguipulli.shp"
    gdf_points = gpd.read_file(shp2_path)  # Corregir nombre de la variable
     #cargar tercer sho
    shp3_path = "Derechos_Panguipulli_comunaCopy.shp"
    gdf_points2 = gpd.read_file(shp3_path)
    shp_path4 = "IncendiosPanguipulliTem2022-2023.shp"
    gdf_points3 = gpd.read_file(shp_path4)
    return gdf, gdf1, gdf_points, gdf_points2, gdf_points3
    


# Crear un objeto Folium Map centrado en los datos de los polígonos
m = folium.Map(location=[-39.67, -71.98], zoom_start=9)

# Función para asignar colores diferentes a cada atributo
# Definir la paleta de colores para asignar un color único a cada valor único en 'Lt_entrega'
color_palette = {
    9000.0: '#fff1ea', #rosado muy claro
    18000.0: '#ffece3', 
    27000.0: '#fee8dd',   
    36000.0: '#fee3d6',   
    54000.0: '#feddcf',   
    63000.0: '#fdd6c4',  
    72000.0: '#fdceba',   
    90000.0: '#fdc6af',  
    99000.0: '#fcbea5',
    117000.0: '#fcb59b',
    135000.0: '#fcad91', 
    153000.0: '#fca486',
    161000.0: '#fc9b7c',
    162000.0: '#fc9272',
    170000.0: '#fc8a6a',
    171000.0: '#fc8161', 
    216000.0: '#fb7959', 
    225000.0: '#fb7050',
    261000.0: '#fa6748',
    270000.0: '#f85d42',
    306000.0: '#f5533b',
    324000.0: '#f34935',
    342000.0: '#f03f2f',
    387000.0: '#ea372a',
    423000.0: '#e32f27',
    531000.0: '#db2824',
    612000.0: '#d32020',
    639000.0: '#cc191d',
    648000.0: '#c3161b',
    702000.0: '#ba1419',
    747000.0: '#b11218',
    918000.0: '#a91016',
    1125000.0: '#9b0d14',
    1602000.0: '#890811',
    1161000.0: '#78040f',  # Rojo muy intenso
}

# Función para asignar colores diferentes a cada atributo
def color_palette1(attribute):
    if attribute in ['Bosque Nativo', 'Ñadis Herbáceos y Arbustivos']:
        return '#124016'
    elif attribute == 'Plantaciones':
        return '#b6011e'
    elif attribute in ['Bosque Mixto']:
        return '#9cbb3e'
    elif attribute in ['Cajas de Ríos', 'Otros Terrenos Húmedos', 'Ríos', 'Vegetaciión Herbácea en Orilla']:
        return '#1e27ce'
    elif attribute in ['Ciudades-Pueblos-Zonas Industriales']:
        return '#634421'
    elif attribute == 'Lago-Laguna-Embalse-Tranque':
        return '#1e27ce'
    elif attribute in ['Matorral', 'Matorral Arborescente', 'Matorral-Pradera', 'Praderas']:
        return '#a8aa25'
    elif attribute == ['Playas y Dunas']:
        return '#969696'
    elif attribute in ['Rotaciión Cultivo-Pradera', 'Terrenos de Uso Agrícola', 'Rotacií³n Cultivo-Pradera']:
        return '#cfd919'
    else:
        return 'gray'


# Función para asignar colores diferentes a cada atributo
def style_function1(feature):
    attribute = feature['properties']['Lt_entrega']
    return {'fillColor': color_palette.get(attribute, '#808081'), 'fillOpacity': 0.9, 'color': 'none'}

# Función para asignar colores diferentes a cada atributo
def style_function(feature):
    attribute = feature['properties']['SUBUSO']
    return {'fillColor': color_palette1(attribute), 'fillOpacity': 1.0, 'color': 'none'}

# Agregar los datos de los polígonos al mapa
# Obtener los datos de los polígonos y agregarlos al mapa
gdf, gdf1, gdf_points, gdf_points2, gdf_points3= get_data()

# Crear un objeto FeatureGroup de Folium para los polígonos
#poligonos_group = folium.FeatureGroup(name='Zonas de entrega de agua potable mediante camiones aljibes')
folium.GeoJson(gdf1,
               tooltip=folium.GeoJsonTooltip(fields=['NOMBRE_LOC', 'Lt_entrega'], aliases=['Nombre de localidad', 'Litros entregados']),
               style_function=style_function1,
               name='Zonas de entrega de agua potable mediante camiones aljibes',
               show= True
               ).add_to(m)

folium.GeoJson(gdf,
               name='Uso de suelo en Panguipulli al año 2014',
               tooltip=folium.GeoJsonTooltip(fields=['NOM_COM','SUBUSO'], aliases=['Comuna', 'Uso de suelo al 2014']),
               style_function=style_function,
               show=False# no se moestrara la capa al cargar la página, de lo contrario si es que se desea que se pueda visualizar desde un inicio debe ser con el comando "overlay=True"
               ).add_to(m)

folium.GeoJson(gdf_points,
               tooltip=folium.GeoJsonTooltip(fields=['Nombre__of', 'Beneficiar'], aliases=['Nombre', 'Beneficiarios']),
               name='APR Panguipulli',
               show= False
               ).add_to(m)

#Crear un objetoi FeaturGroup de Folium para la segunda capa de puntos
folium.GeoJson(gdf_points2,
               tooltip=folium.GeoJsonTooltip(fields=['TipoDerech', 'Naturaleza', 'UsodelAgua', 'Clasificac'], aliases=['Tipo de derecho', 'Naturaleza de derecho', 'Uso del agua', 'Clasificación']),
               name= 'Derechos de aprovechamiento de aguas, comuna de Panguipulli',
               show= False
               ).add_to(m)

#Crear un objetoi FeaturGroup de Folium para la segunda capa de puntos
folium.GeoJson(gdf_points3,
               tooltip=folium.GeoJsonTooltip(fields=['Name', 'BeginTime', 'EndTime'], aliases=['Nombre', 'Inicio', 'Termino']),
               name= 'Incendios temporada 2022-2023 Comuna de Panguipulli',
               show= False
               ).add_to(m)



# Crear el control de capas agrupadas

control = folium.LayerControl()

control.add_to(m)


# Mostrar el mapa en Streamlit utilizando folium_static
folium_static(m, width=800, height=450)



def main():
# Estilo CSS para anclar en la parte inferior
    st.markdown(
            """
            <style>
            .footer {
                position: fixed;
                left: 0;
                bottom: 0;
                width: 100%;
                background-color: #000000;
                padding: 2px;
                text-align: center;
            }
            .footer p {
            font-size: 12px; /* Ajusta el tamaño de la letra */
            line-height: 1.2; /* Ajusta el espacio entre líneas */
            margin: 0; /* Elimina el margen alrededor del párrafo */
            color: #ffffff; /* Cambia el color del texto a blanco */
            }
            .footer a {
            font-size: 15px; /* Ajusta el tamaño del hipervínculo */
            color: #1443E4; /* Cambia el color del hipervínculo a blanco */
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        # Agrega una división con la clase 'footer'
    st.markdown(
            """
            <div class="footer">
                <p>Web diseñada y desarrollada por Francisco Javier Aros Muñoz</p>
                <a href="mailto:franciscoarosmunoz@gmail.com">franciscoarosmunoz@gmail.com</a>
            </div>
            """,
            unsafe_allow_html=True
        )
    
if __name__ == '__main__':
    main() 