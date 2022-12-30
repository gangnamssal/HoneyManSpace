import { useState, useEffect } from "react";

function App() {
  const [loading, setLoading] = useState(true);
  const [movies, setMovies] = useState([]);

  const getMovies = async () => {
    const json = await (
      await fetch(`https://yts.mx/api/v2/list_movies.json?minimum_rating=8.5`)
    ).json();
    setMovies(json.data.movies);
    setLoading(false);
  };

  useEffect(() => {
    getMovies();
  }, []);

  console.log(movies);
  return (
    <div>
      {loading ? (
        <h1>Loading...</h1>
      ) : (
        <div>
          {movies.map((movie) => {
            return (
              <div key={movie.id}>
                <img src={movie.medium_cover_image} alt="img" />
                <h1>{movie.title}</h1>
                <p>{movie.summary}</p>
                <ul>
                  {movie.genres.map((g) => {
                    return <li key={g}>{g}</li>;
                  })}
                </ul>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}

export default App;
