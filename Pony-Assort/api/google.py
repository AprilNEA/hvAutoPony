from google.cloud import aiplatform

def predict_image_classification_sample(
    endpoint: str, instance: dict, parameters_dict: dict
):
    client_options = dict(api_endpoint="us-central1-prediction-aiplatform.googleapis.com")
    client = aiplatform.gapic.PredictionServiceClient(client_options=client_options)
    from google.protobuf import json_format
    from google.protobuf.struct_pb2 import Value

    # See gs://google-cloud-aiplatform/schema/predict/params/image_classification_1.0.0.yaml for the format of the parameters.
    parameters = json_format.ParseDict(parameters_dict, Value())

    # See gs://google-cloud-aiplatform/schema/predict/instance/image_classification_1.0.0.yaml for the format of the instances.
    instances_list = [instance]
    instances = [json_format.ParseDict(s, Value()) for s in instances_list]
    response = client.predict(
        endpoint=endpoint, instances=instances, parameters=parameters
    )

    print("response")
    print(" deployed_model_id:", response.deployed_model_id)
    predictions = response.predictions
    print("predictions")
    for prediction in predictions:
        # See gs://google-cloud-aiplatform/schema/predict/prediction/classification_1.0.0.yaml for the format of the predictions.
        print(" prediction:", dict(prediction))