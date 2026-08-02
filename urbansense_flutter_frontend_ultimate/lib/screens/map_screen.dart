import 'package:flutter/material.dart';
import 'package:flutter_map/flutter_map.dart';
import 'package:latlong2/latlong.dart';
import '../services/api_service.dart';

class MapScreen extends StatefulWidget {
  const MapScreen({super.key});
  @override
  State<MapScreen> createState() => _MapScreenState();
}

class _MapScreenState extends State<MapScreen> {
  List<Marker> _markers = [];
  bool _isLoading = true;

  @override
  void initState() {
    super.initState();
    _loadMarkers();
  }

  void _loadMarkers() async {
    final data = await ApiService.getMapMarkers();
    if (mounted) {
      setState(() {
        _markers = data.map((m) {
          final lat = m['latitude'] as double;
          final lng = m['longitude'] as double;
          final isEmergency = m['priority'] == 'Emergency';
          return Marker(
            point: LatLng(lat, lng),
            width: 40,
            height: 40,
            child: Icon(
              Icons.location_on_rounded,
              color: isEmergency ? const Color(0xFFF87171) : const Color(0xFF4FD1C5),
              size: 40,
            ),
          );
        }).toList();
        _isLoading = false;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: _isLoading
          ? const Center(child: CircularProgressIndicator(color: Color(0xFF4FD1C5)))
          : ClipRRect(
              borderRadius: const BorderRadius.vertical(top: Radius.circular(32)),
              child: FlutterMap(
                options: const MapOptions(
                  initialCenter: LatLng(20.5937, 78.9629),
                  initialZoom: 5.0,
                ),
                children: [
                  TileLayer(
                    urlTemplate: 'https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', // Switched to soothing light map
                    userAgentPackageName: 'com.urbansense.app',
                  ),
                  MarkerLayer(markers: _markers),
                ],
              ),
            ),
      floatingActionButton: FloatingActionButton(
        onPressed: _loadMarkers,
        backgroundColor: Colors.white,
        elevation: 4,
        child: const Icon(Icons.my_location_rounded, color: Color(0xFF4FD1C5)),
      ),
    );
  }
}
