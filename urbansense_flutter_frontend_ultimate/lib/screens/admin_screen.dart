import 'package:flutter/material.dart';
import '../services/api_service.dart';

class AdminScreen extends StatefulWidget {
  const AdminScreen({super.key});
  @override
  State<AdminScreen> createState() => _AdminScreenState();
}

class _AdminScreenState extends State<AdminScreen> {
  late Future<List<dynamic>> _complaintsFuture;

  @override
  void initState() {
    super.initState();
    _fetchData();
  }

  void _fetchData() {
    setState(() { _complaintsFuture = ApiService.getAllComplaints(); });
  }

  void _updateStatus(int id, String status) async {
    bool success = await ApiService.updateComplaintStatus(id, status);
    if (success && mounted) {
      ScaffoldMessenger.of(context).showSnackBar(const SnackBar(content: Text('Status updated'), backgroundColor: Color(0xFF4FD1C5)));
      _fetchData();
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Admin Console')),
      body: FutureBuilder<List<dynamic>>(
        future: _complaintsFuture,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) return const Center(child: CircularProgressIndicator(color: Color(0xFF4FD1C5)));
          final data = snapshot.data ?? [];
          return ListView.builder(
            padding: const EdgeInsets.all(24),
            itemCount: data.length,
            itemBuilder: (context, index) {
              final item = data[index];
              return Card(
                child: Padding(
                  padding: const EdgeInsets.all(20),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: [
                          Expanded(child: Text(item['title'] ?? 'No Title', style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: Color(0xFF1E293B)))),
                          Container(
                            padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
                            decoration: BoxDecoration(color: const Color(0xFFF8FAFC), borderRadius: BorderRadius.circular(20)),
                            child: Text(item['status'] ?? 'Unknown', style: const TextStyle(color: Color(0xFF4FD1C5), fontWeight: FontWeight.w600, fontSize: 12)),
                          )
                        ],
                      ),
                      const SizedBox(height: 12),
                      Text(item['description'] ?? '', style: const TextStyle(color: Color(0xFF64748B))),
                      const SizedBox(height: 16),
                      const Divider(color: Color(0xFFF1F5F9)),
                      Row(
                        mainAxisAlignment: MainAxisAlignment.end,
                        children: [
                          TextButton(onPressed: () => _updateStatus(item['id'], 'Pending'), child: const Text('Set Pending', style: TextStyle(color: Color(0xFFF59E0B)))),
                          const SizedBox(width: 8),
                          ElevatedButton(
                            style: ElevatedButton.styleFrom(padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8)),
                            onPressed: () => _updateStatus(item['id'], 'Resolved'), 
                            child: const Text('Resolve'),
                          ),
                        ],
                      )
                    ],
                  ),
                ),
              );
            },
          );
        },
      ),
    );
  }
}
