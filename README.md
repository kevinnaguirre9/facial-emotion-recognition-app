# 🔭 Facial Emotion Recognition App

Welcome to the Facial Emotion Recognition App, a real-time web application designed to monitor students' moods in a classroom. Utilizing a convolutional neural network with Python, Streamlit, and Streamlit WebRTC, this app provides insightful emotion analysis in educational environments.

## Features

- **Real-Time Emotion Recognition**: Uses advanced CNN to identify and analyze emotions in real-time.
- **Streamlit Integration**: Offers a user-friendly web interface for easy interaction and monitoring.
- **Educational Focus**: Tailored to understand and improve the classroom experience.

## Getting Started 🚀

### Prerequisites

- Docker and Docker Compose

### Environment Setup

```bash
# Copy environment variables
cp .env.example .env

# Start development containers
docker-compose up
```
### Run tests
    
Execute tests as described in [the Python unittest documentation.](https://docs.python.org/3/library/unittest.html#command-line-interface).

```bash
docker-compose exec app python -m unittest -v <test_class_directory>
```

## Collaborators 👥

This project is the result of the collaborative efforts of these fantastic individuals:
- Kevin Aguirre [Github](https://github.com/kevinnaguirre9) - [Linkedin](https://www.linkedin.com/in/kevinnaguirre9/)
- Sergio Díaz [Github](https://github.com/codediaz) - [Linkedin](https://www.linkedin.com/in/sergio-diaz-fernandez/)
  
We thank them for their invaluable contributions and expertise.

## License  
  
This project is open-sourced software licensed unde the [MIT license](https://github.com/codediaz/facial-emotion-recognition-app/blob/master/LICENSE).
