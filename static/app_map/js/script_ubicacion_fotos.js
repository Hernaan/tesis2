$(function(){
	var lat = $('#mapa').attr('latitud');
	var lng = $('#mapa').attr('longitud');

	initialize(lat, lng);

	function initialize(lat, lng)
	{
		var GLatLng = new google.maps.LatLng(lat, lng);

		var mapSettings = {
			center: GLatLng,
			zoom: 12,
			mapTypeId: google.maps.MapTypeId.ROADMAP
		}

		map = new google.maps.Map($('#mapa').get(0), mapSettings);
		
		var marker = new google.maps.Marker({
			position: GLatLng,
			map:map			
		});
	}	
});