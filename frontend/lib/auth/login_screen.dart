import 'package:flutter/material.dart';

import '../citizen/bottom_navigation_screen.dart';
import '../widgets/custom_button.dart';
import '../widgets/custom_textfield.dart';
import 'register_screen.dart';

class LoginScreen extends StatelessWidget {
  const LoginScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final emailController = TextEditingController();
    final passwordController = TextEditingController();

    return Scaffold(
      body: SafeArea(
        child: Center(
          child: SingleChildScrollView(
            padding: const EdgeInsets.symmetric(
              horizontal: 24,
              vertical: 20,
            ),
            child: Column(
              children: [

                Container(
                  height: 120,
                  width: 120,
                  decoration: BoxDecoration(
                    color: Colors.white,
                    borderRadius: BorderRadius.circular(25),
                    boxShadow: [
                      BoxShadow(
                        color: Colors.black.withOpacity(0.08),
                        blurRadius: 10,
                        offset: const Offset(0, 5),
                      ),
                    ],
                  ),
                  child: const Icon(
                    Icons.location_city,
                    size: 70,
                    color: Color(0xFF2563EB),
                  ),
                ),

                const SizedBox(height: 30),

                const Text(
                  "UrbanSense AI 2.0",
                  style: TextStyle(
                    fontSize: 30,
                    fontWeight: FontWeight.bold,
                  ),
                ),

                const SizedBox(height: 8),

                const Text(
                  "Smart City Analytics Platform",
                  style: TextStyle(
                    color: Colors.grey,
                    fontSize: 16,
                  ),
                ),

                const SizedBox(height: 45),

                const Align(
                  alignment: Alignment.centerLeft,
                  child: Text(
                    "Welcome Back",
                    style: TextStyle(
                      fontSize: 26,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                ),

                const SizedBox(height: 8),

                const Align(
                  alignment: Alignment.centerLeft,
                  child: Text(
                    "Login to continue",
                    style: TextStyle(
                      color: Colors.grey,
                    ),
                  ),
                ),

                const SizedBox(height: 30),

                CustomTextField(
                  controller: emailController,
                  hintText: "Email Address",
                  icon: Icons.email_outlined,
                ),

                const SizedBox(height: 20),

                CustomTextField(
                  controller: passwordController,
                  hintText: "Password",
                  icon: Icons.lock_outline,
                  obscureText: true,
                ),

                const SizedBox(height: 30),

                SizedBox(
                  width: double.infinity,
                  child: CustomButton(
                    title: "LOGIN",
                    onPressed: () {
                      Navigator.pushReplacement(
                        context,
                        MaterialPageRoute(
                          builder: (context) =>
                              const BottomNavigationScreen(),
                        ),
                      );
                    },
                  ),
                ),

                const SizedBox(height: 20),

                TextButton(
                  onPressed: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) =>
                            const RegisterScreen(),
                      ),
                    );
                  },
                  child: const Text(
                    "Create a New Account",
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}