import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';

class ApiService {
  static const String baseUrl = 'https://team-shivam-shivam-9.onrender.com/api';

  static Future<String?> getToken() async {
    final prefs = await SharedPreferences.getInstance();
    return prefs.getString('urbansense_token');
  }

  static Future<void> saveToken(String token) async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.setString('urbansense_token', token);
  }

  static Future<void> logout() async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.remove('urbansense_token');
  }

  // --- Auth ---
  static Future<bool> login(String email, String password) async {
    try {
      final response = await http.post(
        Uri.parse('$baseUrl/users/login'),
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({'email': email, 'password': password}),
      );
      if (response.statusCode == 200) {
        final data = jsonDecode(response.body);
        await saveToken(data['access_token']);
        return true;
      }
      return false;
    } catch (e) { return false; }
  }

  // --- Citizen Dashboard ---
  static Future<Map<String, dynamic>?> getDashboardSummary() async {
    final token = await getToken();
    try {
      final response = await http.get(Uri.parse('$baseUrl/dashboard/summary'), headers: {'Authorization': 'Bearer $token'});
      if (response.statusCode == 200) return jsonDecode(response.body);
    } catch (e) {}
    return null;
  }

  // --- Maps ---
  static Future<List<dynamic>> getMapMarkers() async {
    final token = await getToken();
    try {
      final response = await http.get(Uri.parse('$baseUrl/maps/markers'), headers: {'Authorization': 'Bearer $token'});
      if (response.statusCode == 200) return jsonDecode(response.body);
    } catch (e) {}
    return [];
  }

  // --- Notifications ---
  static Future<List<dynamic>> getNotifications() async {
    final token = await getToken();
    try {
      final response = await http.get(Uri.parse('$baseUrl/notifications/'), headers: {'Authorization': 'Bearer $token'});
      if (response.statusCode == 200) return jsonDecode(response.body);
    } catch (e) {}
    return [];
  }

  // --- Complaints ---
  static Future<String?> uploadImage(String filePath) async {
    final token = await getToken();
    try {
      var request = http.MultipartRequest('POST', Uri.parse('$baseUrl/uploads/image'));
      request.headers['Authorization'] = 'Bearer $token';
      request.files.add(await http.MultipartFile.fromPath('file', filePath));
      var streamedResponse = await request.send();
      if (streamedResponse.statusCode == 200) {
        var responseData = await streamedResponse.stream.bytesToString();
        return jsonDecode(responseData)['image_path'];
      }
    } catch (e) {}
    return null;
  }

  static Future<bool> submitComplaint(Map<String, dynamic> data) async {
    final token = await getToken();
    try {
      final response = await http.post(
        Uri.parse('$baseUrl/complaints/'),
        headers: {'Content-Type': 'application/json', 'Authorization': 'Bearer $token'},
        body: jsonEncode(data),
      );
      return response.statusCode == 200 || response.statusCode == 201;
    } catch (e) { return false; }
  }

  // --- Admin Panel ---
  static Future<List<dynamic>> getAllComplaints() async {
    final token = await getToken();
    try {
      final response = await http.get(Uri.parse('$baseUrl/admin/complaints'), headers: {'Authorization': 'Bearer $token'});
      if (response.statusCode == 200) return jsonDecode(response.body);
    } catch (e) {}
    return [];
  }

  static Future<bool> updateComplaintStatus(int id, String status) async {
    final token = await getToken();
    try {
      final response = await http.put(
        Uri.parse('$baseUrl/admin/complaints/$id'),
        headers: {'Content-Type': 'application/json', 'Authorization': 'Bearer $token'},
        body: jsonEncode({'status': status}),
      );
      return response.statusCode == 200;
    } catch (e) { return false; }
  }

  // --- Advanced Analytics ---
  static Future<Map<String, dynamic>?> getAnalytics() async {
    final token = await getToken();
    try {
      final response = await http.get(Uri.parse('$baseUrl/analytics/data'), headers: {'Authorization': 'Bearer $token'});
      if (response.statusCode == 200) return jsonDecode(response.body);
    } catch (e) {}
    return null;
  }

  // --- Feedback ---
  static Future<bool> submitFeedback(int rating, String comment) async {
    final token = await getToken();
    try {
      final response = await http.post(
        Uri.parse('$baseUrl/feedback/'),
        headers: {'Content-Type': 'application/json', 'Authorization': 'Bearer $token'},
        body: jsonEncode({'rating': rating, 'comment': comment}),
      );
      return response.statusCode == 200 || response.statusCode == 201;
    } catch (e) { return false; }
  }

  static Future<List<dynamic>> getFeedbacks() async {
    final token = await getToken();
    try {
      final response = await http.get(Uri.parse('$baseUrl/feedback/'), headers: {'Authorization': 'Bearer $token'});
      if (response.statusCode == 200) return jsonDecode(response.body);
    } catch (e) {}
    return [];
  }
}
