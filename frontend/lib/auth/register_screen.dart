import 'package:flutter/material.dart';

import '../citizen/bottom_navigation_screen.dart';
import '../widgets/custom_button.dart';
import '../widgets/custom_textfield.dart';

class RegisterScreen extends StatelessWidget {
  const RegisterScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final nameController = TextEditingController();
    final emailController = TextEditingController();
    final passwordController = TextEditingController();

    return Scaffold(
      appBar: AppBar(
        title: const Text("Create Account"),
      ),
      body: Padding(
        padding: const EdgeInsets.all(25),
        child: SingleChildScrollView(
          child: Column(
            children: [
              const SizedBox(height: 30),

              const Icon(
                Icons.person_add_alt_1,
                size: 80,
                color: Color(0xFF2563EB),
              ),

              const SizedBox(height: 20),

              const Text(
                "Register",
                style: TextStyle(
                  fontSize: 28,
                  fontWeight: FontWeight.bold,
                ),
              ),

              const SizedBox(height: 10),

              const Text(
                "Create your UrbanSense AI account",
              ),

              const SizedBox(height: 40),

              CustomTextField(
                hintText: "Full Name",
                icon: Icons.person_outline,
                controller: nameController,
              ),

              const SizedBox(height: 20),

              CustomTextField(
                hintText: "Email Address",
                icon: Icons.email_outlined,
                controller: emailController,
              ),

              const SizedBox(height: 20),

              CustomTextField(
                hintText: "Password",
                icon: Icons.lock_outline,
                controller: passwordController,
                obscureText: true,
              ),

              const SizedBox(height: 30),

              CustomButton(
                title: "REGISTER",
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

              const SizedBox(height: 20),

              TextButton(
                onPressed: () {
                  Navigator.pop(context);
                },
                child: const Text(
                  "Already have an account? Login",
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}