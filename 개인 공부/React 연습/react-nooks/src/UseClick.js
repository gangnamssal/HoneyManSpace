const useClick = (onClick) => {
  if (typeof onClick !== "function") {
    return;
  }

  const element = useRef();

  useEffect(() => {
    if (element.current) {
      element.current.addEventListener("click", onClick);
    }

    // return은 componentWillUnMount때 호출된다.
    return () => {
      if (element.current) {
        element.current.removeEventListener("click", onClick);
      }
    };
  }, []);
  return element;
};
