import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      fruits: [],
    };
  }

  componentDidMount() {
    fetch('http://localhost:8000/fruits')
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        this.setState({ fruits: data });
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  }

  render() {
    const { fruits } = this.state;

    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            Edit <code>src/App.js</code> and save to reload.
          </p>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>
          <div>
            <h2>Fruits List</h2>
            <ul>
             {console.log(this.state.fruits)}
            </ul>
          </div>
        </header>
      </div>
    );
  }
}

export default App;