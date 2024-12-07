from django.shortcuts import render
from src.DimondPricePrediction.pipelines.prediction_pipeline import CustomData, PredictPipeline
def home_page(request):
    return render(request, "templates/index.html")

def predict_datapoint(request):
    if request.method == 'GET':
        return render(request, "templates/form.html")
    else:
        data = CustomData(
            carat=float(request.POST.get('carat')),
            depth=float(request.POST.get('depth')),
            table=float(request.POST.get('table')),
            x=float(request.POST.get('x')),
            y=float(request.POST.get('y')),
            z=float(request.POST.get('z')),
            cut=request.POST.get('cut'),
            color=request.POST.get('color'),
            clarity=request.POST.get('clarity')
        )
        final_data = data.get_data_as_dataframe()
        predict_pipeline = PredictPipeline()
        pred = predict_pipeline.predict(final_data)
        result = round(pred[0], 2)
        return render(request, "templates/result.html", {'final_result': result})
