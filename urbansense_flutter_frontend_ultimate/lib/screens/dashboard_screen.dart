import 'package:flutter/material.dart';
import '../services/api_service.dart';

class DashboardScreen extends StatefulWidget {
  const DashboardScreen({super.key});
  @override
  State<DashboardScreen> createState() => _DashboardScreenState();
}

class _DashboardScreenState extends State<DashboardScreen> {
  late Future<Map<String, dynamic>?> _summaryFuture;

  @override
  void initState() {
    super.initState();
    _summaryFuture = ApiService.getDashboardSummary();
  }

  @override
  Widget build(BuildContext context) {
    return FutureBuilder<Map<String, dynamic>?>(
      future: _summaryFuture,
      builder: (context, snapshot) {
        if (snapshot.connectionState == ConnectionState.waiting) return const Center(child: CircularProgressIndicator(color: Color(0xFF4FD1C5)));
        final stats = snapshot.data ?? {};
        return RefreshIndicator(
          color: const Color(0xFF4FD1C5),
          onRefresh: () async => setState(() { _summaryFuture = ApiService.getDashboardSummary(); }),
          child: ListView(
            padding: const EdgeInsets.symmetric(horizontal: 24.0, vertical: 16.0),
            children: [
              const Text('Hello, Citizen 👋', style: TextStyle(fontSize: 28, fontWeight: FontWeight.bold, color: Color(0xFF1E293B))),
              const SizedBox(height: 8),
              const Text('Here is the current status of reported urban issues.', style: TextStyle(color: Color(0xFF94A3B8), fontSize: 16)),
              const SizedBox(height: 32),
              GridView.count(
                shrinkWrap: true,
                physics: const NeverScrollableScrollPhysics(),
                crossAxisCount: 2,
                crossAxisSpacing: 16,
                mainAxisSpacing: 16,
                childAspectRatio: 1.1,
                children: [
                  _buildSoftCard('Total Reports', '${stats['total_complaints'] ?? 0}', Icons.folder_open_rounded, const Color(0xFF60A5FA), const Color(0xFFEFF6FF)),
                  _buildSoftCard('Pending', '${stats['pending'] ?? 0}', Icons.pending_actions_rounded, const Color(0xFFFBBF24), const Color(0xFFFFFBEB)),
                  _buildSoftCard('Resolved', '${stats['resolved'] ?? 0}', Icons.check_circle_outline_rounded, const Color(0xFF34D399), const Color(0xFFECFDF5)),
                  _buildSoftCard('Emergencies', '${stats['critical'] ?? 0}', Icons.warning_amber_rounded, const Color(0xFFF87171), const Color(0xFFFEF2F2)),
                ],
              ),
            ],
          ),
        );
      },
    );
  }

  Widget _buildSoftCard(String title, String value, IconData icon, Color iconColor, Color bgColor) {
    return Container(
      padding: const EdgeInsets.all(20),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(24),
        boxShadow: [BoxShadow(color: const Color(0xFFE2E8F0).withOpacity(0.5), blurRadius: 10, offset: const Offset(0, 4))],
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Container(
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(color: bgColor, borderRadius: BorderRadius.circular(16)),
            child: Icon(icon, size: 28, color: iconColor),
          ),
          Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(value, style: const TextStyle(fontSize: 32, fontWeight: FontWeight.w800, color: Color(0xFF1E293B), height: 1.2)),
              Text(title, style: const TextStyle(color: Color(0xFF94A3B8), fontSize: 14, fontWeight: FontWeight.w500)),
            ],
          ),
        ],
      ),
    );
  }
}
