from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicializar el navegador
driver = webdriver.Chrome()

# Iniciar sesión (reemplaza con tu código de inicio de sesión)
driver.get("http://localhost/Passarinho/public/login")
wait = WebDriverWait(driver, 10)
campo_email = wait.until(EC.visibility_of_element_located((By.ID, "email")))
campo_password = wait.until(EC.visibility_of_element_located((By.ID, "password")))
campo_email.send_keys("admin@gmail.com")
campo_password.send_keys("1")
campo_password.send_keys(Keys.RETURN)

# Navegar a la página de creación de tour
driver.get("http://localhost/Passarinho/public/admin/create-tour")

# Esperar hasta que los campos estén visibles
wait = WebDriverWait(driver, 10)
campo_codigo = wait.until(EC.visibility_of_element_located((By.NAME, "code")))
campo_nombre = wait.until(EC.visibility_of_element_located((By.NAME, "name")))
campo_imagen = wait.until(EC.visibility_of_element_located((By.NAME, "image")))
campo_precio = wait.until(EC.visibility_of_element_located((By.NAME, "price")))
campo_estado = wait.until(EC.visibility_of_element_located((By.NAME, "status")))
campo_itinerario = wait.until(EC.visibility_of_element_located((By.NAME, "itinerary")))
campo_descripcion = wait.until(EC.visibility_of_element_located((By.NAME, "description")))
#campo_categoria = wait.until(EC.visibility_of_element_located((By.NAME, "tour_category_id")))

# Rellenar los campos
campo_codigo.send_keys("1001")
campo_nombre.send_keys("Embalse del Yeso")
campo_imagen.send_keys("C:\\Users\\JOSE\\Desktop\\img\\la_serena.jpg")  # Reemplaza con la ruta de tu imagen
campo_precio.send_keys("100")
campo_estado.click()
campo_itinerario.send_keys("Itinerario del Tour")
campo_descripcion.send_keys("Descripción del Tour")

# Seleccionar la categoría del tour
#opciones_categoria = campo_categoria.find_elements(By.TAG_NAME, "option")
#for opcion in opciones_categoria:
#    if opcion.text == "Categoría":
#        continue
#    if opcion.text == "City tour":  # Reemplaza con el nombre de la categoría correcta
#        opcion.click()
#        break

# Enviar el formulario
campo_codigo.submit()

# Cerrar el navegador
driver.quit()
