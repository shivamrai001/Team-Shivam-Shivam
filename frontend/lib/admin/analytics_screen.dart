import 'package:flutter/material.dart';

class AnalyticsScreen extends StatelessWidget {
  const AnalyticsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("AI Analytics"),
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(20),
        child: Column(
          children: [

            // Smart City Health Score

            _buildAnalyticsCard(
              title: "Smart City Health Score",
              value: "92/100",
              icon: Icons.health_and_safety,
            ),

            const SizedBox(height: 15),

            _buildAnalyticsCard(
              title: "Traffic Congestion Index",
              value: "Low",
              icon: Icons.traffic,
            ),

            const SizedBox(height: 15),

            _buildAnalyticsCard(
              title: "Air Pollution Level",
              value: "Moderate",
              icon: Icons.air,
            ),

            const SizedBox(height: 15),

            _buildAnalyticsCard(
              title: "Citizen Satisfaction",
              value: "95%",
              icon: Icons.people,
            ),

            const SizedBox(height: 15),

            _buildAnalyticsCard(
              title: "Emergency Risk Level",
              value: "Low",
              icon: Icons.warning,
            ),

            const SizedBox(height: 25),

            // AI Predictions Section

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
                    "AI Risk Predictions",
                    style: TextStyle(
                      fontSize: 22,
                      fontWeight: FontWeight.bold,
                    ),
                  ),

                  SizedBox(height: 15),

                  Text("• Garbage complaints expected to increase by 12%"),

                  SizedBox(height: 10),

                  Text("• Flood risk remains LOW for the next 48 hours"),

                  SizedBox(height: 10),

                  Text("• Traffic congestion expected near commercial areas"),

                  SizedBox(height: 10),

                  Text("• High citizen activity predicted during weekends"),

                ],
              ),
            ),

            const SizedBox(height: 25),

            // Monthly Insights

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
                    "Monthly Insights",
                    style: TextStyle(
                      fontSize: 22,
                      fontWeight: FontWeight.bold,
                    ),
                  ),

                  SizedBox(height: 15),

                  Text("Complaints Resolved : 2,089"),

                  SizedBox(height: 10),

                  Text("Average Resolution Time : 18 Hours"),

                  SizedBox(height: 10),

                  Text("AI Detection Accuracy : 97%"),

                  SizedBox(height: 10),

                  Text("Overall City Performance : Excellent"),

                ],
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildAnalyticsCard({
    required String title,
    required String value,
    required IconData icon,
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

                Text(
                  value,
                  style: const TextStyle(
                    fontSize: 20,
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
