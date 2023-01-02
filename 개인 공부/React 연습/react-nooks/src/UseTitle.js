const useTitle = (initialTitle) => {
  const [title, setTitle] = useState(initialTitle);
  const updateTitle = () => {
    const hemlTitle = document.querySelector("title");
    hemlTitle.textContent = title;
  };
  useEffect(updateTitle, [title]);
  return setTitle;
};
