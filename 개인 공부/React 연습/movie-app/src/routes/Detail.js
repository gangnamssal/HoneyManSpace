import { useEffect, useCallback, useState } from "react";
import { useParams } from "react-router-dom";
function Detail() {
  const { id } = useParams();
  const [movie, setMovie] = useState({});
  const getMovie = useCallback(async () => {
    const json = await (
      await fetch(`https://yts.mx/api/v2/movie_details.json?movie_id=${id}`)
    ).json();
    setMovie(json.data.movie);
  }, [id]);
  // console.log(movie);
  useEffect(() => {
    getMovie();
  }, [getMovie]);
  return (
    <div>
      <h1>Detail</h1>
      <img src={movie.medium_cover_image} alt="img" />
    </div>
  );
}
export default Detail;
