create table reporte (
    id_reporte int PRIMARY KEY AUTO_INCREMENT, 
    tipo_archivo varchar(10),
    archivo_dir varchar(255),
    estado varchar(255),
    resultado_dir varchar(255),
    nombre_reporte varchar(50),
    descripcion_reporte varchar(255),
    persona_encargada varchar(100)        
        
)