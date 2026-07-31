import 'package:flutter/material.dart';

class DashboardScreen extends StatelessWidget {
  const DashboardScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Smart City Dashboard"),
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(20),
        child: Column(
          children: [

            // Header Card

            Container(
              width: double.infinity,
              padding: const EdgeInsets.all(20),
              decoration: BoxDecoration(
                color: Colors.white,
                borderRadius: BorderRadius.circular(20),
              ),
              child: const Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    "UrbanSense AI 2.0",
                    style: TextStyle(
                      fontSize: 24,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  SizedBox(height: 10),
                  Text(
                    "Real-Time Smart City Monitoring System",
                  ),
                ],
              ),
            ),

            const SizedBox(height: 20),

            // Today's Statistics

            _buildDashboardCard(
              Icons.report_problem,
              "Today's Complaints",
              "37",
            ),

            const SizedBox(height: 15),

            _buildDashboardCard(
              Icons.check_circle,
              "Resolved Today",
              "28",
            ),

            const SizedBox(height: 15),

            _buildDashboardCard(
              Icons.warning_amber,
              "Active Alerts",
              "04",
            ),

            const SizedBox(height: 15),

            _buildDashboardCard(
              Icons.analytics,
              "AI Detection Accuracy",
              "97%",
            ),

            const SizedBox(height: 25),

            // AI Predictions

            Container(
              width: double.infinity,
              padding: const EdgeInsets.all(20),
              decoration: BoxDecoration(
                color: Colors.white,
                borderRadius: BorderRadius.circular(20),
              ),
              child: const Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [

                  Text(
                    "AI Predictions",
                    style: TextStyle(
                      fontSize: 22,
                      fontWeight: FontWeight.bold,
                    ),
                  ),

                  SizedBox(height: 15),

                  Text("Traffic Congestion : LOW"),

                  SizedBox(height: 10),

                  Text("Flood Risk : LOW"),

                  SizedBox(height: 10),

                  Text("Pollution Level : MODERATE"),

                  SizedBox(height: 10),

                  Text("Complaint Trend : +12%"),

                ],
              ),
            ),

            const SizedBox(height: 25),

            // Department Performance

            Container(
              width: double.infinity,
              padding: const EdgeInsets.all(20),
              decoration: BoxDecoration(
                color: Colors.white,
                borderRadius: BorderRadius.circular(20),
              ),
              child: const Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [

                  Text(
                    "Department Performance",
                    style: TextStyle(
                      fontSize: 22,
                      fontWeight: FontWeight.bold,
                    ),
                  ),

                  SizedBox(height: 15),

                  Text("Municipal Services : 92%"),

                  SizedBox(height: 10),

                  Text("Traffic Department : 88%"),

                  SizedBox(height: 10),

                  Text("Water Department : 95%"),

                  SizedBox(height: 10),

                  Text("Electrical Department : 91%"),

                ],
              ),
            ),

            const SizedBox(height: 25),

            // Smart City Status

            Container(
              width: double.infinity,
              padding: const EdgeInsets.all(20),
              decoration: BoxDecoration(
                color: Colors.white,
                borderRadius: BorderRadius.circular(20),
              ),
              child: const Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [

                  Text(
                    "Smart City Status",
                    style: TextStyle(
                      fontSize: 22,
                      fontWeight: FontWeight.bold,
                    ),
                  ),

                  SizedBox(height: 15),

                  Text("City Health Score : 92 / 100"),

                  SizedBox(height: 10),

                  Text("Emergency Response : ACTIVE"),

                  SizedBox(height: 10),

                  Text("Smart Monitoring : ONLINE"),

                  SizedBox(height: 10),

                  Text("AI Services : RUNNING"),

                ],
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildDashboardCard(
    IconData icon,
    String title,
    String value,
  ) {
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
              crossAxisAlignment:
                  CrossAxisAlignment.start,
              children: [

                Text(
                  title,
                  style: const TextStyle(
                    fontSize: 18,
                    fontWeight: FontWeight.bold,
                  ),
                ),

                const SizedBox(height: 5),

                Text(
                  value,
                  style: const TextStyle(
                    fontSize: 22,
                    fontWeight: FontWeight.bold,
                  ),
                ),

              ],
            ),
          ),
        ],
      ),
    );
  }
}