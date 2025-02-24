<?php
// Check if the form has been submitted and a file is uploaded
if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_FILES['file'])) {
    // Set the upload directory and file path
    $uploadDirectory = 'uploads/';
    $filePath = $uploadDirectory . basename($_FILES['file']['name']);

    // Check if the file is an image
    if (getimagesize($_FILES['file']['tmp_name'])) {
        // Try to move the uploaded file to the desired location
        if (move_uploaded_file($_FILES['file']['tmp_name'], $filePath)) {
            echo json_encode(['status' => 'success', 'message' => 'File uploaded successfully.']);
        } else {
            echo json_encode(['status' => 'error', 'message' => 'Sorry, there was an error uploading your file.']);
        }
    } else {
        echo json_encode(['status' => 'error', 'message' => 'Please upload a valid image file.']);
    }
} else {
    echo json_encode(['status' => 'error', 'message' => 'No file uploaded.']);
}
