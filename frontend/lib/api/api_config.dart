import 'dart:io' show Platform;
import 'package:flutter/foundation.dart' show kIsWeb;

class ApiConfig {
  static String get baseUrl {
    // Check if URL is injected during build (e.g., flutter build --dart-define=API_URL=https://myapi.com)
    const String prodUrl = String.fromEnvironment('API_URL');
    if (prodUrl.isNotEmpty) {
      return prodUrl;
    }

    if (kIsWeb) {
      return 'http://127.0.0.1:8000';
    } else if (Platform.isAndroid) {
      // Android Emulator maps 10.0.2.2 to host machine's localhost
      return 'http://10.0.2.2:8000';
    } else {
      // iOS Simulator and Desktop platforms
      return 'http://127.0.0.1:8000';
    }
  }

  static String get apiVersion => '/api';
  static String get fullUrl => '$baseUrl$apiVersion';
}
