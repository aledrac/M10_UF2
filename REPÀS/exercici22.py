import xml.etree.ElementTree as ET

def generar_xml():
    root = ET.Element("students")
    for i in range(1, 6):
        student = ET.SubElement(root, "student")
        name = ET.SubElement(student, "name")
        surname = ET.SubElement(student, "surname")
        email = ET.SubElement(student, "email")
        dni = ET.SubElement(student, "dni")
        student.set("id", str(i))
        name.text = f"Nombre{i}"
        surname.text = f"Apellido{i}"
        email.text = f"email{i}@ejemplo.com"
        dni.text = f"DNI{i}12345678Z"

    tree = ET.ElementTree(root)
    tree.write("students.xml")

    with open("students.xml", "r") as file:
        xml_content = file.read()
        print(xml_content)

generar_xml()
