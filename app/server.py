import time
import uuid
import structlog
import boto3
from flask import Flask, request, jsonify, g
from config import CLOUDWATCH_NAMESPACE, AWS_REGION, APP_PORT

structlog.configure(
    processors=[
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.stdlib.add_log_level,
        structlog.processors.JSONRenderer()
    ]
)

logger = structlog.get_logger()
app = Flask(__name__)

cloudwatch = boto3.client("cloudwatch", region_name=AWS_REGION)


def put_metric(metric_name, value, unit="Count"):
    try:
        cloudwatch.put_metric_data(
            Namespace=CLOUDWATCH_NAMESPACE,
            MetricData=[
                {
                    "MetricName": metric_name,
                    "Value": value,
                    "Unit": unit
                }
            ]
        )
        logger.info(
            "metric_sent",
            metric_name=metric_name,
            value=value,
            unit=unit
        )
    except Exception as e:
        logger.error(
            "metric_send_failed",
            metric_name=metric_name,
            error=str(e)
        )


@app.before_request
def before_request():
    g.start_time = time.time()
    g.correlation_id = request.headers.get("X-Correlation-ID", str(uuid.uuid4()))


@app.after_request
def after_request(response):
    latency_ms = round((time.time() - g.start_time) * 1000, 2)

    logger.info(
        "request_completed",
        correlation_id=g.correlation_id,
        path=request.path,
        method=request.method,
        status_code=response.status_code,
        latency_ms=latency_ms,
        metric_request_count=1
    )

    put_metric("RequestCount", 1, "Count")

    return response


@app.route("/")
def home():
    logger.info(
        "request_received",
        correlation_id=g.correlation_id,
        path="/",
        method=request.method
    )

    return jsonify({
        "message": "Service is running",
        "correlation_id": g.correlation_id
    })


@app.route("/health")
def health():
    logger.info(
        "health_check",
        correlation_id=g.correlation_id,
        path="/health",
        method=request.method,
        status="healthy"
    )

    return jsonify({
        "status": "healthy",
        "correlation_id": g.correlation_id
    })


@app.route("/order", methods=["POST"])
def create_order():
    data = request.get_json(silent=True) or {}

    order_id = f"ord-{uuid.uuid4().hex[:8]}"
    amount = data.get("amount", 0)
    items = data.get("items", 0)
    user_id = data.get("user_id", "unknown")

    logger.info(
        "order_created",
        correlation_id=g.correlation_id,
        order_id=order_id,
        amount=amount,
        items=items,
        user_id=user_id,
        metric_orders_created=1,
        metric_order_value=amount,
        path="/order",
        method=request.method
    )

    put_metric("OrdersCreated", 1, "Count")
    put_metric("OrderValue", float(amount), "None")

    return jsonify({
        "status": "created",
        "order_id": order_id,
        "correlation_id": g.correlation_id
    }), 201


@app.route("/slow")
def slow():
    logger.warning(
        "slow_request_started",
        correlation_id=g.correlation_id,
        path="/slow",
        method=request.method
    )

    time.sleep(5)

    logger.info(
        "slow_request_finished",
        correlation_id=g.correlation_id,
        delay_seconds=5
    )

    return jsonify({
        "status": "slow response completed",
        "correlation_id": g.correlation_id
    })


@app.route("/error")
def error():
    logger.error(
        "simulated_error",
        correlation_id=g.correlation_id,
        path="/error",
        method=request.method,
        message="This is a test error endpoint",
        metric_error_count=1
    )

    put_metric("ErrorCount", 1, "Count")

    return jsonify({
        "status": "error",
        "message": "Simulated internal error",
        "correlation_id": g.correlation_id
    }), 500


if __name__ == "__main__":
    logger.info("application_started", port=APP_PORT)
    app.run(host="0.0.0.0", port=APP_PORT)
