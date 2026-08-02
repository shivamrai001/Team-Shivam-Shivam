import 'package:flutter/material.dart';
import '../services/api_service.dart';

class NotificationsScreen extends StatefulWidget {
  const NotificationsScreen({super.key});
  @override
  State<NotificationsScreen> createState() => _NotificationsScreenState();
}

class _NotificationsScreenState extends State<NotificationsScreen> {
  late Future<List<dynamic>> _notifsFuture;

  @override
  void initState() {
    super.initState();
    _notifsFuture = ApiService.getNotifications();
  }

  @override
  Widget build(BuildContext context) {
    return FutureBuilder<List<dynamic>>(
      future: _notifsFuture,
      builder: (context, snapshot) {
        if (snapshot.connectionState == ConnectionState.waiting) return const Center(child: CircularProgressIndicator(color: Color(0xFF4FD1C5)));
        final notifs = snapshot.data ?? [];
        return RefreshIndicator(
          color: const Color(0xFF4FD1C5),
          onRefresh: () async => setState(() { _notifsFuture = ApiService.getNotifications(); }),
          child: ListView.builder(
            padding: const EdgeInsets.symmetric(horizontal: 24.0, vertical: 16.0),
            itemCount: notifs.isEmpty ? 1 : notifs.length + 1,
            itemBuilder: (context, index) {
              if (index == 0) {
                return const Padding(
                  padding: EdgeInsets.only(bottom: 24.0),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text('Recent Alerts', style: TextStyle(fontSize: 28, fontWeight: FontWeight.bold, color: Color(0xFF1E293B))),
                      SizedBox(height: 8),
                      Text('Stay updated on issue resolutions.', style: TextStyle(color: Color(0xFF94A3B8), fontSize: 16)),
                    ],
                  ),
                );
              }
              if (notifs.isEmpty) return const Center(child: Text('All caught up!', style: TextStyle(color: Color(0xFF94A3B8))));
              
              final n = notifs[index - 1];
              return Card(
                child: ListTile(
                  contentPadding: const EdgeInsets.all(16),
                  leading: Container(
                    padding: const EdgeInsets.all(12),
                    decoration: BoxDecoration(color: const Color(0xFFF0FDF4), borderRadius: BorderRadius.circular(12)),
                    child: const Icon(Icons.notifications_active_rounded, color: Color(0xFF34D399)),
                  ),
                  title: Text(n['message'] ?? 'Alert', style: const TextStyle(fontWeight: FontWeight.w600, color: Color(0xFF1E293B))),
                  subtitle: Padding(
                    padding: const EdgeInsets.top(8.0),
                    child: Text(n['created_at'] != null ? n['created_at'].toString().split('T')[0] : '', style: const TextStyle(color: Color(0xFF94A3B8))),
                  ),
                ),
              );
            },
          ),
        );
      },
    );
  }
}
