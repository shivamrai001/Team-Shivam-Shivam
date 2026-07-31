import 'package:flutter/material.dart';

class NotificationsScreen extends StatelessWidget {
  const NotificationsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Smart Alerts"),
      ),
      body: ListView(
        padding: const EdgeInsets.all(20),
        children: [

          _notification(
            Icons.check_circle,
            Colors.green,
            "Complaint Submitted",
            "Your complaint USA-2026-001 has been submitted successfully.",
            "09:20 AM",
          ),

          _notification(
            Icons.apartment,
            Colors.blue,
            "Department Assigned",
            "Municipal Services has accepted your complaint.",
            "09:45 AM",
          ),

          _notification(
            Icons.traffic,
            Colors.orange,
            "Traffic Alert",
            "Heavy traffic detected near City Center.",
            "10:10 AM",
          ),

          _notification(
            Icons.air,
            Colors.deepPurple,
            "Pollution Alert",
            "AQI has increased in the Industrial Area.",
            "11:15 AM",
          ),

          _notification(
            Icons.water_drop,
            Colors.blue,
            "Flood Prediction",
            "Low flood risk predicted for the next 48 hours.",
            "12:00 PM",
          ),

          _notification(
            Icons.smart_toy,
            Colors.teal,
            "AI Recommendation",
            "Garbage complaints are expected to increase this weekend.",
            "01:10 PM",
          ),
        ],
      ),
    );
  }

  Widget _notification(
      IconData icon,
      Color color,
      String title,
      String subtitle,
      String time,
      ) {
    return Card(
      margin: const EdgeInsets.only(bottom: 15),
      elevation: 1,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(18),
      ),
      child: ListTile(
        leading: CircleAvatar(
          backgroundColor: color.withOpacity(0.15),
          child: Icon(icon, color: color),
        ),
        title: Text(
          title,
          style: const TextStyle(
            fontWeight: FontWeight.bold,
          ),
        ),
        subtitle: Text(subtitle),
        trailing: Text(
          time,
          style: const TextStyle(
            color: Colors.grey,
            fontSize: 12,
          ),
        ),
      ),
    );
  }
}