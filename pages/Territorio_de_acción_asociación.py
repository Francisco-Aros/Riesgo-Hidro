import geopandas as gpd
import folium
from folium import CustomIcon
from streamlit_folium import folium_static
import streamlit as st
from streamlit.components.v1 import html



st.sidebar.write("En el territorio de acción de la asociación existen 43 localidades que reciben ayuda de agua potable en caminones aljibes a través del municipio, entregandose un total de 6.088.350 litros semanales.")
st.sidebar.write("En total existen a junio del presente año 1.684 Derechos de aprovechamiento de agua en el territorio")
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
    "En el siguiente mapa cuenta con un selector de capas para poder activar/desactivar las que desee. En este ejemplo se cuenta con los sectores de las cuatro comunas pertenecientes a la asociación y en cuales de ellos existe entrega de agua potable a través de camiones aljibes, ya sean estos por parte de un camión municipal o de la gobernación regional."
)

@st.cache_data()
def get_data():
    # Cargar el archivo SHP en un objeto GeoDataFrame
    shp_path = "Localidades_Accion_CamionesAljibes.shp"
    gdf = gpd.read_file(shp_path)
    # Cargar el segundo archivo SHP en otro objeto GeoDataFrame
    shp2_path = "SSR_accion.shp"
    gdf_points = gpd.read_file(shp2_path)  # Corregir nombre de la variable
    #cargar tercer sho
    shp3_path = "Derechos_territorio_acciom.shp"
    gdf_points2 = gpd.read_file(shp3_path)
    shp4_path = "Territorio_accion14Copy2.shp"
    gdf1 = gpd.read_file(shp4_path)
    shp_path4 = "incendios_accion.shp"
    gdf_points3 = gpd.read_file(shp_path4)

    return gdf, gdf1, gdf_points, gdf_points2,gdf_points3  # Corregir nombre de la variable


# Obtener los datos de los polígonos y puntos
gdf, gdf1, gdf_points, gdf_points2,gdf_points3 = get_data()  # Corregir nombre de la variable

unique_values = gdf['Lt_entrega'].unique()
print(unique_values)

# Crear un objeto Folium Map centrado en los datos de los polígonos
m = folium.Map(location=[-39.7621, -72.6444], zoom_start=9)

# Definir la paleta de colores para asignar un color único a cada valor único en 'Lt_entrega'
color_palette = {
    350.0: '#fff0e9', #rosado
    1000.0: '#ffece3',   
    1050.0: '#fee7dc',   
    2000.0: '#fee3d6',   
    3200.0: '#fedccd',  
    3850.0: '#fdd4c2',   
    5600.0: '#fdccb8',  
    8050.0: '#fcc4ad',
    9100.0: '#fcbca2',
    9900.0: '#fcb398', 
    18200.0: '#fcaa8d', 
    36400.0: '#fca183',
    42700.0: '#fc9879',
    45500.0: '#fc8f6f',
    54000.0: '#fc8666',
    54600.0: '#fb7d5d',
    56400.0: '#fb7555',
    63700.0: '#fb6c4c',
    72000.0: '#f96245',
    100100.0: '#f6573e',
    117000.0: '#f44d38',
    135000.0: '#f14331',
    171000.0: '#ed392b',
    216000.0: '#e53128',
    254450.0: '#dd2a25',
    261000.0: '#d52221',
    306000.0: '#cd1a1e',
    324000.0: '#c5161c',
    342000.0: '#bc141a',
    382200.0: '#b31218',
    609700.0: '#aa1016',
    648000.0: '#9c0d14',
    702000.0: '#8a0912',
    747000.0: '#ff0000',  # Rojo muy intenso
}

