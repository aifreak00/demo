from fastapi import FastAPI
from lazypredict import LazyClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
import uvicorn

app=FastAPI()

@app.get("/train")
async def classification():
    data=load_breast_cancer()
    x=data.data
    y=data.target
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.5)
    clf=LazyClassifier()
    models,predictions=clf.fit(x_train,x_test,y_train,y_test)
    models_dict=models.to_dict(orient="index")
    return models_dict

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,port=8000)