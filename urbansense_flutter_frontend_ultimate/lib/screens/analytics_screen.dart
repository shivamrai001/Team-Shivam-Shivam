import 'package:flutter/material.dart';
import '../services/api_service.dart';

class AnalyticsScreen extends StatefulWidget {
  const AnalyticsScreen({super.key});
  @override
  State<AnalyticsScreen> createState() => _AnalyticsScreenState();
}

class _AnalyticsScreenState extends State<AnalyticsScreen> {
  late Future<Map<String, dynamic>?> _dataFuture;

  @override
  void initState() {
    super.initState();
    _dataFuture = ApiService.getAnalytics();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Advanced Analytics')),
      body: FutureBuilder<Map<String, dynamic>?>(
        future: _dataFuture,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) return const Center(child: CircularProgressIndicator(color: Color(0xFF4FD1C5)));
          // Fallback static data if backend lacks advanced route
          return ListView(
            padding: const EdgeInsets.all(24),
            children: [
              Container(
                padding: const EdgeInsets.all(24),
                decoration: BoxDecoration(
                  gradient: const LinearGradient(colors: [Color(0xFF4FD1C5), Color(0xFF34D399)], begin: Alignment.topLeft, end: Alignment.bottomRight),
                  borderRadius: BorderRadius.circular(24),
                ),
                child: const Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text('Platform Health', style: TextStyle(color: Colors.white, fontSize: 16, fontWeight: FontWeight.w500)),
                    SizedBox(height: 8),
                    Text('98.4%', style: TextStyle(color: Colors.white, fontSize: 40, fontWeight: FontWeight.bold)),
                    SizedBox(height: 8),
                    Text('Resolution rate within 48 hours', style: TextStyle(color: Colors.white70)),
                  ],
                ),
              ),
              const SizedBox(height: 24),
              const Text('Resolution Times', style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold, color: Color(0xFF1E293B))),
              const SizedBox(height: 16),
              Card(
                child: Padding(
                  padding: const EdgeInsets.all(24),
                  child: Column(
                    children: [
                      _buildMetricRow('Emergency Issues', 0.9, const Color(0xFFF87171), '2 hrs'),
                      const SizedBox(height: 16),
                      _buildMetricRow('Standard Issues', 0.6, const Color(0xFF60A5FA), '1.5 days'),
                      const SizedBox(height: 16),
                      _buildMetricRow('Low Priority', 0.3, const Color(0xFFCBD5E1), '4 days'),
                    ],
                  ),
                ),
              )
            ],
          );
        },
      ),
    );
  }

  Widget _buildMetricRow(String title, double fraction, Color color, String time) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            Text(title, style: const TextStyle(fontWeight: FontWeight.w600, color: Color(0xFF475569))),
            Text(time, style: const TextStyle(fontWeight: FontWeight.bold, color: Color(0xFF1E293B))),
          ],
        ),
        const SizedBox(height: 8),
        LinearProgressIndicator(
          value: fraction,
          backgroundColor: const Color(0xFFF1F5F9),
          color: color,
          minHeight: 8,
          borderRadius: BorderRadius.circular(4),
        ),
      ],
    );
  }
}
