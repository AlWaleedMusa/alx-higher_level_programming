$.get("https://swapi.co/api/films/?format=json", function (data) {
    $("ul#list_movies").append(
        ...data.results.map((movie) => `<li>${movie.title}</li>`)
    );
});
