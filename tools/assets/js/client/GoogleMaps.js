var GoogleMaps = (function($){
	var map;
	var initialize = function(){
		var mapOptions = {
		  center: new google.maps.LatLng(42.0411274, -87.6900807),
		  zoom: 13
		};
		map =  new google.maps.Map(document.getElementById("map-canvas"),mapOptions);
	},
	addMarker = function(data){
		$.ajax({
			type:"GET",
			dataType:"json",
			data:data,
			url:"/clients/ajax_coordinates/",
			success:function(response){
				response.forEach(function(c){

					var marker = new google.maps.Marker({
						position: new google.maps.LatLng(c["fields"]["latitude"],c["fields"]["longitude"]),
						map : map,
						title: c["fields"]["first_name"]+" "+c["fields"]["last_name"],
					});
				});

			}
		});
	};
	return {
		init: initialize,
		addMarker: addMarker
	};
}(jQuery));