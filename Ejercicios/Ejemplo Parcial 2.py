def creaDic():
    categorias = set()
    
    try:
        oferta = open("oferta_gastronomica.txt", "rt")
        
        for linea in oferta:
            nroid, nombre, categ, cocina, amb, tel, hour, direc, barrio = linea.split(";")
            if categ != "categoria":
                categorias.add(categ)
        
        infolocales = dict.fromkeys(categorias, 0)
        
        for linea in oferta:
            nroid, nombre, categ, cocina, amb, tel, hour, direc, barrio = linea.split(";")
            infolocales[categ] += 1
    
    except OSError as mensaje:
        print(mensaje)
    except FileNotFoundError as mensaje:
        print(f"No se encuentra el archivo: {mensaje}")
    
    finally:
        try:
            oferta.close()
        except NameError:
            pass
        
    return infolocales

def listaCategoria(cat):
    
    try:
        oferta = open("oferta_gastronomica.txt", "rt")  
        locales = []
        for linea in oferta:
            nroid, nombre, categ, cocina, amb, tel, hour, direc, barrio = linea.split(";")
            barriolimp = barrio.rstrip("\n").ljust(20)
            nom = nombre.ljust(20)
            telefono = tel.ljust(20)
            
            info = f"{nombre}{barrio}{tel}"
            
            if cat == categ:
                locales.append(info)
                
    except OSError as mensaje:
        print(mensaje)
    except FileNotFoundError as mensaje:
        print(f"No se encuentra el archivo: {mensaje}")
    
    finally:
        try:
            oferta.close()
        except NameError:
            pass
    
    return locales
        
#main

print(creaDic())