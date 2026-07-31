import 'package:flutter/material.dart';

class ProfileScreen extends StatelessWidget {
  const ProfileScreen({super.key});

  Widget buildCard(
      IconData icon,
      String title,
      String value,
      ) {
    return Card(
      elevation: 1,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(18),
      ),
      child: ListTile(
        leading: CircleAvatar(
          backgroundColor: const Color(0xFF2563EB).withOpacity(0.15),
          child: Icon(
            icon,
            color: const Color(0xFF2563EB),
          ),
        ),
        title: Text(title),
        trailing: Text(
          value,
          style: const TextStyle(
            fontWeight: FontWeight.bold,
            fontSize: 16,
          ),
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Profile"),
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(20),
        child: Column(
          children: [

            const CircleAvatar(
              radius: 50,
              backgroundColor: Color(0xFF2563EB),
              child: Icon(
                Icons.person,
                size: 60,
                color: Colors.white,
              ),
            ),

            const SizedBox(height: 15),

            const Text(
              "Yash Kumar",
              style: TextStyle(
                fontSize: 26,
                fontWeight: FontWeight.bold,
              ),
            ),

            const Text(
              "Smart Citizen",
              style: TextStyle(
                color: Colors.grey,
              ),
            ),

            const SizedBox(height: 30),

            buildCard(
              Icons.assignment,
              "Complaints Submitted",
              "06",
            ),

            buildCard(
              Icons.check_circle,
              "Resolved Complaints",
              "05",
            ),

            buildCard(
              Icons.pending_actions,
              "Pending Complaints",
              "01",
            ),

            buildCard(
              Icons.star,
              "Citizen Score",
              "95 / 100",
            ),

            buildCard(
              Icons.emoji_events,
              "AI Badge",
              "Gold Citizen",
            ),

            buildCard(
              Icons.location_city,
              "City Contribution",
              "Excellent",
            ),

            const SizedBox(height: 30),

            SizedBox(
              width: double.infinity,
              child: ElevatedButton.icon(
                onPressed: () {},
                icon: const Icon(Icons.logout),
                label: const Text("Logout"),
              ),
            ),
          ],
        ),
      ),
    );
  }
}