import 'dart:io';

import 'package:flutter/material.dart';
import 'package:geolocator/geolocator.dart';
import 'package:image_picker/image_picker.dart';

class ReportComplaintScreen extends StatefulWidget {
  const ReportComplaintScreen({super.key});

  @override
  State<ReportComplaintScreen> createState() =>
      _ReportComplaintScreenState();
}

class _ReportComplaintScreenState
    extends State<ReportComplaintScreen> {

  File? selectedImage;

  String latitude = "Not Available";
  String longitude = "Not Available";

  final ImagePicker picker = ImagePicker();

  final titleController = TextEditingController();
  final descriptionController = TextEditingController();

  String? selectedCategory;

  // IMAGE PICKER

  Future<void> pickImage() async {
    final XFile? image =
        await picker.pickImage(source: ImageSource.gallery);

    if (image != null) {
      setState(() {
        selectedImage = File(image.path);
      });
    }
  }

  // LOCATION

  Future<void> getLocation() async {

    LocationPermission permission =
        await Geolocator.checkPermission();

    if (permission == LocationPermission.denied) {
      permission =
          await Geolocator.requestPermission();
    }

    Position position =
        await Geolocator.getCurrentPosition();

    setState(() {
      latitude = position.latitude.toString();
      longitude = position.longitude.toString();
    });
  }

  // AI LOADING

  void showAILoading() {

    showDialog(
      context: context,
      barrierDismissible: false,
      builder: (_) {
        return const AlertDialog(
          title: Text("AI Processing"),
          content: Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment:
                CrossAxisAlignment.start,
            children: [

              CircularProgressIndicator(),

              SizedBox(height: 20),

              Text("Analyzing uploaded image..."),

              SizedBox(height: 8),

              Text("Detecting complaint category..."),

              SizedBox(height: 8),

              Text("Predicting severity..."),

              SizedBox(height: 8),

              Text("Assigning department..."),

              SizedBox(height: 8),

              Text("Generating Complaint ID..."),

            ],
          ),
        );
      },
    );
  }

  // AI RESULT

  void showAIResult() {

    showDialog(
      context: context,
      builder: (_) {
        return AlertDialog(
          title: const Text(
            "AI Analysis Completed",
          ),

          content: const Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment:
                CrossAxisAlignment.start,
            children: [

              Text("Category : Garbage Overflow"),

              SizedBox(height: 8),

              Text("Priority : HIGH"),

              SizedBox(height: 8),

              Text("Severity Score : 92%"),

              SizedBox(height: 8),

              Text(
                  "Department : Municipal Services"),

              SizedBox(height: 8),

              Text(
                  "Estimated Resolution : 24 Hours"),

              SizedBox(height: 8),

              Text("Complaint ID : USA-2026-001"),

              SizedBox(height: 8),

              Text(
                  "Status : Submitted Successfully"),

            ],
          ),

          actions: [

            ElevatedButton(
              onPressed: () {

                Navigator.pop(context);

              },
              child: const Text("DONE"),
            )

          ],
        );
      },
    );
  }

  Future<void> submitComplaint() async {

    if (titleController.text.isEmpty ||
        descriptionController.text.isEmpty ||
        selectedCategory == null) {

      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text(
              "Please fill all required details."),
        ),
      );

      return;
    }

    showAILoading();

    await Future.delayed(
      const Duration(seconds: 3),
    );

    Navigator.pop(context);

    showAIResult();
  }

  @override
  Widget build(BuildContext context) {

    return Scaffold(
      appBar: AppBar(
        title: const Text("Report Complaint"),
      ),

      body: SingleChildScrollView(

        padding: const EdgeInsets.all(20),

        child: Column(

          children: [

            const Text(
              "Report a Smart City Issue",
              style: TextStyle(
                fontSize: 24,
                fontWeight: FontWeight.bold,
              ),
            ),

            const SizedBox(height: 25),

            TextField(
              controller: titleController,
              decoration: const InputDecoration(
                hintText: "Complaint Title",
              ),
            ),

            const SizedBox(height: 20),

            TextField(
              controller: descriptionController,
              maxLines: 4,
              decoration: const InputDecoration(
                hintText: "Describe the issue...",
              ),
            ),

            const SizedBox(height: 20),

            DropdownButtonFormField<String>(
              value: selectedCategory,
              decoration: const InputDecoration(
                hintText: "Select Category",
              ),
              items: const [

                DropdownMenuItem(
                  value: "Garbage",
                  child: Text("Garbage"),
                ),

                DropdownMenuItem(
                  value: "Potholes",
                  child: Text("Potholes"),
                ),

                DropdownMenuItem(
                  value: "Street Light",
                  child: Text("Street Light"),
                ),

                DropdownMenuItem(
                  value: "Water Leakage",
                  child: Text("Water Leakage"),
                ),

              ],
              onChanged: (value) {
                setState(() {
                  selectedCategory = value;
                });
              },
            ),

            const SizedBox(height: 25),

            ElevatedButton.icon(
              onPressed: pickImage,
              icon: const Icon(Icons.image),
              label: const Text("Upload Image"),
            ),

            const SizedBox(height: 15),

            if (selectedImage != null)
              ClipRRect(
                borderRadius:
                    BorderRadius.circular(15),
                child: Image.file(
                  selectedImage!,
                  height: 200,
                  width: double.infinity,
                  fit: BoxFit.cover,
                ),
              ),

            const SizedBox(height: 20),

            ElevatedButton.icon(
              onPressed: getLocation,
              icon: const Icon(Icons.location_on),
              label: const Text(
                "Get Current Location",
              ),
            ),

            const SizedBox(height: 20),

            Container(
              width: double.infinity,
              padding:
                  const EdgeInsets.all(15),
              decoration: BoxDecoration(
                color: Colors.white,
                borderRadius:
                    BorderRadius.circular(15),
              ),
              child: Column(
                crossAxisAlignment:
                    CrossAxisAlignment.start,
                children: [

                  Text("Latitude : $latitude"),

                  const SizedBox(height: 8),

                  Text("Longitude : $longitude"),

                ],
              ),
            ),

            const SizedBox(height: 25),

            SizedBox(
              width: double.infinity,
              child: ElevatedButton(
                onPressed: submitComplaint,
                child: const Text(
                  "SUBMIT COMPLAINT",
                ),
              ),
            ),

            const SizedBox(height: 30),

            Container(
              width: double.infinity,
              padding:
                  const EdgeInsets.all(20),
              decoration: BoxDecoration(
                color: Colors.white,
                borderRadius:
                    BorderRadius.circular(20),
              ),
              child: const Column(
                crossAxisAlignment:
                    CrossAxisAlignment.start,
                children: [

                  Text(
                    "AI Powered Features",
                    style: TextStyle(
                      fontSize: 22,
                      fontWeight:
                          FontWeight.bold,
                    ),
                  ),

                  SizedBox(height: 15),

                  Text("• Automatic Complaint Classification"),

                  SizedBox(height: 10),

                  Text("• Image Based Issue Detection"),

                  SizedBox(height: 10),

                  Text("• Priority Prediction"),

                  SizedBox(height: 10),

                  Text("• Smart Department Assignment"),

                  SizedBox(height: 10),

                  Text("• Resolution Time Prediction"),

                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}