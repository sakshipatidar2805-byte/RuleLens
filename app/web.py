from pathlib import Path

from flask import Flask, render_template, request

from .main import run_rulelens


BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = BASE_DIR / "templates"

app = Flask(
    __name__,
    template_folder=str(TEMPLATE_DIR),
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    attendance = request.form.get("attendance", "")
    medical = request.form.get("medical", "no")
    medical_approved = request.form.get(
        "medical_approved",
        "no",
    )

    try:
        decision = run_rulelens(
            attendance=attendance,
            medical=medical,
            medical_approved=medical_approved,
        )

        return render_template(
            "result.html",
            decision=decision,
        )

    except (ValueError, FileNotFoundError) as error:
        return render_template(
            "result.html",
            error=str(error),
        )


if __name__ == "__main__":
    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000,
    )