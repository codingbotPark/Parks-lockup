import { createGlobalStyle } from "styled-components";
import "./app.css";
import reset from "styled-reset";

const GlobalStyle = createGlobalStyle`
  ${reset}
`;

export default GlobalStyle;