# Función para asignar colores diferentes a cada atributo
def color_palette1(attribute):
    if attribute in ['Bosque Nativo Achaparrado Abierto', 'Bosque Nativo Achaparrado Denso', 'Bosque Nativo Achaparrado Semidenso','Bosque Nativo Adulto Abierto', 'Bosque Nativo Adulto Denso', 'Bosque Nativo Adulto Semidenso', 'Bosque Nativo Adulto-Renoval Denso','Bosque Nativo Adulto-Renoval Semidenso', 'Renoval Abierto', 'Renoval Denso','Renoval Semidenso']:
        return '#124016'
    elif attribute in ['Exoticas asilvestradas', 'Planta joven recien cosechada','Plantacion']:
        return '#b6011e'
    elif attribute in ['Bosque Nativo-exoticas asilvestradas','Bosque Nativo-exoticas asilvestradas Denso','Bosque Nativo-exoticas asilvestradas semidenso', 'Bosque Nativo-plantacion abierto', 'Bosque Nativo-plantacion denso', 'Bosque Nativo-plantacion semidenso']:
        return '#9cbb3e'
    elif attribute in ['Cajas de rios', 'Glaciares','Lago-Laguna-Embalse-Tranque','Nieves','Rios','Vegas','Vegetacion Herbacea en Orilla']:
        return '#1e27ce'
    elif attribute in ['Ciudades-Pueblos-Zonas Industriales','Mineria Industrial']:
        return '#634421'
    elif attribute == 'Lago-Laguna-Embalse-Tranque':
        return '#1e27ce'
    elif attribute in ['Matorral Abierto','Matorral Denso','Matorral Semidenso','Matorral Arborescente Abierto','Matorral Arborescente Semidenso','Matorral Pradera Abierto','Matorral Pradera Semidenso','Estepa patagonica','Praderas Perennes']:
        return '#a8aa25'
    elif attribute == ['Playas y Dunas', 'Corridas de Lava y Escoriales','Derrumbes sin vegetacion','Otros terrenos sin vegetacion']:
        return '#969696'
    elif attribute in ['Rotacion de cultivos-praderas', 'Terrenos de Uso Agricola']:
        return '#cfd919'
    else:
        return 'gray'

# Función para asignar colores diferentes a cada atributo
def style_function(feature):
    attribute = feature['properties']['Lt_entrega']
    return {'fillColor': color_palette.get(attribute, '#808081'), 'fillOpacity': 0.9, 'color': 'none'}

# Función para asignar colores diferentes a cada atributo
def style_function1(feature):
    attribute = feature['properties']['USO_TIERRA']
    return {'fillColor': color_palette1(attribute), 'fillOpacity': 1.0, 'color': 'none'}

# Obtener los datos de los polígonos y puntos

gdf, gdf1, gdf_points, gdf_points2, gdf_points3 = get_data()

# Crear un objeto FeatureGroup de Folium para los polígonos
#poligonos_group = folium.FeatureGroup(name='Zonas de entrega de agua potable mediante camiones aljibes')
folium.GeoJson(gdf,
               tooltip=folium.GeoJsonTooltip(fields=['NOM_COMUNA','NOM_LOCALI', 'Lt_entrega'], aliases=['Comuna','Nombre de localidad', 'Litros entregados']),
               style_function=style_function,
               name='Zonas de entrega de agua potable mediante camiones aljibes',
               show= True
               ).add_to(m)

# Crear un objeto FeatureGroup de Folium para los puntos
#puntos_group = folium.FeatureGroup(name='APR Los Lagos')
folium.GeoJson(gdf_points,
               tooltip=folium.GeoJsonTooltip(fields=['Nombre__of', 'Beneficiar'], aliases=['Nombre', 'Beneficiarios']),
               name='APRS',
               show= False
               ).add_to(m)

#Crear un objetoi FeaturGroup de Folium para la segunda capa de puntos
folium.GeoJson(gdf_points2,
               tooltip=folium.GeoJsonTooltip(fields=['TipoDerech', 'Naturaleza', 'UsodelAgua', 'Clasificac'], aliases=['Tipo de derecho', 'Naturaleza de derecho', 'Uso del agua', 'Clasificación']),
               name= 'Derechos de aprovechamiento de aguas',
               show= False
               ).add_to(m)

folium.GeoJson(gdf1,
               name='Uso de suelo al año 2014',
               tooltip=folium.GeoJsonTooltip(fields=['NOM_COM','USO_TIERRA'], aliases=['Comuna', 'Uso de suelo al 2014']),
               style_function=style_function1,
               show=False# no se moestrara la capa al cargar la página, de lo contrario si es que se desea que se pueda visualizar desde un inicio debe ser con el comando "overlay=True"
               ).add_to(m)

#Crear un objetoi FeaturGroup de Folium para la segunda capa de puntos
folium.GeoJson(gdf_points3,
               tooltip=folium.GeoJsonTooltip(fields=['Name', 'BeginTime', 'EndTime'], aliases=['Nombre', 'Inicio', 'Termino']),
               name= 'Incendios temporada 2022-2023 Territorio de acción',
               show= False
               ).add_to(m)



# Agregar los FeatureGroup al mapa
#m.add_child(poligonos_group)
#m.add_child(puntos_group)

# Crear el control de capas agrupadas

control = folium.LayerControl()

control.add_to(m)

# Mostrar el mapa en Streamlit utilizando folium_static
folium_static(m, width=700, height=450)


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