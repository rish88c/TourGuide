from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import folium
import geocoder


def Intro(response):
	return render(response,'main/Intro.html',{})

def base(response):
	return render(response,'main/base.html',{})

def home(response):
	return render(response,'main/home.html',{})

def chembur(response):
	location = geocoder.osm('chembur')
	lat = location.lat
	lng = location.lng
	country = location.country
	f = folium.Figure(width=600, height=500)
	m = folium.Map(location=[lat,lng], zoom_start=100,control_scale=True ).add_to(f)
	folium.TileLayer('openstreetmap').add_to(m)
	folium.Marker([lat,lng],tooltip = 'Click for more',popup ="chembur").add_to(m)
	m = m._repr_html_()
	context = {

		'm':m,

	}
	return render(response,'main/chembur.html',context)

def marine(response):
	# location = geocoder.osm('marine')
	# lat = location.lat
	# lng = location.lng
	# country = location.country
	lat = 18.941482
	lng = 72.823679
	f = folium.Figure(width=600, height=500)
	m = folium.Map(location=[lat,lng], zoom_start=100,control_scale=True ).add_to(f)
	folium.TileLayer('openstreetmap').add_to(m)
	folium.Marker([lat,lng],tooltip = 'Click for more',popup ="Marines").add_to(m)
	m = m._repr_html_()
	context = {
		'm':m,

	}
	return render(response,'main/marine.html',context)

def bandra(response):
	# location = geocoder.osm('marine')
	# lat = location.lat
	# lng = location.lng
	# country = location.country
	lat = 19.0790
	lng = 72.9080
	f = folium.Figure(width=600, height=500)
	m = folium.Map(location=[lat,lng], zoom_start=100,control_scale=True ).add_to(f)
	folium.TileLayer('openstreetmap').add_to(m)
	folium.Marker([lat,lng],tooltip = 'Click for more',popup ="Bandra").add_to(m)
	m = m._repr_html_()
	context = {
		'm':m,

	}
	return render(response,'main/bandra.html',context)

def ghatkoper(response):
	# location = geocoder.osm('marine')
	# lat = location.lat
	# lng = location.lng
	# country = location.country
	lat = 19.0790
	lng = 72.9080
	f = folium.Figure(width=600, height=500)
	m = folium.Map(location=[lat,lng], zoom_start=100,control_scale=True ).add_to(f)
	folium.TileLayer('openstreetmap').add_to(m)
	folium.Marker([lat,lng],tooltip = 'Click for more',popup ="ghatkoper").add_to(m)
	m = m._repr_html_()
	context = {
		'm':m,

	}
	return render(response,'main/ghatkoper.html',context)

def colaba(response):
	location = geocoder.osm('colaba')
	lat = location.lat
	lng = location.lng
	country = location.country
	f = folium.Figure(width=600, height=500)
	m = folium.Map(location=[lat,lng], zoom_start=100,control_scale=True ).add_to(f)
	folium.TileLayer('openstreetmap').add_to(m)
	folium.Marker([lat,lng],tooltip = 'Click for more',popup =country).add_to(m)
	m = m._repr_html_()
	context = {
		'm':m,

	}
	return render(response,'main/colaba.html',context)


def aboutus(response):
	return render(response,'main/aboutus.html',{})

def history(response):
	return render(response,'main/history.html',{})

def map(request):
	location = geocoder.osm('chembur')
	lat = location.lat
	lng = location.lng
	country = location.country
	# f = folium.Figure(width=1000, height=500)
	m = folium.Map(location=[lat,lng], zoom_start=100,control_scale=True )
	folium.TileLayer('openstreetmap').add_to(m)
	folium.Marker([lat,lng],tooltip = 'Click for more',popup ="chembur").add_to(m)
	m = m._repr_html_()
	context = {
		'm':m,

	}
	return render(request,'main/map.html',context)

	# tiles="Stamen Terrain"