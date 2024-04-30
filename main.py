from fastapi import FastAPI

app = FastAPI()


@app.get('/api/v1/comments/{commentable_id}')
def get_comments(commentable_id: int):
    return {
        "commentable_id": commentable_id,
        "message": "ok"
    }


@app.post('/api/v1/comments/{commend_id}/verify')
def verify_comments(comment_id: int):
    return {
        "message": "ok"
    }


@app.delete('/api/v1/comments/{comment_id}')
def delete_comment():
    return {}



@app.get('/api/v1/comments/unverified-comments')
def unverified_comments():
    return {}
