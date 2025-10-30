import sys
import sqlite3
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView
import folium

class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Navegador Web")
        self.setGeometry(100, 100, 800, 600)

        # Crear un widget QWebEngineView
        self.webview = QWebEngineView()
        self.webview.setUrl(QUrl("file:///C:/Users/JOSE/OneDrive%20-%20INACAP/Portafolio/Proyectos_personales/EmprendeSoft/themes/browser/mapa_con_bd_descripcion.html"))

        # Agregar el widget QWebEngineView al diseño vertical
        layout = QVBoxLayout()
        layout.addWidget(self.webview)

        # Crear un formulario para la entrada de datos
        self.lat_label = QLabel("Latitud:")
        self.lat_input = QLineEdit()
        self.lon_label = QLabel("Longitud:")
        self.lon_input = QLineEdit()
        self.desc_label = QLabel("Descripción:")
        self.desc_input = QLineEdit()

        self.submit_button = QPushButton("Agregar Ubicación")
        self.submit_button.clicked.connect(self.add_location)

        self.reload_button = QPushButton("Recargar Mapa")
        self.reload_button.clicked.connect(self.update_map)

        layout.addWidget(self.lat_label)
        layout.addWidget(self.lat_input)
        layout.addWidget(self.lon_label)
        layout.addWidget(self.lon_input)
        layout.addWidget(self.desc_label)
        layout.addWidget(self.desc_input)
        layout.addWidget(self.submit_button)
        layout.addWidget(self.reload_button)

        # Crear un widget contenedor y establecer el diseño vertical
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Conectar la señal de clic del mapa a la función correspondiente
        self.webview.page().runJavaScript("map.addListener('click', handleMapClick);")
        self.webview.page().javaScriptConsoleMessage = self.handle_console_message

        # Crear la base de datos SQLite y la tabla si no existen
        self.create_database()

    def handle_console_message(self, level, message, lineNumber, sourceID):
        # Manejar los mensajes de la consola de JavaScript
        print("JavaScript console:", message)

    def create_database(self):
        # Conectar a la base de datos SQLite (creará el archivo si no existe)
        self.conn = sqlite3.connect("datos_mapa.db")
        self.cur = self.conn.cursor()

        # Crear la tabla si no existe
        #self.cur.execute("""CREATE TABLE IF NOT EXISTS ubicaciones (
        #                    id INTEGER PRIMARY KEY,
        #                    lat REAL,
        #                    lon REAL,
        #                    descripcion TEXT
        #                    )""")
        #self.conn.commit()

    def add_location(self):
        # Obtener los datos ingresados por el usuario
        lat = self.lat_input.text()
        lon = self.lon_input.text()
        desc = self.desc_input.text()

        # Insertar la ubicación en la base de datos
        self.cur.execute("INSERT INTO coordenadas (lat, lon, descripcion) VALUES (?, ?, ?)", (lat, lon, desc))
        self.conn.commit()

        # Limpiar los campos después de agregar la ubicación
        self.lat_input.clear()
        self.lon_input.clear()
        self.desc_input.clear()

        # Actualizar y mostrar el mapa
        self.update_map()


        print("Ubicación agregada a la base de datos")

    def update_fields(self, lat, lon, desc):
        # Actualizar los campos de latitud, longitud y descripción cuando se hace clic en el mapa
        self.lat_input.setText(str(lat))
        self.lon_input.setText(str(lon))
        self.desc_input.setText(str(desc))

    def update_map(self):
        # Recuperar las coordenadas y descripciones de la base de datos
        self.cur.execute("SELECT lat, lon, descripcion FROM coordenadas")
        coordenadas = self.cur.fetchall()

        # Crear un objeto de mapa con Folium
        mapa = folium.Map(location=[-33.45694, -70.64827], zoom_start=10)

        # Agregar marcadores para cada conjunto de coordenadas
        for coord in coordenadas:
            latitud, longitud, descripcion = coord
            try:
                latitud = float(latitud)
                longitud = float(longitud)
                texto_coordenada = f"Latitud: {latitud}<br>Longitud: {longitud}<br>Descripción: {descripcion}"
                folium.Marker([latitud, longitud], tooltip=texto_coordenada).add_to(mapa)
            except ValueError:
                print(f"Error: No se pudieron convertir los valores de latitud y longitud en números: {latitud}, {longitud}")

        # Guardar el mapa como un archivo HTML temporal
        mapa_file = "mapa_con_bd_descripcion.html"
        mapa.save(mapa_file)

        # Cargar el mapa HTML en el QWebEngineView
        self.webview.setUrl(QUrl.fromLocalFile(mapa_file))

        # Recargar la página HTML en el QWebEngineView para mostrar los cambios
        self.load_html()
        
    def load_html(self):
        # Cargar el archivo HTML en el QWebEngineView
        self.webview.setUrl(QUrl("file:///C:/Users/JOSE/OneDrive%20-%20INACAP/Portafolio/Proyectos_personales/EmprendeSoft/themes/browser/mapa_con_bd_descripcion.html"))
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BrowserWindow()
    window.show()
    sys.exit(app.exec_())
