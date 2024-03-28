// function generateText() {

//     // Display loading animation
//     $("#loading").show();

//     var prompt = document.getElementById("prompt").value;

//     $.ajax({
//         url: "/generate",
//         type: "POST",
//         data: { prompt: prompt },
//         success: function(response) {
//             document.getElementById("generated_text").innerHTML = response.generated_text;
//         },
//         error: function(error) {
//             console.log("Error:", error);
//         }
//     });
// }


function generateText() {
    // Display loading animation
    $("#loading").show();

    // Fetch prompt from textarea
    var prompt = document.getElementById("prompt").value;

    // Make API call to generate text
    $.ajax({
        type: "POST",
        url: "/generate",
        data: { prompt: prompt },
        success: function(response) {
            // Hide loading animation
            $("#loading").hide();

            // Display generated text
            document.getElementById("generated_text").innerHTML = response.generated_text;
        },
        error: function(error) {
            // Hide loading animation
            $("#loading").hide();

            // Handle error
            console.error("Error:", error);
        }
    });
}

