from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicializar el navegador
driver = webdriver.Chrome()

# Iniciar sesión (reemplaza con tu código de inicio de sesión)
driver.get("http://localhost/Xperience/public/login")
wait = WebDriverWait(driver, 10)
campo_email = wait.until(EC.visibility_of_element_located((By.ID, "email")))
campo_password = wait.until(EC.visibility_of_element_located((By.ID, "password")))
campo_email.send_keys("admin@gmail.com")
campo_password.send_keys("1")
campo_password.send_keys(Keys.RETURN)

# Esperar a que se cargue la página de creación de categoría
driver.get("http://localhost/Xperience/public/admin/create-category")

# Esperar hasta que los campos estén visibles
wait = WebDriverWait(driver, 10)
campo_nombre = wait.until(EC.visibility_of_element_located((By.NAME, "name")))
campo_imagen = wait.until(EC.visibility_of_element_located((By.NAME, "image")))
campo_estado = driver.find_element(By.NAME, "status")

# Rellenar los campos
campo_nombre.send_keys("City tour")
campo_imagen.send_keys("C:\\Users\\JOSE\\Desktop\\img\\la_serena.jpg")# Reemplaza con la ruta de tu imagen

# Enviar el formulario
campo_nombre.submit()

# Cerrar el navegador
driver.quit()
