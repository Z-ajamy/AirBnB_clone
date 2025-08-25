# 0x01. AirBnB clone - Web static

## Description

This project is part of the AirBnB clone series, focusing on creating the web static components. The goal is to build the front-end step by step, starting with simple HTML static pages, styling them with CSS, and organizing the project structure for future integration with back-end functionality.

This web static version serves as the foundation for understanding the project structure, design patterns, and user interface elements that will later be integrated with dynamic content and database functionality.

## Project Structure

```
web_static/
├── styles/
│   ├── 4-common.css
│   ├── 3-header.css
│   ├── 3-footer.css
│   ├── 6-filters.css
│   └── 8-places.css
├── images/
│   ├── icon.png
│   ├── logo.png
│   └── icon_*
├── 0-index.html
├── 1-index.html
├── 2-index.html
├── 3-index.html
├── 4-index.html
├── 5-index.html
├── 6-index.html
├── 7-index.html
└── 8-index.html
```

## Technologies Used

- **HTML5**: Semantic markup for structure
- **CSS3**: Styling and layout (no JavaScript allowed)
- **Flexbox**: Modern layout techniques
- **Responsive Design**: Mobile-first approach

## Features

- Clean, semantic HTML structure
- Progressive enhancement through multiple iterations
- Responsive design principles
- Cross-browser compatibility
- Accessible user interface
- Static prototype of AirBnB interface including:
  - Header with logo and user menu
  - Search filters (location, guests, etc.)
  - Places listings with details
  - Footer information

## File Descriptions

### HTML Files
- `0-index.html`: Basic HTML structure with inline styling
- `1-index.html`: HTML with head styling
- `2-index.html`: HTML with external CSS files
- `3-index.html`: Added header and footer
- `4-index.html`: Enhanced styling with common.css
- `5-index.html`: Added search filters
- `6-index.html`: Improved filters with dropdowns
- `7-index.html`: Added places section
- `8-index.html`: Complete layout with place details

### CSS Files
- `4-common.css`: Common styles (body, container)
- `3-header.css`: Header component styles
- `3-footer.css`: Footer component styles
- `6-filters.css`: Search filters styling
- `8-places.css`: Places section styling

## Getting Started

### Prerequisites

- Web browser (Chrome, Firefox, Safari, etc.)
- Text editor (VS Code, Sublime Text, etc.)
- Basic understanding of HTML and CSS

### Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/AirBnB_clone.git
```

2. Navigate to the web_static directory:
```bash
cd AirBnB_clone/web_static
```

3. Open any HTML file in your web browser:
```bash
# Using a simple HTTP server (recommended)
python3 -m http.server 8000

# Or directly open the file
open 8-index.html  # macOS
xdg-open 8-index.html  # Linux
```

## Usage

### Viewing the Static Pages

1. Start from `0-index.html` to see the progression
2. Each file builds upon the previous version
3. The final version (`8-index.html`) shows the complete static interface
4. Open files in your browser to see the rendered pages

### Development Workflow

1. Edit HTML files to modify structure
2. Update CSS files to change styling
3. Refresh browser to see changes
4. Use browser developer tools for debugging

## Design Requirements

### HTML Standards
- HTML5 doctype
- Semantic markup
- Proper nesting and indentation
- Valid HTML (W3C compliant)

### CSS Standards
- External stylesheets only (no inline CSS after task 1)
- No use of `!important`
- No use of IDs in CSS
- Cross-browser compatibility
- Flexible layout using modern CSS

### Accessibility
- Proper heading hierarchy
- Alt text for images
- Semantic HTML elements
- Keyboard navigation support

## Browser Compatibility

Tested and compatible with:
- Chrome 57+
- Firefox 53+
- Safari 10+
- Edge 16+

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Coding Standards

- Use 4 spaces for indentation
- Follow HTML5 semantic standards
- Use meaningful class names
- Comment complex CSS rules
- Maintain consistent formatting

## Project Timeline

- **Task 0-1**: Basic HTML structure and styling methods
- **Task 2-3**: External CSS and layout components
- **Task 4-5**: Enhanced styling and search functionality
- **Task 6-7**: Advanced filters and content sections
- **Task 8**: Complete static prototype

## Future Enhancements

This static version will be enhanced in future projects with:
- Dynamic content loading
- Database integration
- User authentication
- Booking functionality
- API integration
- JavaScript interactivity

## Resources

- [HTML5 Documentation](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS3 Reference](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [Flexbox Guide](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
- [W3C Markup Validator](https://validator.w3.org/)

## License

This project is part of the ALX Software Engineering curriculum.

## Author

**Abd_al-rahman Ajamy**  
Email: abdorahman0283@gmail.com  
---

*This project is part of the ALX Software Engineering Program - AirBnB Clone series*
