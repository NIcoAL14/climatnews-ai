# 🌍 Proyecto Hackathon - Cambio Climático

## 📝 Nombre del Proyecto

**ClimateNews AI**

## 🔍 ¿En qué consiste?

Es una plataforma web que utiliza inteligencia artificial para analizar noticias sobre el cambio climático en tiempo real de múltiples fuentes. El sistema identifica tendencias, genera nubes de palabras, clasifica noticias por impacto ambiental y proporciona un dashboard interactivo con visualizaciones de datos. Además, incluye un generador de resúmenes automáticos y alertas sobre eventos climáticos importantes para mantener a los usuarios informados y concienciados.

## 🎯 ¿Qué problema resuelve?

La desinformación y la sobrecarga de información sobre el cambio climático. Existen miles de noticias sobre el clima diariamente, pero es difícil para las personas saber qué es relevante, distinguir entre información fiable y sensacionalismo, y comprender las tendencias globales. ClimateNews AI resuelve esto filtrando, analizando y presentando la información de manera clara, basada en datos y accesible, permitiendo a los usuarios tomar decisiones informadas y mantenerse actualizados sobre lo que realmente importa en la lucha contra el cambio climático.

## 🎨 Este es el tipo de mi proyecto:
> Plataforma web con Flask + NLP + Visualización de datos + Base de datos

## 📚 Las bibliotecas que voy a utilizar:
- **Flask** - Framework web para crear la aplicación
- **BeautifulSoup4** - Web scraping para extraer noticias de sitios web
- **Requests** - Consumir APIs de noticias (NewsAPI, etc.)
- **NLTK** - Procesamiento de lenguaje natural para clasificación de texto
- **SpaCy** - Análisis de texto avanzado y extracción de entidades
- **WordCloud** - Generación de nubes de palabras
- **Plotly** - Visualización de datos interactiva
- **Matplotlib** - Gráficos estáticos
- **Pandas** - Manejo de datos en tablas
- **NumPy** - Cálculos numéricos

## 🔗 Referencias útiles:
- [Newswire - News Dashboard con Flask](https://github.com/szymon42069/Newswire) - Dashboard de noticias que scrappea RSS feeds de Google News y los sirve a través de una API Flask
- [PyCast News - News Aggregator](https://asbinthapa99.github.io/news/) - Agregador de noticias automatizado con Flask y PostgreSQL que scrappea 14 feeds RSS cada hora
- [Flask News Application con NewsAPI](https://www.geeksforgeeks.org/python/flask-news-application-using-newsapi/) - Tutorial completo para crear una app de noticias con Flask y NewsAPI

## � Los artículos de la guía que me ayudarán durante el desarrollo:
- [NLTK Learning to Classify Text](https://www.nltk.org/book/ch06.html) - Explica cómo usar NLTK para clasificar texto con técnicas de machine learning como Naive Bayes y Decision Trees, perfecto para clasificar noticias por impacto ambiental
- [NLTK Classification How-To](https://www.nltk.org/howto/classify.html) - Documentación práctica sobre cómo implementar clasificadores de texto con NLTK
- [Integrate Plotly Dash Into Flask](https://hackersandslackers.com/plotly-dash-with-flask/) - Guía para integrar visualizaciones interactivas de Plotly dentro de aplicaciones Flask
- [Plotly NanoDash Tutorial](https://github.com/plotly/tutorial-nanodash) - Tutorial que enseña cómo construir dashboards interactivos desde cero con Flask y Plotly.js

## 🚀 Funcionalidades

- **Análisis de noticias en tiempo real** de múltiples fuentes
- **Clasificación por impacto ambiental** (alto, medio, bajo)
- **Nubes de palabras** para identificar temas recurrentes
- **Dashboard interactivo** con visualizaciones de datos
- **Generador de resúmenes automáticos** con IA
- **Alertas** sobre eventos climáticos importantes
- **Búsqueda inteligente** por temas y keywords

## 📦 Instalación

```bash
# Instrucciones de instalación
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

## 📊 Contribución

Este proyecto es parte de un hackathon enfocado en soluciones para el cambio climático.

## 📄 Licencia

MIT License
