# Proceso ETL — Ingesta de Documentos

## Fuente de datos
- Curso Azure (21 documentos)
- Formatos: PDF, DOCX
- Fuente: Google Drive proporcionado por el docente

## Pipeline de procesamiento
1. **Carga**: Lectura de archivos desde `data/raw/`
2. **Extracción**: Parsing según formato (pypdf, python-docx)
3. **Limpieza**: Eliminación de headers/footers repetitivos (si aplica)
4. **Chunking**: RecursiveCharacterTextSplitter con:
   - chunk_size: 1000 caracteres
   - chunk_overlap: 200 caracteres
5. **Metadatos**: documento, chunk_index
6. **Indexación**: Almacenamiento en la base vectorial vía vector_store_service

## Resultados
- Total de documentos procesados: 21
- Total de chunks generados: 883
- Modelo de embeddings: BAAI/bge-m3 (1024 dimensiones)
- Base vectorial: ChromaDB en `data/processed/chroma/`
