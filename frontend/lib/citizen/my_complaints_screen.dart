import 'package:flutter/material.dart';

class MyComplaintsScreen extends StatelessWidget {
  const MyComplaintsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("My Complaints"),
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(20),
        child: Column(
          children: [

            _buildComplaintCard(
              complaintId: "USA-2026-001",
              title: "Garbage Overflow",
              status: "Resolved",
              priority: "High",
              department: "Municipal Services",
              time: "12 Hours",
            ),

            const SizedBox(height: 18),

            _buildComplaintCard(
              complaintId: "USA-2026-002",
              title: "Street Light Not Working",
              status: "In Progress",
              priority: "Medium",
              department: "Electrical Department",
              time: "24 Hours",
            ),

            const SizedBox(height: 18),

            _buildComplaintCard(
              complaintId: "USA-2026-003",
              title: "Water Leakage",
              status: "Pending",
              priority: "High",
              department: "Water Department",
              time: "36 Hours",
            ),

            const SizedBox(height: 18),

            _buildComplaintCard(
              complaintId: "USA-2026-004",
              title: "Pothole on Main Road",
              status: "Resolved",
              priority: "Medium",
              department: "Road Maintenance",
              time: "18 Hours",
            ),

            const SizedBox(height: 18),

            _buildComplaintCard(
              complaintId: "USA-2026-005",
              title: "Illegal Garbage Dumping",
              status: "Pending",
              priority: "High",
              department: "Municipal Services",
              time: "48 Hours",
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildComplaintCard({
    required String complaintId,
    required String title,
    required String status,
    required String priority,
    required String department,
    required String time,
  }) {

    Color statusColor = Colors.orange;

    if (status == "Resolved") {
      statusColor = Colors.green;
    } else if (status == "Pending") {
      statusColor = Colors.red;
    }

    return Container(
      width: double.infinity,
      padding: const EdgeInsets.all(18),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(20),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [

          Row(
            mainAxisAlignment:
                MainAxisAlignment.spaceBetween,
            children: [

              Text(
                complaintId,
                style: const TextStyle(
                  color: Colors.grey,
                  fontWeight: FontWeight.bold,
                ),
              ),

              Container(
                padding: const EdgeInsets.symmetric(
                  horizontal: 12,
                  vertical: 6,
                ),
                decoration: BoxDecoration(
                  color: statusColor.withOpacity(0.15),
                  borderRadius:
                      BorderRadius.circular(20),
                ),
                child: Text(
                  status,
                  style: TextStyle(
                    color: statusColor,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ),
            ],
          ),

          const SizedBox(height: 15),

          Text(
            title,
            style: const TextStyle(
              fontSize: 22,
              fontWeight: FontWeight.bold,
            ),
          ),

          const Divider(height: 30),

          Row(
            children: [

              const Icon(
                Icons.priority_high,
                color: Color(0xFF2563EB),
              ),

              const SizedBox(width: 10),

              Text("Priority : $priority"),
            ],
          ),

          const SizedBox(height: 10),

          Row(
            children: [

              const Icon(
                Icons.apartment,
                color: Color(0xFF2563EB),
              ),

              const SizedBox(width: 10),

              Expanded(
                child: Text(
                  "Department : $department",
                ),
              ),
            ],
          ),

          const SizedBox(height: 10),

          Row(
            children: [

              const Icon(
                Icons.schedule,
                color: Color(0xFF2563EB),
              ),

              const SizedBox(width: 10),

              Text(
                "Estimated Time : $time",
              ),
            ],
          ),
        ],
      ),
    );
  }
}