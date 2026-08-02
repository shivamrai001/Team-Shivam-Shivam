import 'dart:io';
import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import '../services/api_service.dart';

class ComplaintScreen extends StatefulWidget {
  const ComplaintScreen({super.key});
  @override
  State<ComplaintScreen> createState() => _ComplaintScreenState();
}

class _ComplaintScreenState extends State<ComplaintScreen> {
  final _titleController = TextEditingController();
  final _descController = TextEditingController();
  final _latController = TextEditingController();
  final _lngController = TextEditingController();
  
  File? _imageFile;
  bool _isSubmitting = false;

  Future<void> _pickImage() async {
    final picker = ImagePicker();
    final picked = await picker.pickImage(source: ImageSource.gallery);
    if (picked != null) {
      setState(() => _imageFile = File(picked.path));
    }
  }

  void _submit() async {
    if (_titleController.text.isEmpty || _latController.text.isEmpty) return;
    setState(() => _isSubmitting = true);

    String? imagePath;
    if (_imageFile != null) {
      imagePath = await ApiService.uploadImage(_imageFile!.path);
    }

    bool success = await ApiService.submitComplaint({
      'title': _titleController.text,
      'description': _descController.text,
      'latitude': double.tryParse(_latController.text) ?? 0.0,
      'longitude': double.tryParse(_lngController.text) ?? 0.0,
      'image_path': imagePath,
    });

    setState(() => _isSubmitting = false);

    if (success && mounted) {
      ScaffoldMessenger.of(context).showSnackBar(const SnackBar(
        content: Text('Report submitted successfully!'),
        behavior: SnackBarBehavior.floating,
        backgroundColor: Color(0xFF34D399),
        shape: StadiumBorder(),
      ));
      _titleController.clear();
      _descController.clear();
      _latController.clear();
      _lngController.clear();
      setState(() => _imageFile = null);
    }
  }

  @override
  Widget build(BuildContext context) {
    return SingleChildScrollView(
      padding: const EdgeInsets.symmetric(horizontal: 24.0, vertical: 16.0),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          const Text('New Report', style: TextStyle(fontSize: 28, fontWeight: FontWeight.bold, color: Color(0xFF1E293B))),
          const SizedBox(height: 8),
          const Text('Help us improve the community by reporting issues.', style: TextStyle(color: Color(0xFF94A3B8), fontSize: 16)),
          const SizedBox(height: 32),
          
          Container(
            padding: const EdgeInsets.all(24),
            decoration: BoxDecoration(
              color: Colors.white,
              borderRadius: BorderRadius.circular(24),
              boxShadow: [BoxShadow(color: const Color(0xFFE2E8F0).withOpacity(0.5), blurRadius: 10, offset: const Offset(0, 4))],
            ),
            child: Column(
              children: [
                TextField(controller: _titleController, decoration: const InputDecoration(labelText: 'Issue Title', prefixIcon: Icon(Icons.title_rounded))),
                const SizedBox(height: 16),
                TextField(controller: _descController, maxLines: 3, decoration: const InputDecoration(labelText: 'Detailed Description', alignLabelWithHint: true)),
                const SizedBox(height: 16),
                Row(
                  children: [
                    Expanded(child: TextField(controller: _latController, keyboardType: TextInputType.number, decoration: const InputDecoration(labelText: 'Latitude', prefixIcon: Icon(Icons.location_on_outlined)))),
                    const SizedBox(width: 16),
                    Expanded(child: TextField(controller: _lngController, keyboardType: TextInputType.number, decoration: const InputDecoration(labelText: 'Longitude'))),
                  ],
                ),
                const SizedBox(height: 24),
                InkWell(
                  onTap: _pickImage,
                  borderRadius: BorderRadius.circular(16),
                  child: Container(
                    padding: const EdgeInsets.all(20),
                    decoration: BoxDecoration(
                      color: const Color(0xFFF8FAFC),
                      border: Border.all(color: const Color(0xFFE2E8F0), style: BorderStyle.solid),
                      borderRadius: BorderRadius.circular(16),
                    ),
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        Icon(Icons.photo_library_rounded, color: _imageFile == null ? const Color(0xFF94A3B8) : const Color(0xFF4FD1C5)),
                        const SizedBox(width: 12),
                        Text(_imageFile == null ? 'Attach a Photo' : 'Photo Attached', style: TextStyle(color: _imageFile == null ? const Color(0xFF94A3B8) : const Color(0xFF4FD1C5), fontWeight: FontWeight.w600)),
                      ],
                    ),
                  ),
                ),
                const SizedBox(height: 32),
                SizedBox(
                  width: double.infinity,
                  child: ElevatedButton(
                    onPressed: _isSubmitting ? null : _submit,
                    child: _isSubmitting ? const SizedBox(width: 20, height: 20, child: CircularProgressIndicator(color: Colors.white, strokeWidth: 2)) : const Text('Submit Report'),
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
