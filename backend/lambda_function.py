import json, boto3, base64

runtime = boto3.client("sagemaker-runtime")
s3      = boto3.client("s3")

ENDPOINT    = "pytorch-inference-2026-04-20-13-02-06-558"   # from Cell 4 output
BUCKET      = "crop-disease-ruchita"            # your bucket

LABELS = [
    "Apple - Apple Scab","Apple - Black Rot","Apple - Cedar Apple Rust",
    "Apple - Healthy","Blueberry - Healthy","Cherry - Powdery Mildew",
    "Cherry - Healthy","Corn - Cercospora Leaf Spot","Corn - Common Rust",
    "Corn - Northern Leaf Blight","Corn - Healthy","Grape - Black Rot",
    "Grape - Esca (Black Measles)","Grape - Leaf Blight","Grape - Healthy",
    "Orange - Haunglongbing (Citrus Greening)","Peach - Bacterial Spot",
    "Peach - Healthy","Pepper - Bacterial Spot","Pepper - Healthy",
    "Potato - Early Blight","Potato - Late Blight","Potato - Healthy",
    "Raspberry - Healthy","Soybean - Healthy","Squash - Powdery Mildew",
    "Strawberry - Leaf Scorch","Strawberry - Healthy","Tomato - Bacterial Spot",
    "Tomato - Early Blight","Tomato - Late Blight","Tomato - Leaf Mold",
    "Tomato - Septoria Leaf Spot","Tomato - Spider Mites","Tomato - Target Spot",
    "Tomato - Yellow Leaf Curl Virus","Tomato - Mosaic Virus","Tomato - Healthy"
]

def lambda_handler(event, context):
    try:
        if event.get("httpMethod") == "OPTIONS":
            return cors_response(200, {})

        body        = json.loads(event.get("body", "{}"))
        image_b64   = body.get("image", "")
        if not image_b64:
            return cors_response(400, {"error": "No image received"})

        image_bytes = base64.b64decode(image_b64)

        # Store image in S3
        s3.put_object(Bucket=BUCKET, Key="uploads/latest.jpg",
                      Body=image_bytes, ContentType="image/jpeg")

        # Call SageMaker
        resp       = runtime.invoke_endpoint(
            EndpointName = ENDPOINT,
            ContentType  = "application/x-image",
            Body         = image_bytes
        )
        result     = json.loads(resp["Body"].read())
        pred       = result.get("prediction", [[0, 0, 0]])[0]
        idx        = int(pred[0])
        confidence = round(float(pred[1]) * 100, 1)
        label      = LABELS[idx] if idx < len(LABELS) else "Unknown"
        is_healthy = "Healthy" in label

        return cors_response(200, {
            "label":      label,
            "confidence": confidence,
            "is_healthy": is_healthy
        })

    except Exception as e:
        return cors_response(500, {"error": str(e)})

def cors_response(code, body):
    return {
        "statusCode": code,
        "headers": {
            "Access-Control-Allow-Origin":  "*",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Methods": "POST,OPTIONS"
        },
        "body": json.dumps(body)
    }