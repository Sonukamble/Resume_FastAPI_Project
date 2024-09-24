import uvicorn
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

from Configuration import host_ip, host_port
# from resume_filter_API.operation.CRUD import add_user
from resume_filter_API.routes.Authentication import router
from resume_filter_API.routes.FileUpload import file_router
from resume_filter_API.routes.History import chat_history_router
from resume_filter_API.routes.Question import question_router
from resume_filter_API.routes.ResetRequest import reset_router


class ResumeAPI:
    def __init__(self):
        try:
            # Initialize the FastAPI app with metadata and custom responses
            self.app = FastAPI(
                title="dssd",
                version="1.0.0",
                description="gv",
                responses={
                    status.HTTP_404_NOT_FOUND: {
                        "description": "Page not found"
                    },
                    status.HTTP_422_UNPROCESSABLE_ENTITY: {
                        "description": "Validation error"
                    }
                }
            )
            origins = ["*"]

            self.app.add_middleware(
                CORSMiddleware,
                allow_origins=origins,
                allow_credentials=True,
                allow_methods=["*"],
                allow_headers=["*"],
            )
            # Add routes after initializing the app
            # self.add_routes()
            self.app.include_router(router)
            self.app.include_router(reset_router)
            self.app.include_router(file_router)
            self.app.include_router(question_router)
            self.app.include_router(chat_history_router)

        except Exception as e:
            print(e)

    def run(self):
        # Pass the app instance directly to uvicorn
        try:
            uvicorn.run(self.app, host=host_ip, port=host_port)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    # Instantiate the ResumeAPI class and run the application
    resume_api = ResumeAPI()
    resume_api.run()
