import 'package:flutter/material.dart';
import '../services/api_service.dart';

class FeedbackScreen extends StatefulWidget {
  const FeedbackScreen({super.key});
  @override
  State<FeedbackScreen> createState() => _FeedbackScreenState();
}

class _FeedbackScreenState extends State<FeedbackScreen> {
  final _commentController = TextEditingController();
  int _rating = 5;
  bool _isSubmitting = false;

  void _submit() async {
    if (_commentController.text.isEmpty) return;
    setState(() => _isSubmitting = true);
    bool success = await ApiService.submitFeedback(_rating, _commentController.text);
    setState(() => _isSubmitting = false);
    
    if (success && mounted) {
      _commentController.clear();
      ScaffoldMessenger.of(context).showSnackBar(const SnackBar(content: Text('Thank you for your feedback!'), backgroundColor: Color(0xFF34D399)));
      setState(() {});
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Community Feedback')),
      body: FutureBuilder<List<dynamic>>(
        future: ApiService.getFeedbacks(),
        builder: (context, snapshot) {
          final history = snapshot.data ?? [];
          return ListView(
            padding: const EdgeInsets.all(24),
            children: [
              Card(
                child: Padding(
                  padding: const EdgeInsets.all(24),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      const Text('Rate your experience', style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: Color(0xFF1E293B))),
                      const SizedBox(height: 16),
                      Row(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: List.generate(5, (index) {
                          return IconButton(
                            icon: Icon(index < _rating ? Icons.star_rounded : Icons.star_border_rounded),
                            color: const Color(0xFFFBBF24),
                            iconSize: 40,
                            onPressed: () => setState(() => _rating = index + 1),
                          );
                        }),
                      ),
                      const SizedBox(height: 24),
                      TextField(
                        controller: _commentController,
                        maxLines: 4,
                        decoration: const InputDecoration(labelText: 'Tell us how we can improve...', alignLabelWithHint: true),
                      ),
                      const SizedBox(height: 24),
                      SizedBox(
                        width: double.infinity,
                        child: ElevatedButton(
                          onPressed: _isSubmitting ? null : _submit,
                          child: _isSubmitting ? const CircularProgressIndicator(color: Colors.white) : const Text('Submit Feedback'),
                        ),
                      )
                    ],
                  ),
                ),
              ),
              const SizedBox(height: 32),
              const Text('Recent Feedback', style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold, color: Color(0xFF1E293B))),
              const SizedBox(height: 16),
              ...history.map((f) => Card(
                child: ListTile(
                  leading: const CircleAvatar(backgroundColor: Color(0xFFF1F5F9), child: Icon(Icons.person, color: Color(0xFF94A3B8))),
                  title: Row(children: List.generate(5, (i) => Icon(Icons.star, size: 16, color: i < (f['rating'] ?? 5) ? const Color(0xFFFBBF24) : const Color(0xFFE2E8F0)))),
                  subtitle: Padding(
                    padding: const EdgeInsets.only(top: 8.0),
                    child: Text(f['comment'] ?? '', style: const TextStyle(color: Color(0xFF475569))),
                  ),
                ),
              )),
            ],
          );
        },
      ),
    );
  }
}
