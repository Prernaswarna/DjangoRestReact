import React, { Component } from "react";
import { render } from "react-dom";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      code: [],
      loaded: false,
      placeholder: "Loading"
    };
  }

  componentDidMount() {
    fetch("https://internet.channeli.in/oauth/authorise/?client_id=k9IXT2RD811seHEj8858BIo24rVCCDHsY50ucEj9/redirect_url=127.0.0.8000/user/confirm")
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(code => {
        this.setState(() => {
          return {
            code,
            loaded: true
          };
        });
      });
  }

  render() {
    return (<p>{this.state.code}</p>);
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);
