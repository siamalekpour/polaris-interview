//--- GMap ---//
(function($, window, document, undefined){

    function GMap(element, options){
        this.$element = $(element);
        this.options = options;
        this.markers = this.options.markers;
        this.mapOptions = {
            scrollwheel: false,
            draggable: true,
            navigationControl: true,
            panControl: true,
            zoom: 16,
            center: new google.maps.LatLng(43.6465734, -79.3938083),
            mapTypeId: google.maps.MapTypeId.ROADMAP
        };
        console.log(this.$element[0])
        this._initMap();
    }

    GMap.prototype = {
        _initMap: function(){
            this.map = new google.maps.Map(document.getElementById('trip-map'), this.mapOptions);
            this._centerMap();
            for(var i=0; i<this.markers.length; i++){
                this._addMarker(this.markers[i]);
            }
        },
        _centerMap: function(){
            var length = this.options.markers.length;
            if(length){
                if(length==1){
                    this.map.setOptions({center: new google.maps.LatLng(this.markers[0].lat, this.markers[0].lng)});
                }else{
                    var bounds = new google.maps.LatLngBounds();
                    for (var i = 0; i<length; i++) {
                        bounds.extend(new google.maps.LatLng(this.markers[i].lat,this.markers[i].lng));
                    }
                    this.map.fitBounds(bounds);
                }
            }
        },
        _addMarker: function(marker){
            new google.maps.Marker({
                position: new google.maps.LatLng(marker.lat, marker.lng),
                map: this.map,
                title: marker.name
            });
        }
    };
    // Plugin Definition //
    $.fn.gmap = function(options){
        if( typeof options == 'string'){
            var plugin = this.data('gmap');
            if(plugin){
                var r = plugin[options].apply(plugin, Array.prototype.slice.call( arguments, 1 ) );
                if(r) return r
            }
            return this
        }

        options = $.extend({}, $.fn.gmap.defaults, options);

        return this.each(function(){
            var plugin = $.data(this, 'gmap');
            if( ! plugin ){
                plugin = new GMap(this, options);
                $.data(this, 'gmap', plugin);
            }
        });
    };
    $.fn.gmap.defaults = {
        markers: []
    };

})(jQuery, window, document);
