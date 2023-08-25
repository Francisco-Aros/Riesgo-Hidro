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

st.title("Presentación web")

st.info(
    "La siguiente web presenta un total de 5 pestañas adicionales a ésta, en las cuales se pueden apreciar a través de diversos visualizadores web la situación actualizada de cada comuna que compone la Asociación Paisajes de Conservación para la Biodiversidad de la Región de Los Ríos."
)

#@st.cache_data()
#def get_data():
    # Cargar el archivo SHP en un objeto GeoDataFrame
 #   shp_path = "Localidades_Mafil_CamionesAljibes.shp"
  #  gdf = gpd.read_file(shp_path)
    #Cargar el segundo archivo shp de poligono en una objeto GeoDataFrame
   # shp_path3 = "Suelo_mafil_2014.shp"
    #gdf1 = gpd.read_file(shp_path3)
    # Cargar el segundo archivo SHP en otro objeto GeoDataFrame
 #   shp2_path = "APRMafil.shp"
  #  gdf_points = gpd.read_file(shp2_path)  # Corregir nombre de la variable
    #cargar tercer shp
   # shp3_path = "Derechos_Mafil_Comuna.shp"
    #gdf_points2 = gpd.read_file(shp3_path)
#    return gdf, gdf1, gdf_points, gdf_points2  # Corregir nombre de la variable


# Obtener los datos de los polígonos y puntos
#gdf, gdf1, gdf_points, gdf_points2 = get_data()  # Corregir nombre de la variable

#unique_values = gdf['Lt_entrega'].unique()
#print(unique_values)

#unique_values1 = gdf1['SUBUSO'].unique()
#print(unique_values1)

# Lista de caracteres especiales y sus correspondientes reemplazos
#caracteres_especiales = {'Ã': 'Ñ', 'Ã¡': 'a', 'Ã': 'i', 'Ã¡':'a'}
# Función para reemplazar caracteres especiales en un atributo
#def reemplazar_caracteres(atributo):
 #   for especial, reemplazo in caracteres_especiales.items():
  #      atributo = atributo.replace(especial, reemplazo)
   # return atributo

# Aplicar la función a todos los atributos que necesitas cambiar
#gdf1['SUBUSO'] = gdf1['SUBUSO'].apply(reemplazar_caracteres)
#gdf1['NOM_COM'] = gdf1['NOM_COM'].apply(reemplazar_caracteres)

# Guardar la capa modificada en un nuevo archivo shapefile
#ruta_salida = 'Suelo_mafil_2014_modificada1.shp'
#gdf1.to_file(ruta_salida)


# Crear un objeto Folium Map centrado en los datos de los polígonos
#m = folium.Map(location=[-39.8, -72.6], zoom_start=10, titles ='Stamen Terrain')

# Definir la paleta de colores para asignar un color único a cada valor único en 'Lt_entrega'
#color_palette = {
 #   1050.0: '#ffb4b4', #rosado
  #  2.0: '#ffa5a5',   
   # 3.0: '#ff9696',   
    #14000.0: '#ff8787',   
#    175.0: '#ff7878',  
 #   5.0: '#ff6969',   
  #  385.0: '#ff5a5a',  
   # 6.0: '#ff4b4b',
    #5600.0: '#ff3c3c',
#    6650.0: '#ff2d2d', 
 #   8050.0: '#ff1e1e', 
  #  13650.0: '#ff0f0f', 
   # 18200.0: '#ff0000',  # Rojo muy intenso
#}

# Definir la paleta de colores para asignar un color único a cada valor único en 'SUBUSO'
#color_palette1 = {
 #   'Ãadis HerbÃ¡ceos y Arbustivos': '#33a02c',
  #  'Bosque Mixto': '#53c963',
   # 'Bosque Nativo': '#33a02c',
    #'Cajas de RÃ­os': '#130dc0',
    #'Ciudades-Pueblos-Zonas Industriales': '#ad5914',
    #'Lago-Laguna-Embalse-Tranque':'#130dc0',
    #'Matorral':'#c4c726',
    #'Matorral-Pradera':'#c4c726',
    #'Matorral Arborescente':'#c4c726',
    #'Otros Terrenos HÃºmedos':'#130dc0',
    #'Plantaciones': '#ff0000',
    #'Praderas':'#c4c726',
    #'Playas y Dunas': '#bababa',
    #'RÃ­os':'#130dc0',
    #'RotaciÃ³n Cultivo-Pradera': '#ff3c3c',
    #'Terrenos de Uso AgrÃ­cola': '#ff3c3c',
    #'VegetaciÃ³n HerbÃ¡cea en Orilla':'#130dc0',
