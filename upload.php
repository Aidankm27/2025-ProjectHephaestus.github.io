<?php
// Tell the browser that we are returning JSON
header('Content-Type: application/json');

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Define the upload directory (make sure this directory exists and is writable)
    $uploadDirectory = '/var/www/html/uploads/';

    // The 'file' index here corresponds to the name attribute in your HTML form's file input.
    $filename = basename($_FILES['file']['name']);
    $targetFile = $uploadDirectory . $filename;

    // Check for errors during upload
    if ($_FILES['file']['error'] !== UPLOAD_ERR_OK) {
        http_response_code(400);
        echo json_encode(array("error" => "Error during file upload."));
        exit;
    }

    // Move the uploaded file from its temporary location to the uploads directory
    if (move_uploaded_file($_FILES['file']['tmp_name'], $targetFile)) {
        echo json_encode(array(
            "success" => true,
            "message" => "File uploaded successfully.",
            "filename" => $filename
        ));
    } else {
        http_response_code(500);
        echo json_encode(array("error" => "Failed to move the uploaded file."));
    }
} else {
    // If the request method is not POST, return an error
    http_response_code(405);
    echo json_encode(array("error" => "Method not allowed."));
}
?>
