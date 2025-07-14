import { Component, OnInit } from '@angular/core';
import { GoogleMapsService } from '../../google-maps.service';

@Component({
  selector: 'app-encontrar-dermatologo',
  templateUrl: './encontrar-dermatologo.component.html',
  styleUrls: ['./encontrar-dermatologo.component.css']
})
export class EncontrarDermatologoComponent implements OnInit {

  map!: google.maps.Map;

  constructor(private googleMapsService: GoogleMapsService) { }

  ngOnInit(): void {
    this.googleMapsService.loadScript()
      .then(() => {
        this.initMap();
      })
      .catch(err => {
        console.error('Error loading Google Maps script:', err);
        alert('No se pudo cargar el mapa. Por favor, intente de nuevo más tarde.');
      });
  }

  initMap(): void {
    this.map = new google.maps.Map(document.getElementById("map") as HTMLElement, {
      center: { lat: -2.90055, lng: -79.00453 },
      zoom: 12,
    });
  }

  buscarDermatologos(): void {
    if (!this.map) {
      alert('El mapa no se ha inicializado.');
      return;
    }

    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(position => {
        const userLocation = {
          lat: position.coords.latitude,
          lng: position.coords.longitude,
        };

        this.map.setCenter(userLocation);
        new google.maps.Marker({
          position: userLocation,
          map: this.map,
          title: "Tu ubicación",
        });

        const service = new google.maps.places.PlacesService(this.map);
        service.nearbySearch({
          location: userLocation,
          radius: 5000,
          keyword: 'dermatologist',
          type: 'doctor'
        }, (results, status) => {
          if (status === google.maps.places.PlacesServiceStatus.OK && results) {
            for (const place of results) {
              if (place.geometry && place.geometry.location) {
                const marker = new google.maps.Marker({
                  map: this.map,
                  position: place.geometry.location,
                  title: place.name
                });

                const infowindow = new google.maps.InfoWindow({
                  content: `
                    <strong>${place.name}</strong><br>
                    ${place.vicinity || ''}<br>
                    <a href="https://www.google.com/maps/place/?q=place_id:${place.place_id}" target="_blank" class="text-blue-600 underline">Ver en Google Maps</a>
                  `
                });

                marker.addListener('click', () => {
                  infowindow.open(this.map, marker);
                });
              }
            }
          }
        });
      }, () => {
        alert("No se pudo obtener tu ubicación. Asegúrate de haber concedido los permisos.");
      });
    } else {
      alert("Tu navegador no permite obtener la ubicación.");
    }
  }
}
