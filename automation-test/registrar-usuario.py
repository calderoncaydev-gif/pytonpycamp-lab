from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicializar el navegador
driver = webdriver.Chrome()

# Registrar usuario
driver.get("http://localhost/Xperience/public/register")
wait = WebDriverWait(driver, 10)
campo_nombre = wait.until(EC.visibility_of_element_located((By.ID, "name")))
campo_email = wait.until(EC.visibility_of_element_located((By.ID, "email")))
campo_password = wait.until(EC.visibility_of_element_located((By.ID, "password")))
campo_passwordconfirm = wait.until(EC.visibility_of_element_located((By.ID, "password-confirm")))
campo_nombre.send_keys("admin")
campo_email.send_keys("admin@gmail.com")
campo_password.send_keys("1")
campo_passwordconfirm .send_keys("1")
campo_passwordconfirm .send_keys(Keys.RETURN)

# Cerrar el navegador
driver.quit()
