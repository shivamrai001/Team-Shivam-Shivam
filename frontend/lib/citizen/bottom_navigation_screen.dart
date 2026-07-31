import 'package:flutter/material.dart';

import '../admin/analytics_screen.dart';
import '../admin/dashboard_screen.dart';
import 'home_screen.dart';
import 'profile_screen.dart';
import 'report_complaint_screen.dart';

class BottomNavigationScreen extends StatefulWidget {
  const BottomNavigationScreen({super.key});

  @override
  State<BottomNavigationScreen> createState() =>
      _BottomNavigationScreenState();
}

class _BottomNavigationScreenState
    extends State<BottomNavigationScreen> {

  int currentIndex = 0;

  final List<Widget> screens = const [

    HomeScreen(),

    ReportComplaintScreen(),

    DashboardScreen(),

    AnalyticsScreen(),

    ProfileScreen(),

  ];

  @override
  Widget build(BuildContext context) {

    return Scaffold(

      body: screens[currentIndex],

      bottomNavigationBar: NavigationBar(

        selectedIndex: currentIndex,

        onDestinationSelected: (index) {

          setState(() {

            currentIndex = index;

          });

        },

        destinations: const [

          NavigationDestination(
            icon: Icon(Icons.home_outlined),
            label: "Home",
          ),

          NavigationDestination(
            icon: Icon(Icons.report_problem_outlined),
            label: "Report",
          ),

          NavigationDestination(
            icon: Icon(Icons.dashboard_outlined),
            label: "Dashboard",
          ),

          NavigationDestination(
            icon: Icon(Icons.analytics_outlined),
            label: "Analytics",
          ),

          NavigationDestination(
            icon: Icon(Icons.person_outline),
            label: "Profile",
          ),
        ],
      ),
    );
  }
}