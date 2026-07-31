import 'package:flutter/material.dart';

class MapScreen extends StatelessWidget {
  const MapScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Smart City Map"),
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(20),
        child: Column(
          children: [

            // LIVE MAP CARD

            Container(
              height: 250,
              width: double.infinity,
              decoration: BoxDecoration(
                color: Colors.white,
                borderRadius: BorderRadius.circular(25),
              ),
              child: const Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [

                  Icon(
                    Icons.location_city,
                    size: 80,
                    color: Color(0xFF2563EB),
                  ),

                  SizedBox(height: 15),

                  Text(
                    "LIVE SMART CITY MONITORING",
                    style: TextStyle(
                      fontSize: 22,
                      fontWeight: FontWeight.bold,
                    ),
                  ),

                  SizedBox(height: 10),

                  Text(
                    "AI Powered GIS Monitoring System",
                  ),
                ],
              ),
            ),

            const SizedBox(height: 25),

            _buildAlertCard(
              icon: Icons.traffic,
              title: "Traffic Zone",
              location: "City Center",
              status: "LOW TRAFFIC",
            ),

            const SizedBox(height: 15),

            _buildAlertCard(
              icon: Icons.air,
              title: "Pollution Zone",
              location: "Industrial Area",
              status: "MODERATE AQI",
            ),

            const SizedBox(height: 15),

            _buildAlertCard(
              icon: Icons.water_drop,
              title: "Flood Monitoring",
              location: "Riverside Area",
              status: "LOW FLOOD RISK",
            ),

            const SizedBox(height: 15),

            _buildAlertCard(
              icon: Icons.report_problem,
              title: "Complaint Hotspot",
              location: "Sector 12",
              status: "15 ACTIVE COMPLAINTS",
            ),

            const SizedBox(height: 15),

            _buildAlertCard(
              icon: Icons.warning_amber,
              title: "Emergency Zone",
              location: "Highway Junction",
              status: "MINOR INCIDENT DETECTED",
            ),

            const SizedBox(height: 15),

            _buildAlertCard(
              icon: Icons.water_damage,
              title: "Water Leakage Zone",
              location: "Sector 8",
              status: "UNDER MAINTENANCE",
            ),

            const SizedBox(height: 25),

            // SMART CITY STATUS

            Container(
              width: double.infinity,
              padding: const EdgeInsets.all(20),
              decoration: BoxDecoration(
                color: Colors.white,
                borderRadius: BorderRadius.circular(25),
              ),
              child: const Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [

                  Text(
                    "Smart Monitoring Features",
                    style: TextStyle(
                      fontSize: 22,
                      fontWeight: FontWeight.bold,
                    ),
                  ),

                  SizedBox(height: 15),

                  Text("• Real-Time Traffic Monitoring"),

                  SizedBox(height: 10),

                  Text("• Pollution Heatmap Analysis"),

                  SizedBox(height: 10),

                  Text("• Complaint Hotspot Detection"),

                  SizedBox(height: 10),

                  Text("• Flood Risk Prediction"),

                  SizedBox(height: 10),

                  Text("• Emergency Incident Tracking"),

                  SizedBox(height: 10),

                  Text("• Smart Water Monitoring"),

                  SizedBox(height: 10),

                  Text("• AI Powered Urban Analytics"),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildAlertCard({
    required IconData icon,
    required String title,
    required String location,
    required String status,
  }) {
    return Container(
      width: double.infinity,
      padding: const EdgeInsets.all(18),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(20),
      ),
      child: Row(
        children: [

          Icon(
            icon,
            size: 40,
            color: const Color(0xFF2563EB),
          ),

          const SizedBox(width: 20),

          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [

                Text(
                  title,
                  style: const TextStyle(
                    fontSize: 18,
                    fontWeight: FontWeight.bold,
                  ),
                ),

                const SizedBox(height: 5),

                Text(location),

                const SizedBox(height: 5),

                Text(status),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
