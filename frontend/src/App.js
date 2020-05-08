import React, { Component } from 'react';
import './App.css';

class App extends Component {

	constructor(props) {
		super(props);
		this.state = {
			tip: {
				id: null,
				body: '',
				author: '',
			}
		}

		this.getRandomTip = this.getRandomTip.bind(this);
	}

	componentWillMount() {
		this.getRandomTip();
	}

	getRandomTip() {

		console.log('Fetching...');

		fetch('http://127.0.0.1:8000/api/random-tip/')
			.then(response => response.json())
			.then(data => {
				this.setState({
					tip: data
				})

				console.log('Complete');
			})
	}

	render() {

		return (
			<div className="App">

				<nav>
					
				</nav>
			<header className="App-header">

				<h1>Random Life-Changing Tip</h1>
				
				<div className="tip-card">
					<p>{this.state.tip.body}</p>

					<p className="author">By <span>{this.state.tip.author}</span></p>
				</div>
				
				<button className="btn-accent" onClick={this.getRandomTip}>Random Tip</button>
			</header>
			</div>
		);
	}
}

export default App;
