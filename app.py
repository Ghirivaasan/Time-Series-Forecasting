from flask import Flask, render_template, request
from utils import fetch_data
from models import train_model
from eda import perform_eda

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            api_url = request.form["api_url"]
            target_col = request.form["target_col"]
            periods = int(request.form["periods"])
            model_type = request.form["model_type"]

            df = fetch_data(api_url)
            if isinstance(df, str):
                return render_template("error.html", error_message=df)

            eda_results, trend_plot = perform_eda(df)
            forecast_df, metrics, forecast_plot = train_model(df, model_type, periods)

            return render_template("results.html",
                                   eda_results=eda_results,
                                   forecast_df=forecast_df.to_dict(orient="records"),
                                   metrics=metrics,
                                   forecast_plot=forecast_plot)

        except Exception as e:
            return render_template("error.html", error_message=str(e))

    return render_template("index.html")


@app.route("/error")
def error():
    return render_template("error.html", error_message="An error occurred.")


if __name__ == "__main__":
    app.run(debug=True)