#}
# Función para asignar colores diferentes a cada atributo
#def style_function(feature):
  #  attribute = feature['properties']['Lt_entrega']
 #   return {'fillColor': color_palette.get(attribute, '#808081'), 'fillOpacity': 0.7, 'color': 'none'}

# Función para asignar colores diferentes a cada atributo de gdf1
#def style_function_gdf1(feature):
  #  attribute = feature['properties']['SUBUSO']
 #   return {'fillColor': color_palette1.get(attribute, '#808081'), 'fillOpacity': 0.7, 'color': 'none'}

# Obtener los datos de los polígonos y puntos
#gdf, gdf1, gdf_points, gdf_points2 = get_data()

# Crear un objeto FeatureGroup de Folium para los polígonos
#poligonos_group = folium.FeatureGroup(name='Zonas de entrega de agua potable mediante camiones aljibes')
#poligonos_group = folium.FeatureGroup(name='Zonas de entrega de agua potable mediante camiones aljibes')
#folium.GeoJson(gdf,
     #          tooltip=folium.GeoJsonTooltip(fields=['NOM_LOCALI', 'Lt_entrega'], aliases=['Nombre de localidad', 'Litros entregados']),
    #           style_function=style_function,
   #            name='Zonas de entrega de agua potable mediante camiones aljibes',
  #             show= True
 #              ).add_to(m)

#suelo_group = folium.FeatureGroup(name='Uso de suelo Los Lagos año 2014')
#folium.GeoJson(gdf1,
     #          tooltip=folium.GeoJsonPopup(fields=['SUBUSO', 'ESTRUCTURA'], aliases= ['Uso Tierra', 'Estructura']),
    #           style_function= style_function_gdf1,
   #            name='Uso de suelo Los Lagos año 2014',
  #             show= False
 #              ).add_to(m)

# Crear un objeto FeatureGroup de Folium para los puntos
#puntos_group = folium.FeatureGroup(name='APR Los Lagos')
#puntos_group = folium.FeatureGroup(name='APR Los Lagos')
#folium.GeoJson(gdf_points,
   #            tooltip=folium.GeoJsonTooltip(fields=['Nombre__of', 'Beneficiar'], aliases=['Nombre', 'Beneficiarios']),
    #           name='APR Los Lagos',
  #             show= False
 #              ).add_to(m)

#Crear un objetoi FeaturGroup de Folium para la segunda capa de puntos
#derechos_group = folium.FeatureGroup(name='Derechos de aprovechamiento de aguas, comuna de Los Lagos')
#folium.GeoJson(gdf_points2,
  #             tooltip=folium.GeoJsonTooltip(fields=['TipoDerech', 'Naturaleza', 'UsodelAgua', 'Clasificac'], aliases=['Tipo de derecho', 'Naturaleza de derecho', 'Uso del agua', 'Clasificación']),
 #              name= 'Derechos de aprovechamiento de aguas, comuna de Los Lagos',
#               show= False
#               ).add_to(m)

# Agregar los FeatureGroups al mapa
#poligonos_group.add_to(m)
#suelo_group.add_to(m)
#puntos_group.add_to(m)
#derechos_group.add_to(m)




# Agregar los FeatureGroup al mapa
#m.add_child(poligonos_group)
#m.add_child(puntos_group)

# Crear el control de capas agrupadas

#control = folium.LayerControl()

#control.add_to(m)

# Mostrar el mapa en Streamlit utilizando folium_static
#folium_static(m, width=800, height=600)

st.write("Los invitamos a recorrer cada una de las pestañas de cada comuna y finalmente una última pestaña referente al Territorio de acción correspondiente a la asociación. ")

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