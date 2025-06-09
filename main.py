import app as app
import specifications as specs

import uvicorn

if __name__ == "__main__":
    # Use specifications from the specs file (if applicable)
    host = specs.HOST if hasattr(specs, 'HOST') else '127.0.0.1'
    port = specs.PORT if hasattr(specs, 'PORT') else 8000

    # Run the FastAPI app
    uvicorn.run(app.app, host=host, port=port)