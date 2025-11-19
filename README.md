# Production Line Simulator

A web-based manufacturing simulation that models a three-stage production line process. This interactive simulator demonstrates how materials move through different manufacturing stages with random variations in production output.

## Demo

![Production Line Simulator Demo](demo.gif)

## Features

- **Three-Stage Production Line**: Materials progress through Forming, CNC, and Buffing stations
- **Random Production Variations**: Each station has configurable min/max output ranges
- **Real-time Visualization**: See materials move through each stage of the production process
- **Interactive Controls**: Run, show, reset, and adjust settings through an intuitive UI
- **Responsive Design**: Works on desktop and mobile devices
- **Visual Feedback**: Animations and highlighting show active processing stations

## How It Works

The simulation models a manufacturing process where:

1. **Materials Supply**: 30 raw materials are supplied per turn (configurable)
2. **Forming Station**: Processes materials with random output between 28-30 units
3. **CNC Station**: Processes formed parts with random output between 28-30 units
4. **Buffing Station**: Finishes CNC parts with random output between 28-29 units
5. **Completed Products**: Finished items are counted in the completed total

Each station has a queue where materials wait to be processed. The random variations simulate real-world factors that might affect production efficiency.

## Technologies Used

- **HTML5**: Structure and content
- **CSS3**: Styling and animations
- **JavaScript**: Simulation logic and interactivity
- **No external dependencies**: Pure web technologies only

## Getting Started

1. Clone or download this repository
2. Open `index.html` in any modern web browser
3. Start the simulation by clicking "Run" or pressing Enter

## Controls

- **Run (Enter)**: Advance the simulation by one turn
- **Show (S)**: Refresh the display without advancing
- **Reset (RS)**: Reset the simulation to initial state
- **Settings (ST)**: Open settings to adjust parameters

## Customization

You can adjust the following parameters through the settings menu:

- **Materials per Turn**: Change how many raw materials are supplied each turn
- **Forming Station**: Adjust min/max production range
- **CNC Station**: Adjust min/max production range
- **Buffing Station**: Adjust min/max production range

## File Structure

```
production_line/
├── index.html          # Main HTML structure
├── styles.css          # All styling and animations
├── script.js           # Simulation logic and interactivity
└── README.md           # This file
```

## Browser Support

Works in all modern browsers that support:
- ES6 JavaScript
- CSS3 animations and flexbox
- HTML5

Tested in:
- Chrome
- Firefox
- Safari
- Edge

## Development

To modify the simulator:

1. Edit `index.html` to change the structure
2. Modify `styles.css` to change appearance
3. Update `script.js` to change simulation logic

## License

This project is open source and available under the MIT License.

## Acknowledgments

Based on a Python console application, converted to a web-based interactive experience with enhanced visualization and user interface.