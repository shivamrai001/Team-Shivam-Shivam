import 'package:flutter/material.dart';

import '../admin/analytics_screen.dart';
import '../admin/dashboard_screen.dart';
import '../admin/map_screen.dart';
import 'my_complaints_screen.dart';
import 'notifications_screen.dart';
import 'report_complaint_screen.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("UrbanSense AI 2.0"),
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(20),
        child: Column(
          children: [
            // Welcome Card

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
                    "Welcome Citizen!",
                    style: TextStyle(
                      fontSize: 24,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  SizedBox(height: 10),
                  Text(
                    "Report city issues and help build a smarter and safer city.",
                  ),
                ],
              ),
            ),

            const SizedBox(height: 25),

            _buildFeatureCard(
              context,
              icon: Icons.report_problem_outlined,
              title: "Report Complaint",
              subtitle:
                  "Submit issues like potholes, garbage and water leakage.",
              screen: const ReportComplaintScreen(),
            ),

            const SizedBox(height: 15),

            _buildFeatureCard(
              context,
              icon: Icons.track_changes_outlined,
              title: "Track Complaints",
              subtitle:
                  "Check the current status of your submitted complaints.",
              screen: const MyComplaintsScreen(),
            ),

            const SizedBox(height: 15),

            _buildFeatureCard(
              context,
              icon: Icons.notifications_active_outlined,
              title: "Notifications",
              subtitle:
                  "Receive real-time complaint updates and alerts.",
              screen: const NotificationsScreen(),
            ),

            const SizedBox(height: 15),

            _buildFeatureCard(
              context,
              icon: Icons.smart_toy_outlined,
              title: "AI Analytics",
              subtitle:
                  "View smart city AI predictions and analytics.",
              screen: const AnalyticsScreen(),
            ),

            const SizedBox(height: 15),

            _buildFeatureCard(
              context,
              icon: Icons.dashboard_outlined,
              title: "Dashboard",
              subtitle:
                  "Monitor complaints and smart city statistics.",
              screen: const DashboardScreen(),
            ),

            const SizedBox(height: 15),

            _buildFeatureCard(
              context,
              icon: Icons.map_outlined,
              title: "Smart City Map",
              subtitle:
                  "View traffic, pollution and complaint hotspots.",
              screen: const MapScreen(),
            ),

            const SizedBox(height: 25),

            Container(
              width: double.infinity,
              padding: const EdgeInsets.all(18),
              decoration: BoxDecoration(
                color: Colors.white,
                borderRadius: BorderRadius.circular(20),
              ),
              child: const Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    "Smart City Features",
                    style: TextStyle(
                      fontSize: 20,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  SizedBox(height: 15),
                  Text("• AI Complaint Classification"),
                  SizedBox(height: 8),
                  Text("• Image Verification"),
                  SizedBox(height: 8),
                  Text("• Priority Prediction"),
                  SizedBox(height: 8),
                  Text("• Department Assignment"),
                  SizedBox(height: 8),
                  Text("• Real-Time Notifications"),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildFeatureCard(
    BuildContext context, {
    required IconData icon,
    required String title,
    required String subtitle,
    required Widget screen,
  }) {
    return GestureDetector(
      onTap: () {
        Navigator.push(
          context,
          MaterialPageRoute(
            builder: (_) => screen,
          ),
        );
      },
      child: Container(
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
                      fontWeight:
                          FontWeight.bold,
                    ),
                  ),
                  const SizedBox(height: 5),
                  Text(subtitle),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
