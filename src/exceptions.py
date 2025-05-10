from fastapi import HTTPException, status


# Not found
NotFoundError = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
