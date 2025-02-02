function fetchGameData() {
    fetch('http://127.0.0.1:5000/get_game_data')
        .then(response => response.json())
        .then(data => {
            if (data && Array.isArray(data)) {
                // Update image paths to use the game_image endpoint
                gameData = data.map(question => ({
                    ...question,
                    image_path: `http://127.0.0.1:5000${question.image_path}`  // Correct path for images
                }));
                initializeGame();
            } else {
                console.error("Error: No game data received");
            }
        })
        .catch(error => console.error("Error fetching game data:", error));
}
