import geopandas as gpd
import folium
from folium import CustomIcon
from streamlit_folium import folium_static
import streamlit as st
from streamlit.components.v1 import html



st.sidebar.write("")
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
col1, col2 = st.sidebar.columns([1, 7])

css = '''
<style>
    [data-testid='stSidebarNav'] > ul {
        min-height: 54vh;
    }
</style>
'''

st.markdown(css, unsafe_allow_html=True)

st.title("Ejemplo de capas de información en visualizador web")

st.info(
    "En el siguiente mapa cuenta con un selector de capas para poder activar/desactivar las que desee. En este ejemplo se cuenta con los sectores de la comuna de Los Lagos y en cuales de ellos existe entrega de agua potable a través de camiones aljibes, ya sean estos por parte de un camión municipal o de la gobernación regional."
)

@st.cache_data()
def get_data():
    # Cargar el archivo SHP en un objeto GeoDataFrame
    shp_path = "Entidades_LosLagos_CamionesALjibes.shp"
    gdf = gpd.read_file(shp_path)
    # Cargar el segundo archivo SHP en otro objeto GeoDataFrame
    shp2_path = "LosLagos.shp"
    gdf_points = gpd.read_file(shp2_path)  # Corregir nombre de la variable
    #cargar tercer sho
    shp3_path = "Derechos_comuna_LLagos.shp"
    gdf_points2 = gpd.read_file(shp3_path)
    #cargar cuarto shp
    shp_path3 = "suelo_LLAgos_2014.shp" 
    gdf1 = gpd.read_file(shp_path3)
    #cargar info de 5to shp
    shp_path4 = "Incendios_L_LagosTem2022-2023.shp"
    gdf_points3 = gpd.read_file(shp_path4)
    return gdf, gdf_points, gdf_points2, gdf1,gdf_points3  # Corregir nombre de la variable


# Obtener los datos de los polígonos y puntos
gdf, gdf_points, gdf_points2, gdf1, gdf_points3 = get_data()  # Corregir nombre de la variable

unique_values = gdf['Lt_entrega'].unique()
print(unique_values)

# Crear un objeto Folium Map centrado en los datos de los polígonos
m = folium.Map(location=[-39.8, -72.6], zoom_start=10, tiles='Stamen Terrain')

# Definir la paleta de colores para asignar un color único a cada valor único en 'Lt_entrega'
color_palette = {
    350.0: '#ffede5', #rosado
    9100.0: '#fee6da',   
    18200.0: '#fedccd',  
    18220.0: '#fdcfbb', 
    36400.0: '#fcc1a9',   
    45500.0: '#fcb398',  
    54600.0: '#fca486',   
    63700.0: '#fc9575',  
    91000.0: '#fc8666',
    92750.0: '#fb7757',
    100100.0: '#fb6949',
    118300.0: '#f6573e',
    163800.0: '#f24633', 
    164500.0: '#ea372a',
    203350.0: '#dd2a25', 
    254450.0: '#d01d1f',
    265500.0: '#c2161b',
    382200.0: '#b31218',
    497000.0: '#a20e15',
    609700.0: '#850711',  # Rojo muy intenso
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
def style_function(feature):
    attribute = feature['properties']['Lt_entrega']
    return {'fillColor': color_palette.get(attribute, '#808081'), 'fillOpacity': 0.9, 'color': 'none'}

# Función para asignar colores diferentes a cada atributo
def style_function1(feature):
    attribute = feature['properties']['SUBUSO']
    return {'fillColor': color_palette1(attribute), 'fillOpacity': 0.7, 'color': 'none'}

# Obtener los datos de los polígonos y punto

# Obtener los datos de los polígonos y puntos
gdf, gdf_points, gdf_points2, gdf1, gdf_points3 = get_data()

# Crear un objeto FeatureGroup de Folium para los polígonos
#poligonos_group = folium.FeatureGroup(name='Zonas de entrega de agua potable mediante camiones aljibes')
folium.GeoJson(gdf,
               tooltip=folium.GeoJsonTooltip(fields=['NOMBRE_ENT', 'Per_afecta', 'Lt_entrega', 'Cant_seman'], aliases=['Nombre de localidad', 'Personas afectadas','Litros entregados', 'Cantidad de veces por semana']),
               style_function=style_function,
               name='Zonas de entrega de agua potable mediante camiones aljibes',
               show= True
               ).add_to(m)

# Crear un objeto FeatureGroup de Folium para los puntos
#puntos_group = folium.FeatureGroup(name='APR Los Lagos')
folium.GeoJson(gdf_points,
               tooltip=folium.GeoJsonTooltip(fields=['Nombre__of', 'Beneficiar'], aliases=['Nombre', 'Beneficiarios']),
               name='APR Los Lagos',
               show= False
               ).add_to(m)

#Crear un objetoi FeaturGroup de Folium para la segunda capa de puntos
folium.GeoJson(gdf_points2,
               tooltip=folium.GeoJsonTooltip(fields=['TipoDerech', 'Naturaleza', 'UsodelAgua', 'Clasificac'], aliases=['Tipo de derecho', 'Naturaleza de derecho', 'Uso del agua', 'Clasificación']),
               name= 'Derechos de aprovechamiento de aguas, comuna de Los Lagos',
               show= False
               ).add_to(m)

folium.GeoJson(gdf1,
               name='Uso de suelo en Los Lagos al año 2014',
               tooltip=folium.GeoJsonTooltip(fields=['NOM_COM','SUBUSO'], aliases=['Comuna', 'Uso de suelo al 2014']),
               style_function=style_function1,
               show=False# no se moestrara la capa al cargar la página, de lo contrario si es que se desea que se pueda visualizar desde un inicio debe ser con el comando "overlay=True"
               ).add_to(m)

#Crear un objetoi FeaturGroup de Folium para la segunda capa de puntos
folium.GeoJson(gdf_points3,
               tooltip=folium.GeoJsonTooltip(fields=['Name', 'BeginTime', 'EndTime'], aliases=['Nombre', 'Inicio', 'Termino']),
               name= 'Incendios temporada 2022-2023 Comuna de Los Lagos',
               show= False
               ).add_to(m)




# Agregar los FeatureGroup al mapa
#m.add_child(poligonos_group)
#m.add_child(puntos_group)

# Crear el control de capas agrupadas

control = folium.LayerControl()

control.add_to(m)

# Mostrar el mapa en Streamlit utilizando folium_static
folium_static(m, width=800, height=600)


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
