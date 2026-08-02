import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  // Your live FastAPI backend URL hosted on Render
  static const String baseUrl = 'https://team-shivam-shivam-10.onrender.com';

  static Future<bool> login(String email, String password) async {
    try {
      final response = await http.post(
        Uri.parse('$baseUrl/login'), // Adjust to match your exact FastAPI route (e.g., /api/login or /token)
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({
          'email': email,
          'password': password,
        }),
      );

      // If the backend accepts the credentials and returns a success status (200 OK)
      if (response.statusCode == 200) {
        return true;
      } else {
        print('Backend rejected login: ${response.body}');
        return false;
      }
    } catch (e) {
      print('Connection error: $e');
      return false;
    }
  }
}
